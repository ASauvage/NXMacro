from argparse import ArgumentParser, Namespace
from pathlib import Path


def cli() -> Namespace:
    parser = ArgumentParser(description="Nintendo Switch macro recorder/player via sys-bot")

    parser.add_argument("-H", "--host", default="192.168.1.1",
                        help="Switch IP address (default: 192.168.1.1)")
    parser.add_argument("-p", "--port", type=int, default=6000,
                        help="sys-bot TCP port (default: 6000)")

    subparser = parser.add_subparsers(dest="command")

    # record
    record_parser = subparser.add_parser("record", help="Record a macro from your controller")
    record_parser.add_argument("-f", "--file", type=Path, default=Path("macro.json"),
                               help="Output .json file (default: macro.json)")
    
    # play
    play_parser = subparser.add_parser("play", help="Play back a macro on the Switch")
    play_parser.add_argument("-f", "--file", type=Path, default=Path("macro.json"),
                             help="Input .json macro file (default: macro.json)")
    play_parser.add_argument("-l", "--loop", type=int, default=1,
                             help="Repetitions (0 = infinite, default: 1)")
    play_parser.add_argument("--speed", type=float, default=1.0,
                             help="Playback speed multiplier (default: 1.0)")
 
    args = parser.parse_args()

    if args.command not in ["record", "play"]:
        parser.print_usage()
        exit(1)
    
    return args
