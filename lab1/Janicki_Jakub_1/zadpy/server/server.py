import socket
import sys
from threading import Thread
from time import sleep

from config import Config as config
from server.clientsStorage import ClientStorage, ClientData


class Server:
    def __init__(self):
        try:
            self.server_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_tcp_socket.bind(config.SERVER_SOCKET_ADDR)
            self.server_tcp_socket.listen(config.MAX_CLIENTS_NUM)

            self.server_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            self.server_udp_socket.bind(config.SERVER_SOCKET_ADDR)

            self.clients = ClientStorage()

            Thread(target=self.udp_handler, daemon=True).start()
            Thread(target=self.tcp_handler, daemon=True).start()
            while True:
                sleep(1)
        except(KeyboardInterrupt, SystemExit):
            print("Closing server")
            self.clients.close_all()
            self.server_tcp_socket.close()
            self.server_udp_socket.close()
        finally:
            sys.exit()

    def new_client(self, new_client: ClientData):
        new_client.id = str(new_client.conn.recv(config.MAX_MSG_SIZE), config.ENCODING)
        self.clients.__add__(new_client)
        print(f"New client: {new_client.id}")

        while True:
            try:
                msg = new_client.conn.recv(config.MAX_MSG_SIZE)
            except OSError:
                return
            if msg:
                decoded_msg = str(msg, config.ENCODING)
                new_msg = f"{new_client.id}: {decoded_msg}"
                print(f"[TCP]{new_client.id}: {decoded_msg}")
                self.clients.broadcast_tcp(new_msg, new_client)

    def tcp_handler(self):
        print(f"Server started: {config.SERVER_IP}:{config.SERVER_PORT}")
        while True:
            conn, addr = self.server_tcp_socket.accept()
            client = ClientData(conn, addr)
            Thread(target=self.new_client, args=[client], daemon=True).start()

    def udp_handler(self):
        while True:
            try:
                msg, addr = self.server_udp_socket.recvfrom(config.MAX_MSG_SIZE)
            except OSError:
                return
            if msg:
                sender = self.clients.get_client(addr)
                decoded_msg = str(msg, config.ENCODING)
                new_msg = f"{sender.id}: {decoded_msg}"
                print(f"[UDP]{sender.id}: {decoded_msg}")
                self.clients.broadcast_upd(new_msg, sender, self.server_udp_socket)
