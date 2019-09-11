from gabriel_server.network_engine import engine_server_shuttle
import logging


logging.basicConfig(level=logging.INFO)


def main():
    engine_server_shuttle.run()


if __name__ == '__main__':
    main()
