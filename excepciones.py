#logs y excepciones

import logging

logging.basicConfig(
    filename="softwarefj_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass


class ReservaError(Exception):
    pass
