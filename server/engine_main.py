from gabriel_server.network_engine import engine_runner
from openrtist_engine import OpenrtistEngine
from openrtist_engine import ENGINE_NAME
import logging


ADDR = 'tcp://localhost:5555'


logging.basicConfig(level=logging.INFO)


def main():
    def engine_setup():
        return OpenrtistEngine(use_gpu=True)
    engine_runner.run(engine_setup, ENGINE_NAME, ADDR)


if __name__ == '__main__':
    main()
