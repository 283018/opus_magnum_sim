from icecream import ic

import opus_magnum_sym.elements.env.index_manager as im
from opus_magnum_sym.elements.board import Board, Hex
from opus_magnum_sym.elements.components import ComponentType, Enter, Exit, Manupulator


def main():
    board = Board(10, 10)

    # treat
    board.place_componet(Hex(2, 3), ComponentType.ENTRANCE, im.allocate())
    board.place_componet(Hex(3, 4), ComponentType.EXIT, im.allocate())
    board.place_componet(Hex(3, 3), ComponentType.ARM, im.allocate())

    ic(board.base_obj, board.objects)  # noqa: T201

    # TODO: add storing logic for instances of componenets
    arm = Manupulator()


if __name__ == "__main__":
    main()
