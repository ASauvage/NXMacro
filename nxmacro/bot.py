from .connection import Connection
from .config import BUTTONS


class Bot:
    _conn: Connection

    def __init__(self, host: str, port: int = 6000) -> None:
        self._conn = Connection(host, port)
    
    def send_command(self, cmd: str) -> None:
        self._conn.send(cmd)
    
    def press(self, btn: str) -> None:
        self._conn.send(f"press {btn}")

    def release(self, btn: str) -> None:
        self._conn.send(f"release {btn}")

    def click(self, btn: str) -> None:
        self._conn.send(f"click {btn}")

    def set_stick(self, stick: str, x: int, y: int) -> None:
        self._conn.send(f"setStick {stick} {x} {y}")

    def reset_stick(self, stick: str) -> None:
        self._conn.send(f"resetStick {stick}")
    
    def release_all(self) -> None:
        for btn in BUTTONS:
            self._conn.send(f"release {btn}")

    def connect(self) -> None:
        self._conn.connect()

    def close(self) -> None:
        self._conn.close()
