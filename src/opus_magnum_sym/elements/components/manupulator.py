from typing import TYPE_CHECKING

from opus_magnum_sym.elements.actions.actions import StepAction, StepActionType
from opus_magnum_sym.elements.actions.base_action import ActionAssignmentError
from opus_magnum_sym.elements.board import Direction
from opus_magnum_sym.elements.components.base_component import Component, ComponentType
from opus_magnum_sym.elements.env import index_manager
from opus_magnum_sym.elements.objects.base_object import ObjectType

if TYPE_CHECKING:
    from opus_magnum_sym.elements.board import Board, Hex


class Manupulator(Component):
    def __init__(self, idx: int | None, pos: Hex, rotation: int = 0, length: int = 1) -> None:
        super().__init__(
            idx or index_manager.allocate(),
            ComponentType.ARM,
            pos,
            rotation,
        )
        self.hand_length: int = length  # TODO: check correct length
        self.holding: ObjectType = ObjectType.NONE

    def get_hand_pos(self) -> Hex:
        return (
            Direction().from_rotation(self.hand_length)
            .apply(self.pos, self.hand_length)
        )  # fmt: skip

    def _rotate_clw(self) -> None:
        self.rotation = (self.rotation + 1) % 6

    def _rotate_cclw(self) -> None:
        self.rotation = (self.rotation - 1) % 6

    def _extend(self) -> None:
        msg = "Assigned EXTEND action to component that does not support this action."
        raise ActionAssignmentError(msg, self.type, self.id)

    def _retract(self) -> None:
        msg = "Assigned RETRACT action to component that does not support this action."
        raise ActionAssignmentError(msg, self.type, self.id)

    # TODO: for now just blindly removing/placing from/on board
    def _grab(self, board: Board) -> None:
        pos = self.get_hand_pos()
        obj = board.get_object(pos)
        if obj != ObjectType.NONE:
            self.holding = obj
            board.remove_object(pos)

    def _release(self, board: Board) -> None:
        pos = self.get_hand_pos()
        if self.holding != ObjectType.NONE:
            board.place_object(pos, self.holding)

    def _execute(self, action: StepAction, board: Board) -> None:
        match action.type:
            case StepActionType.ROTATE_CLW:
                self._rotate_clw()
            case StepActionType.ROTATE_CCLW:
                self._rotate_cclw()
            case StepActionType.EXTEND:
                self._extend()
