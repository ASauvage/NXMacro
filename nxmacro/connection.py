import socket


class Connection:
    host: str
    port: int
    _sock: socket.socket | None

    def __init__(self, host: str, port: int = 6000) -> None:
        self.host = host
        self.port = port

    def connect(self, timeout: int = 5) -> None:
        print(f"Connecting to {self.host}:{self.port} ...")
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.settimeout(timeout)
        self._sock.connect((self.host, self.port))
        print(f"Connected.")
    
    def close(self) -> None:
        if self._sock:
            self._sock.close()
            self._sock = None
            print(f"Disconnected.")
    
    def send(self, cmd: str) -> None:
        if not self._sock:
            raise RuntimeError("Not connected")
        
        self._sock.sendall((cmd + "\r\n").encode())
