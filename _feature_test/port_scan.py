import socket
import os

def is_port_available(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # bind to create socket
        try:
            s.bind(("0.0.0.0", port))
        except OSError:
            # return False if port in use.
            return False
        else:
            # return True if port is Available.
            return True