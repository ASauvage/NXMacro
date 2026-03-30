

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
    "3": "A", "2": "B", "5": "X", "1": "Y",
    "4": "L", "6": "R", "7": "ZL", "9": "ZR",
    "-": "MINUS", "+": "PLUS",
    "return": "CAPTURE", "space": "HOME",
    "q": "DLEFT", "d": "DRIGHT", "z": "DUP", "s": "DDOWN",
    "j": "LSTICK", "k": "RSTICK"
}
