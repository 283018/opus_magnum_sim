from collections import defaultdict
from dataclasses import dataclass, field
from enum import IntEnum
from typing import TYPE_CHECKING

from opus_magnum_sym.elements.actions.actions import StepActionType

if TYPE_CHECKING:
    from opus_magnum_sym.elements.board import Hex


class ComponentAssignmentError(Exception):
    def __init__(
        self,
        message,
        component_type: ComponentType,
    ) -> None:
        self.message = message
        super().__init__(self.message)
        self.component_type = component_type


class ComponentType(IntEnum):
    """Full objects index, includes both base objects (manipulator bases, entrance) and dynamic parts as atoms"""

    EMPTY = -1
    ENTRANCE = 0
    EXIT = 1
    ARM = 2
    ARM_RETR = 3
    TRANSPORTER = 4


@dataclass
class Component:
    idx: int
    pos: Hex
    type: ComponentType = ComponentType.EMPTY
    rotation: int = 0
    _programm: defaultdict[int, StepActionType] = field(
        default_factory=lambda: defaultdict(lambda: StepActionType.NONE),
    )

    def assign_step_action(self, step: int, action: StepActionType):
        """
        Adds step action to program of current component.
        If action already assigned to provided step will overwrite previous action.
        """
        self._programm[step] = action

    def get_step_action(self, step) -> StepActionType:
        """
        Provides action assigned to given step.
        If none is assigned returns `StepActionType.NONE`
        """
        return self._programm.get(step, StepActionType.NONE)
