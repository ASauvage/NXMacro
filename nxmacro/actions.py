import time
from pathlib import Path

from .config import KEY_MAP, print_bindings
from .bot import Bot
from .macro import Macro, MacroEventButton, MacroEventStick


def record(host: str, port: int = 6000, filename: Path = Path("macro.json")) -> None:
    import keyboard

    bot = Bot(host, port)
    try:
        bot.connect()
    except (ConnectionRefusedError, TimeoutError, OSError) as e:
        print(f"Error: {e}")
        return

    try:
        bot.release_all()

        print_bindings()
        print("\nF9 = start  |  F10 = stop & save\n")
        keyboard.wait("f9")

        start = time.perf_counter()
        macro = Macro()
        held_keys = set()

        print("● Recording... press F10 to stop\n")

        def on_key(e) -> None:
            action = "click"
            if e.event_type == keyboard.KEY_DOWN:
                if e.name.lower() in held_keys:
                    return
                action = "press"
                held_keys.add(e.name.lower())
            elif e.event_type == keyboard.KEY_UP:
                action = "release"
                held_keys.discard(e.name.lower())
            
            btn = KEY_MAP.get(e.name.lower())
            if btn:
                t = round(time.perf_counter() - start, 4)
                macro.events.append(MacroEventButton(timestamp=t, action=action, button=btn))
                bot.send_command(f"{action} {btn}")
                print(f"  {t:.3f}s  {btn}")

        hook = keyboard.hook(on_key)
        keyboard.wait("f10")
        keyboard.unhook(hook)

        print(f"Saving macro file to {filename}...")
        macro.save(path=filename, indent=4)
        print("Saved.")
    finally:
        bot.release_all()
        bot.close()


def play(host: str, port: int = 6000, loop: int = 1, filename: Path = Path("macro.json")):
    loop_count = 0
    bot = Bot(host, port)

    try:
        bot.connect()
    except (ConnectionRefusedError, TimeoutError, OSError) as e:
        print(f"Error: {e}")
        return

    try:
        bot.release_all()
        macro = Macro.from_json(filename)
        print(f"Loaded macro '{macro.name}' — {len(macro.events)} events")

        while loop == 0 or loop_count < loop:
            print(f"Starting loop #{loop_count}/{loop}")
            start = time.perf_counter()

            for i, event in enumerate(macro.events, 1):
                target = start + event.timestamp
                remaining = target - time.perf_counter()
                if remaining > 0.001:
                    time.sleep(remaining - 0.001)
                while time.perf_counter() < target:
                    pass

                if isinstance(event, MacroEventButton):
                    bot.send_command(f"{event.action} {event.button}")
                    print(f"  [{i}/{len(macro.events)}] {event.timestamp:.3f}s  {event.action} {event.button}")

                elif isinstance(event, MacroEventStick):
                    bot.send_command(f"{event.action} {event.stick} {event.x} {event.y}")
                    print(f"  [{i}/{len(macro.events)}] {event.timestamp:.3f}s  {event.action} {event.stick} ({event.x}, {event.y})")

                else:
                    print(f"  [{i}/{len(macro.events)}] {event.timestamp:.3f}s  Skipping unknown event")
                    continue

            loop_count += 1
            print(f"Macro completed in {time.perf_counter() - start:.3f}s")
    finally:
        bot.release_all()
        bot.close()
