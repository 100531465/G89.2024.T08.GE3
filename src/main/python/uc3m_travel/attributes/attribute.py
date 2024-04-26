"""Class for attributes"""
import re
from uc3m_travel.hotel_management_exception import HotelManagementException


class Attribute: # pylint: disable=too-few-public-methods
    """Attribute class definition"""

    def __init__(self, validation_pattern, error_message):
        """Constructor for Attribute class"""
        self._validation_pattern = validation_pattern
        self._error_message = error_message
        self._attr_value = ""

    def _validate(self, attr_value):
        """Attribute validation definition"""
        myregex = re.compile(self._validation_pattern)
        regex_matches = myregex.fullmatch(attr_value)
        if not regex_matches:
            raise HotelManagementException(self._error_message)
        return attr_value

    @property
    def value(self):
        """Returns attribute value"""
        return self._attr_value

    @value.setter
    def value(self, attr_value):
        """Validates and sets the attribute value"""
        self._attr_value = self._validate(attr_value)
