from .attribute import Attribute

class AttributeRoomkey(Attribute):
    def __init__(self, attr_value):
        """"Definition of attribute Roomkey init"""
        super().__init__(r'^[a-fA-F0-9]{64}$', "Invalid room key format")
        self.value = attr_value

    def _validate(self, attr_value):
        return super()._validate(attr_value)
