from dataclasses import dataclass
from enum import IntEnum


class ActionType(IntEnum):
    ADD_COMPONENT = 0
    ADD_INSTRUCTION = 1
    REMOVE_COMPONENT = 2
    FINISH = 3


@dataclass
class Action:
    type: ActionType
    component_id: int | None = None
    x: int | None = None
    y: int | None = None
    component_type: int | None = None
    instruction_type: int | None = None
