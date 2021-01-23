__all__ = ["send"]

import json
import socket
from typing import Dict

SERVER_ADDRESS = ("raspberrypi.local", 35007)


def send(data: Dict) -> None:
    """Send data to server by serializing the provided
    dict and sending it.

    :param data: the data to be sent
    :type data: Dict
    """
    serialized_data = json.dumps(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(SERVER_ADDRESS)
        sock.sendall(bytes(serialized_data + "\n", "utf-8"))
