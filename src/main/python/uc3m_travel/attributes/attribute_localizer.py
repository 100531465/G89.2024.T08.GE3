from .attribute import Attribute

class AttributeLocalizer(Attribute):
    def __init__(self, attr_value):
        """"Definition of attribute Localizer init"""
        super().__init__(r'^[a-fA-F0-9]{32}$', "Invalid localizer")
        self.value = attr_value

    def _validate(self, attr_value):
        return super()._validate(attr_value)
