"""Class for RoomType"""
from .attribute import Attribute

class AttributeRoomType(Attribute): # pylint: disable=too-few-public-methods
    """AttributeRoomType definition"""
    def __init__(self, attr_value):
        """"Definition of attribute Roomtype init"""
        super().__init__(r"(SINGLE|DOUBLE|SUITE)", "Invalid roomtype value")
        self.value = attr_value

    def _validate(self, attr_value):
        """Call attribute superclass to validate"""
        return super()._validate(attr_value)
