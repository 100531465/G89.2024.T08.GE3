"""Class for IdCard"""
from uc3m_travel.hotel_management_exception import HotelManagementException
from .attribute import Attribute


class AttributeIdCard(Attribute):  # pylint: disable=too-few-public-methods
    "AttributeIdCard definition"

    def __init__(self, attr_value):
        """Definition of attribute IdCard init"""
        super().__init__(r'^[0-9]{8}[A-Z]{1}$', "Invalid IdCard format")
        self.value = attr_value

    def _validate(self, attr_value):
        """Override the validation method to add additional checks"""
        super()._validate(attr_value)
        self._validate_dni(attr_value)
        return attr_value

    def _validate_dni(self, attr_value):
        """Validate the DNI letter"""
        letter_mapping = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
                          "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
                          "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
                          "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}
        dni_number = int(attr_value[0:8])
        remainder_key = str(dni_number % 23)
        if attr_value[8] != letter_mapping[remainder_key]:
            raise HotelManagementException("Invalid IdCard letter")
