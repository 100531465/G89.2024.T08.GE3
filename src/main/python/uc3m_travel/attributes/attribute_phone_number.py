"""Class for PhoneNumber"""
from .attribute import Attribute


class AttributePhoneNumber(Attribute):  # pylint: disable=too-few-public-methods
    """AttributePhoneNumber definition"""

    def __init__(self, attr_value):
        """"Definition of attribute PhoneNumber init"""
        super().__init__(r"^(\+)[0-9]{9}", "Invalid phone number format")
        self.value = attr_value

    def _validate(self, attr_value):  # pylint: disable=useless-parent-delegation
        return super()._validate(attr_value)
