from .cli import cli
from .actions import record, play


args = cli()

match args.command:
    case "record":
        record(args.host, args.port, args.file)
    case "play":
        play(args.host, args.port, args.loop ,args.file)
