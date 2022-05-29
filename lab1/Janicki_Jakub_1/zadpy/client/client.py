import os
import select
import socket
import struct
import sys
from threading import Thread

from config import Config as config


class Client:
    def __init__(self):
        try:
            self.client_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            self.client_tcp_socket.connect(config.SERVER_SOCKET_ADDR)

            self.client_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            self.client_udp_socket.bind(('', self.client_tcp_socket.getsockname()[1]))

            self.client_mcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            self.client_mcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.client_mcast_socket.bind(('', config.MULTICAST_PORT))
            multicast_group = socket.inet_aton(config.MULTICAST_GROUP)
            multicast_request = struct.pack('4sL', multicast_group, socket.INADDR_ANY)
            self.client_mcast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, multicast_request)

            self.id = str(os.getpid())

            self.client_tcp_socket.send(bytes(self.id, config.ENCODING))
            self.sockets = [self.client_tcp_socket, self.client_udp_socket, self.client_mcast_socket]
            print(f"Client started: {self.id}")
            Thread(target=self.receive, daemon=True).start()
            self.send()
        except(KeyboardInterrupt, SystemExit, ConnectionRefusedError):
            self.client_tcp_socket.close()
            self.client_mcast_socket.close()
            self.client_udp_socket.close()
            print("Closing Client")
        finally:
            sys.exit()

    def receive(self):
        while True:
            msg = ""
            open_sockets, _, _ = select.select(self.sockets, [], [])
            if self.client_tcp_socket in open_sockets:
                msg_recv = str(self.client_tcp_socket.recv(config.MAX_MSG_SIZE), config.ENCODING)
                msg = f"[TCP]{msg_recv}"
            if self.client_udp_socket in open_sockets:
                msg_recv = str(self.client_udp_socket.recvfrom(config.MAX_MSG_SIZE)[0], config.ENCODING)
                msg = f"[UDP]{msg_recv}"
            if self.client_mcast_socket in open_sockets:
                msg_recv = str(self.client_mcast_socket.recvfrom(config.MAX_MSG_SIZE)[0], config.ENCODING)
                if msg_recv[:len(self.id)] != self.id:
                    msg = f"[MUL]{msg_recv}"
            if len(msg) > len("[PRE]"):
                print(msg)

    def send(self):
        while True:
            cmd = input().strip()
            if cmd[:2] == 'U:':
                self.client_udp_socket.sendto(bytes(cmd[2:], config.ENCODING), config.SERVER_SOCKET_ADDR)
            elif cmd[:2] == 'M:':
                self.client_mcast_socket.sendto(bytes(f"{str(self.id)}:{cmd[2:]}", config.ENCODING),
                                                config.MULTICAST_ADDR)
            elif cmd[:2] == "P:":
                with open('ascii_picture.txt') as f:
                    lines = f.readlines()
                for line in lines:
                    self.client_udp_socket.sendto(bytes(line[:-1], config.ENCODING), config.SERVER_SOCKET_ADDR)
            else:
                self.client_tcp_socket.send(bytes(cmd, config.ENCODING))
