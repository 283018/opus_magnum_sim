from typing import TYPE_CHECKING

from icecream import ic

from opus_magnum_sym.elements.env import level_counter
from opus_magnum_sym.elements.actions.actions import StepActionType
from opus_magnum_sym.elements.components import ComponentType
from opus_magnum_sym.elements.components.base_component import Component
from opus_magnum_sym.elements.objects.base_object import ObjectType

if TYPE_CHECKING:
    from opus_magnum_sym.elements.board import Board, Hex


class Enter(Component):
    def __init__(
        self,
        idx: int,
        pos: Hex,
        object_type: ObjectType,
        rotation: int = 0,
    ) -> None:
        super().__init__(
            idx=idx,
            type=ComponentType.ENTRANCE,
            pos=pos,
            rotation=rotation,
        )
        self.object_type = object_type

    def _execute(self, board: Board, action_type: StepActionType) -> None:
        # action_type is stale here since spawning new objects depends on state of board
        if board.get_object(self.pos) == ObjectType.NONE:
            board.place_object(self.pos, self.object_type)


class Exit(Component):
    def __init__(
        self,
        idx: int,
        pos: Hex,
        object_type: ObjectType,
        rotation: int = 0,
    ) -> None:
        super().__init__(
            idx=idx,
            type=ComponentType.EXIT,
            pos=pos,
            rotation=rotation,
        )
        self.object_type = object_type

    def _execute(self, board: Board, action_type: StepActionType) -> None:
        # global CORRECT_FINISHED  # noqa: PLW0603
        if board.get_object(self.pos) == self.object_type:
            board.remove_object(self.pos)
            level_counter.CORRECT_FINISHED += 1
        ic(level_counter.CORRECT_FINISHED)
