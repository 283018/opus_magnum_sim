from dataclasses import dataclass, field
from enum import IntEnum
from typing import TYPE_CHECKING

from opus_magnum_sym.elements.actions.actions import StepAction, StepActionType

if TYPE_CHECKING:
    from opus_magnum_sym.elements.board import Hex


class ComponentType(IntEnum):
    """Full objects index, includes both base objects (manupulator bases, entrance) and dinamic parts as atoms"""

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
    pos: Hex
    rotation: int = 0
    program: list[StepAction] = field(default_factory=list)

    def ensure_slot(self, slot: int) -> None:
        while len(self.program) <= slot:
            self.program.append(StepAction(StepActionType.NONE))

    def set_step_action(self, slot: int, step_action: StepAction) -> None:
        self.ensure_slot(slot)
        self.program[slot] = step_action

    def remove_step_action(self, slot: int) -> None:
        if 0 <= slot < len(self.program):
            self.program[slot] = StepAction(StepActionType.NONE)
