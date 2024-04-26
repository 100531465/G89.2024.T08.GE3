"""Class for CreditCard"""
from uc3m_travel.hotel_management_exception import HotelManagementException
from .attribute import Attribute


class AttributeCreditCard(Attribute): # pylint: disable=too-few-public-methods
    """AttributeCreditCard definition"""
    def __init__(self, attr_value):
        """"Definition of attribute CreditcCard init"""
        super().__init__(r"^[0-9]{16}", "Invalid credit card format")
        self.value = attr_value

    def _validate(self, attr_value):
        """Call attribute superclass to validate"""
        super()._validate(attr_value)

        # Validate using Luhn algorithm
        def digits_of(credit_card_string):
            return [int(digit) for digit in str(credit_card_string)]

        digits = digits_of(attr_value)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for digit in even_digits:
            checksum += sum(digits_of(digit * 2))
        if not checksum % 10 == 0:
            raise HotelManagementException("Invalid credit card number (not luhn)")

        return attr_value
