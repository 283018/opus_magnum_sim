from typing import TYPE_CHECKING

import opus_magnum_sym.elements.env.index_manager as im
from opus_magnum_sym.elements.actions.actions import StepActionType
from opus_magnum_sym.elements.board import Board, Hex
from opus_magnum_sym.elements.components import ComponentType
from opus_magnum_sym.elements.components.components_index import get_component_type

if TYPE_CHECKING:
    from opus_magnum_sym.elements.components.base_component import Component


# TODO: sprinkle Errors across simulation
class SimulationRuntimeError(Exception):
    def __init__(
        self,
        message,
        step: int,
    ) -> None:
        self.message = message
        super().__init__(self.message)


class Simulator:
    def __init__(self, size: tuple[int, int]) -> None:
        self.board: Board = Board(*size)
        self.im = im
        self.components: dict[int, Component] = {}
        self.step = 0

    def _verify_init_state(self):
        # TODO: create more granular verification if needed
        all_components = {comp.type for comp in self.components.values()}
        if not (ComponentType.ENTRANCE in all_components and ComponentType.EXIT in all_components):
            msg = "Incorrect initial state of board, ENTER or EXIT is missing."
            raise SimulationRuntimeError(msg, step=self.step)

    def next_step(self):
        if self.step == 0:
            self._verify_init_state()

        for component in self.components.items():
            print(component)

    # TODO: do something with kwargs
    # TODO: rework id logic (again)
    def add_component(
        self,
        cell: Hex,
        comp_type: ComponentType,
        **kwargs,
    ):
        new_id = im.allocate()
        self.board.place_componet(cell, comp_type, new_id)
        self.components[new_id] = get_component_type(comp_type)(idx=new_id, pos=cell, **kwargs)

    def assign_step_action(
        self,
        comp_id: int,
        step: int,
        action: StepActionType,
    ):
        self.components[comp_id].assign_step_action(step=step, action=action)
