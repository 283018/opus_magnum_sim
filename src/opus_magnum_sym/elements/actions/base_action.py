from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from opus_magnum_sym.elements.components.base_component import ComponentType


class ActionAssignmentError(Exception):
    def __init__(
        self,
        message,
        component_type: ComponentType,
        component_id: int,
    ) -> None:
        self.message = message
        super().__init__(self.message)
        self.component_type = component_type
        self.component_id = component_id
