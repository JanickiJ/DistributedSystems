from config import Config as config


class ClientData:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.id = None

    def __eq__(self, other):
        return self.id == other.id

    def close(self):
        print(f"Closing {self.id}")
        self.conn.close()


class ClientStorage:
    def __init__(self):
        self.clients = []

    def __add__(self, other: ClientData):
        self.clients.append(other)

    def broadcast_tcp(self, msg, sender: ClientData):
        for client in self.clients:
            if not client.__eq__(sender):
                try:
                    client.conn.send(bytes(msg, config.ENCODING))
                except BrokenPipeError:
                    self.close_client(client)

    def broadcast_upd(self, msg, sender: ClientData, server_socket):
        for client in self.clients:
            if not client.__eq__(sender):
                try:
                    server_socket.sendto(bytes(msg, config.ENCODING), client.addr)
                except BrokenPipeError:
                    self.close_client(client)

    def close_all(self):
        for client in self.clients:
            client.close()
        self.clients.clear()

    def close_client(self, client):
        client.close()
        self.clients.remove(client)

    def get_client(self, addr):
        for client in self.clients:
            if client.addr == addr:
                return client
        return None
