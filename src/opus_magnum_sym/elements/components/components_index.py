from opus_magnum_sym.elements.components import ComponentType, Enter, Exit
from opus_magnum_sym.elements.components.base_component import Component, ComponentAssignmentError
from opus_magnum_sym.elements.components.manipulator import Manipulator

_COMPONENT_MAP: dict[ComponentType, type[Component]] = {
    ComponentType.ARM: Manipulator,
    ComponentType.ENTRANCE: Enter,
    ComponentType.EXIT: Exit,
}


def create_component_instance(comp_type: ComponentType) -> type[Component]:
    if (cls := _COMPONENT_MAP.get(comp_type)) is None:
        msg = "Unknown component."
        raise ComponentAssignmentError(msg, comp_type)
    return cls
