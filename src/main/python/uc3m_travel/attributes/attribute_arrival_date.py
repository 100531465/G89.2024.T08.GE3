"""Class for ArrivalDate"""
from .attribute import Attribute


class AttributeArrivalDate(Attribute): # pylint: disable=too-few-public-methods
    """AttributeArrivalDate definition"""
    def __init__(self, attr_value):
        """"Definition of attribute ArrivalDate init"""
        super().__init__(r"^(([0-2]\d|-3[0-1])\/(0\d|1[0-2])\/\d\d\d\d)$", "Invalid date format")
        self.value = attr_value

    def _validate(self, attr_value):
        """Call attribute superclass to validate"""
        return super()._validate(attr_value)
