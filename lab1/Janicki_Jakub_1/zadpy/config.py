class Config:
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 8080
    SERVER_SOCKET_ADDR = (SERVER_IP, SERVER_PORT)
    MAX_CLIENTS_NUM = 10
    MAX_MSG_SIZE = 10000
    ENCODING = 'UTF-8'
    MULTICAST_GROUP = '224.0.0.1'
    MULTICAST_PORT = 8081
    MULTICAST_ADDR = (MULTICAST_GROUP, MULTICAST_PORT)
