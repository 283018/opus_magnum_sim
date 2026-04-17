import opus_magnum_sym.elements.env.index_manager
from opus_magnum_sym.elements.actions.base_action import ComponentType
from opus_magnum_sym.elements.board import Board, Hex
from opus_magnum_sym.elements.components.base_component import Component
from opus_magnum_sym.elements.env.level_counter import CORRECT_FINISHED
from opus_magnum_sym.elements.objects.base_object import ObjectType


class Enter(Component):
    def __init__(
        self,
        idx: int | None,
        pos: Hex,
        object_type: ObjectType,
        rotation: int = 0,
    ) -> None:
        super().__init__(
            idx or opus_magnum_sym.elements.env.index_manager.allocate(),
            ComponentType.ENTRANCE,
            pos,
            rotation,
        )
        self.object_type = object_type

    def _execute(self, board: Board) -> None:
        if board.get_object(self.pos) == ObjectType.NONE:
            board.place_object(self.pos, self.object_type)


class Exit(Component):
    def __init__(
        self,
        idx: int | None,
        pos: Hex,
        object_type: ObjectType,
        rotation: int = 0,
    ) -> None:
        super().__init__(
            idx or opus_magnum_sym.elements.env.index_manager.allocate(),
            ComponentType.ENTRANCE,
            pos,
            rotation,
        )
        self.object_type = object_type

    def _execute(self, board: Board) -> None:
        if board.get_object(self.pos) == self.object_type:
            board.remove_object(self.pos)
        global CORRECT_FINISHED  # noqa: PLW0603
        CORRECT_FINISHED += 1
