from opus_magnum_sym.elements.actions.actions import StepActionType
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from opus_magnum_sym.elements.actions.actions import Proposal
    from opus_magnum_sym.elements.board import Board, Hex
    from opus_magnum_sym.elements.components import Component


class ProgramState:
    """
    Stores plannded action for each component.
    """

    components: dict[int, Component]

    def __init__(self) -> None:
        self.components = {}

    # TODO: can that be None or ComponentType.NONE, if so add return type bool
    def add_component(self, comp: Component) -> None:
        self.components[comp.id] = comp

    def remove_component(self, component_id: int) -> None:
        self.components.pop(component_id, None)

    def get_component(self, component_id) -> Component | None:
        return self.components.get(component_id)

    def all_components(self) -> list[Component]:
        return list(self.components.values())


class Simulator:
    def previos_step(
        self,
        board: Board,
        program: ProgramState,
        tick: int,
    ) -> Proposal:
        """
        Compute effects without applying them.
        """
        affected: set[Hex] = set()
        updates: list[tuple[str, Any]] = []

        # one step = one step_action per component at index tick
        occupied_targets: set[tuple[int, int]] = set()

        # TODO: replace with real object intraction
        # for comp in program.all_components():
        #     if tick >= len(comp.program):
        #         continue

        #     step_action = comp.program[tick]
        #     if step_action.type is StepActionType.NONE:
        #         continue

        #     match step_action.type:
        #         case StepActionType.GRAB:
        #             affected.add(comp.pos)
        #             updates.append(("grab", comp.id))

        #         case StepActionType.RELEASE:
        #             affected.add(comp.pos)
        #             updates.append(("release", comp.id))

        #         case StepActionType.EXTEND:
        #             affected.add(comp.pos)
        #             updates.append(("arm_extention", comp.id))

        #         case StepActionType.RETRACT:
        #             affected.add(comp.pos)
        #             updates.append(("arm_retraction", comp.id))

        return Proposal(valid=True, updates=updates, affected=affected)

    def commit_step(
        self,
        board: Board,
        program: ProgramState,
        proposal: Proposal,
    ) -> None:
        if not proposal.valid:
            return

            # TODO: StepActionType dispatch/pesudo-dispatch
