from .attribute import Attribute
from uc3m_travel.hotel_management_exception import HotelManagementException

class AttributeNumDays(Attribute):
    def __init__(self, attr_value):
        """"Definition of attribute PhoneNumber init"""
        super().__init__(r"^\d+$", "Invalid num_days datatype")
        self.value = attr_value

    def _validate(self, attr_value):
        """Validates the number of days to ensure it's an integer within the range 1-10"""
        try:
            days = int(attr_value)
        except ValueError as ex:
            raise HotelManagementException("Invalid num_days datatype") from ex
        if days < 1 or days > 10:
            raise HotelManagementException("Numdays should be in the range 1-10")
        return attr_value
