"""Class for RoomKey"""
from .attribute import Attribute


class AttributeRoomkey(Attribute):  # pylint: disable=too-few-public-methods
    """AttributeRoomkey definition"""

    def __init__(self, attr_value):
        """"Definition of attribute Roomkey init"""
        super().__init__(r'^[a-fA-F0-9]{64}$', "Invalid room key format")
        self.value = attr_value

    def _validate(self, attr_value):
        """Call attribute superclass to validate"""
        return super()._validate(attr_value)
