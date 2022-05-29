import Ice

from control.Client import Client

if __name__ == '__main__':
    try:
        with Ice.initialize("config.client") as communicator:
            client = Client(communicator)
            client.init_devices()
            client.run_io()
    except KeyboardInterrupt:
        exit(0)
    finally:
        print('Client shut down')
