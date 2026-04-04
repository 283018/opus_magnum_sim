from dataclasses import dataclass
from enum import IntEnum


class ComponentType(IntEnum):
    EMPTY = -1
    ENTRANCE = 0
    EXIT = 1
    ARM = 2
    ARM_RETR = 3
    TRANSPORTER = 4


@dataclass
class Component:
    id: int
    type: ComponentType
    x: int
    y: int
    rotation: int = 0
