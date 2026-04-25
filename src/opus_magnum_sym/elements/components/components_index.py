from opus_magnum_sym.elements.components import ComponentType, Enter, Exit
from opus_magnum_sym.elements.components.base_component import Component, ComponentAssignmentError
from opus_magnum_sym.elements.components.manipulator import Manipulator

_COMPONENT_MAP: dict[ComponentType, type[Component]] = {
    ComponentType.ARM: Manipulator,
    ComponentType.ENTRANCE: Enter,
    ComponentType.EXIT: Exit,
}


def get_component_type(comp_type: ComponentType) -> type[Component]:
    """
    Provides generator for `Component` subclass by `ComponentType` enum.

    Usage:
    get_component_type(ComponentType.ARM)(args*, **kwargs)
    """
    if (cls := _COMPONENT_MAP.get(comp_type)) is None:
        msg = "Unknown component."
        raise ComponentAssignmentError(msg, comp_type)
    return cls
