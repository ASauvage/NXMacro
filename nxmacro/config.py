

def print_bindings() -> None:
    print("Key bindings:")
    for key, btn in KEY_MAP.items():
        print(f"  {key:<10} → {btn}")
    print()


BUTTONS = [
    "A", "B", "X", "Y",
    "L", "R", "ZL", "ZR",
    "PLUS", "MINUS",
    "HOME", "CAPTURE",
    "DLEFT", "DRIGHT", "DUP", "DDOWN",
    "LSTICK", "RSTICK",
]
 
STICKS = ["LEFT", "RIGHT"]

KEY_MAP = {
    "m": "A", "l": "B", "o": "X", "k": "Y",
    "i": "L", "p": "R", "a": "ZL", "e": "ZR",
    "&": "MINUS", "=": "PLUS",
    "return": "CAPTURE", "space": "HOME",
    "q": "DLEFT", "d": "DRIGHT", "z": "DUP", "s": "DDOWN",
    "g": "LSTICK", "h": "RSTICK"
}
