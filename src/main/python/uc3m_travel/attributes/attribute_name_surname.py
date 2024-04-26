from .attribute import Attribute

class AttributeNameSurname(Attribute):
    def __init__(self, attr_value):
        """"Definition of attribute Localizer init"""
        super().__init__(r"^(?=^.{10,50}$)([a-zA-Z]+(\s[a-zA-Z]+)+)$", "Invalid name format")
        self.value = attr_value

    def _validate(self, attr_value):
        return super()._validate(attr_value)
