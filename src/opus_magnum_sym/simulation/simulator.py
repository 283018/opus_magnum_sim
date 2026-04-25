import opus_magnum_sym.elements.env.index_manager as im
from opus_magnum_sym.elements.board import Board, Hex
from opus_magnum_sym.elements.components import ComponentType


class Simulator:
    def __init__(self, size: tuple[int, int]) -> None:
        self.board: Board = Board(*size)
        self.im = im

    def add_component(
        self,
        cell: Hex,
        comp_type: ComponentType,
    ):
        new_id = im.allocate()
        self.board.place_componet(cell, comp_type, new_id)
