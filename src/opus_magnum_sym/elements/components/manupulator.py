from typing import TYPE_CHECKING

from opus_magnum_sym.elements.actions.actions import ActionAssignmentError, StepAction, StepActionType
from opus_magnum_sym.elements.components.base_component import Component, ComponentType
from opus_magnum_sym.elements.env import index_manager

if TYPE_CHECKING:
    from opus_magnum_sym.elements.board import Board, Hex


class Manupulator(Component):
    def __init__(self, idx: int | None, pos: Hex, rotation: int = 0) -> None:
        super().__init__(
            idx or index_manager.allocate(),
            ComponentType.ARM,
            pos,
            rotation,
        )
        self.holding = None

    def get_hand_pos(self) -> Hex:


    def _rotate_clw(self) -> None:
        self.rotation = ( self.rotation  + 1) % 6

    def _rotate_cclw(self) -> None:
        self.rotation = ( self.rotation  - 1) % 6

    def _extend(self) -> None:
        msg = "Assigned EXTEND action to component that does not support this action."
        raise ActionAssignmentError(msg, self.type, self.id)

    def _grab(self) -> None:
        ...



    def _execute(self, action: StepAction, board:Board) -> None:
        match action.type:
            case StepActionType.ROTATE_CLW:
                self._rotate_clw()
            case StepActionType.ROTATE_CCLW:
                self._rotate_cclw()
            case StepActionType.EXTEND:
                self._extend()
