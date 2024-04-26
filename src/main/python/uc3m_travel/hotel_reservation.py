import hashlib
from datetime import datetime
from uc3m_travel.attributes.attribute_phone_number import AttributePhoneNumber
from uc3m_travel.attributes.attribute_credit_card import AttributeCreditCard
from uc3m_travel.attributes.attribute_room_type import AttributeRoomType
from uc3m_travel.attributes.attribute_arrival_date import AttributeArrivalDate
from uc3m_travel.attributes.attribute_id_card import AttributeIdCard
from uc3m_travel.attributes.attribute_name_surname import AttributeNameSurname
from uc3m_travel.attributes.attribute_num_days import AttributeNumDays

class HotelReservation:
    """Class for representing hotel reservations"""
    # Singleton instance
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self,
                 id_card:str,
                 credit_card_number:str,
                 name_surname:str,
                 phone_number:str,
                 room_type:str,
                 arrival:str,
                 num_days:int):
        """constructor of reservation objects"""
        # Instance attributes
        self.__credit_card_number = AttributeCreditCard(credit_card_number).value
        self.__id_card = AttributeIdCard(id_card).value
        self.__arrival = AttributeArrivalDate(arrival).value
        self.__reservation_date = datetime.timestamp(datetime.utcnow())
        self.__name_surname = AttributeNameSurname(name_surname).value
        self.__phone_number = AttributePhoneNumber(phone_number).value
        self.__room_type = AttributeRoomType(room_type).value
        self.__num_days = AttributeNumDays(num_days).value
        self.__localizer = hashlib.md5(str(self).encode()).hexdigest()

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        json_info = {
            "id_card": self.__id_card,
            "name_surname": self.__name_surname,
            "credit_card": self.__credit_card_number,
            "phone_number:": self.__phone_number,
            "reservation_date": self.__reservation_date,
            "arrival_date": self.__arrival,
            "num_days": self.__num_days,
            "room_type": self.__room_type,
        }
        return "HotelReservation:" + str(json_info)

    @property
    def credit_card(self):
        """property for getting and setting the credit_card number"""
        return self.__credit_card_number

    @credit_card.setter
    def credit_card(self, value):
        self.__credit_card_number = value

    @property
    def id_card(self):
        """property for getting and setting the id_card"""
        return self.__id_card

    @id_card.setter
    def id_card(self, value):
        self.__id_card = value

    @property
    def localizer(self):
        """Returns the md5 signature"""
        return self.__localizer
