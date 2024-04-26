"""Class for Localizer"""
from .attribute import Attribute


class AttributeLocalizer(Attribute):  # pylint: disable=too-few-public-methods
    """AttributeLocalizer definition"""

    def __init__(self, attr_value):
        """"Definition of attribute Localizer init"""
        super().__init__(r'^[a-fA-F0-9]{32}$', "Invalid localizer")
        self.value = attr_value

    def _validate(self, attr_value):
        """Call attribute superclass to validate"""
        return super()._validate(attr_value)
