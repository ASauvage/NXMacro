import json
from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime
from typing import Literal


@dataclass
class MacroEvent:
    timestamp: float

    def as_dict(self) -> dict:
        raise NotImplementedError


@dataclass
class MacroEventButton(MacroEvent):
    action: Literal["press", "release", "click"]
    button: str

    def as_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "action": self.action,
            "button": self.button
        }


@dataclass
class MacroEventStick(MacroEvent):
    action: Literal["setStick", "resetStick"]
    stick: Literal["LEFT", "RIGHT"]
    x: int
    y: int

    def as_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "action": self.action,
            "stick": self.stick,
            "x": self.x,
            "y": self.y
        }

 
@dataclass
class Macro:
    name: str = "unnamed"
    created: datetime = datetime.now()
    events: list[MacroEvent | MacroEventButton | MacroEventStick] = field(default_factory=list)
 
    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "created": self.created.isoformat(),
            "events": [event.as_dict() for event in self.events],
        }
    
    def save(self, path: Path, indent: int | None = None) -> None:
        with open(path, 'w', encoding="utf8") as macrofile:
            json.dump(self.as_dict(), macrofile, indent=indent, ensure_ascii=False)
 
    @classmethod
    def from_json(cls, path: Path) -> "Macro":
        with open(path, 'r', encoding="utf8") as jsonfile:
            data = json.load(jsonfile)
            events: list[MacroEvent] = []

            for event in data.get("events", []):
                if event.get("button", None):
                    events.append(MacroEventButton(**event))
                elif event.get("stick", None):
                    events.append(MacroEventStick(**event))

            return cls(
                name=data.get("name", "unnamed"),
                created=datetime.fromisoformat(data.get("created", datetime.now())),
                events=events
            )
