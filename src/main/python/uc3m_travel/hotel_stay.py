''' Class HotelStay (GE2.2) '''
from datetime import datetime
import hashlib
from uc3m_travel.attributes.attribute_room_type import AttributeRoomType
from uc3m_travel.attributes.attribute_localizer import AttributeLocalizer
from uc3m_travel.attributes.attribute_id_card import AttributeIdCard
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.storage.json_store import JsonStore
import json


class HotelStay():
    """Class for representing hotel stays"""
    def __init__(self,
                 idcard:str,
                 localizer:str,
                 numdays:int,
                 roomtype:str):
        """constructor for HotelStay objects"""
        self.__alg = "SHA-256"
        self.__type = AttributeRoomType(roomtype).value
        self.__idcard = AttributeIdCard(idcard).value
        self.__localizer = AttributeLocalizer(localizer).value
        justnow = datetime.utcnow()
        self.__arrival = datetime.timestamp(justnow)
        #timestamp is represented in seconds.miliseconds
        #to add the number of days we must express num_days in seconds
        self.__departure = self.__arrival + (numdays * 24 * 60 * 60)
        self.__room_key = hashlib.sha256(self.__signature_string().encode()).hexdigest()

    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + str(self.__arrival) + \
            ",departure:" + str(self.__departure) + "}"

    @property
    def id_card(self):
        """Property that represents the product_id of the patient"""
        return self.__idcard

    @id_card.setter
    def id_card(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.__arrival

    @property
    def room_key(self):
        """Returns the sha256 signature of the date"""
        return self.__room_key

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        """returns the value of the departure date"""
        self.__departure = value

    # @classmethod
    # def get_stay_from_room_key(cls, room_key: str):
    #     """Find and return a HotelStay instance from the room key"""
    #     # Load the check-in data
    #     file_store = JSON_FILES_PATH + "store_check_in.json"
    #     room_key_list = JsonStore(file_store, "room_key_check_in").load_json_store()
    #
    #     # Iterate through the room key list to find the matching stay
    #     found = False
    #     departure_date_timestamp = None
    #     arrival_date_timestamp = None
    #     for item in room_key_list:
    #         if room_key == item["_HotelStay__room_key"]:
    #             departure_date_timestamp = item["_HotelStay__departure"]
    #             arrival_date_timestamp = item["_HotelStay__arrival"]
    #             found = True
    #             break
    #
    #     # If the room key is not found, raise an exception
    #     if not found:
    #         raise HotelManagementException("Error: room key not found")
    #
    #     # Calculate the number of days of the stay
    #     # departure_date = datetime.utcfromtimestamp(departure_date_timestamp).date()
    #     # arrival_date = datetime.utcfromtimestamp(arrival_date_timestamp).date()
    #     # numdays = (departure_date - arrival_date).days
    #     numdays = (departure_date_timestamp - arrival_date_timestamp) / (24 * 60 * 60)
    #
    #     return cls(
    #         idcard=item["_HotelStay__idcard"],
    #         localizer=item["_HotelStay__localizer"],
    #         numdays=numdays,
    #         roomtype=item["_HotelStay__type"]
    #     )
    #
    # def check_out(self):
    #     """Perform the checkout process for the guest"""
    #     # Check if today is the departure day
    #     today = datetime.utcnow().date()
    #     if datetime.fromtimestamp(self.__departure).date() != today:
    #         raise HotelManagementException("Error: today is not the departure day")
    #
    #     # Load the check-out data
    #     file_store_checkout = JSON_FILES_PATH + "store_check_out.json"
    #     room_key_checkout_list = JsonStore(file_store_checkout, "room_key_check_out").load_json_store()
    #
    #     # Check if the guest is already checked out
    #     for checkout in room_key_checkout_list:
    #         if checkout["room_key"] == self.__room_key:
    #             raise HotelManagementException("Guest is already checked out")
    #
    #     # Add the checkout entry
    #     room_checkout = {"room_key": self.__room_key, "checkout_time": datetime.timestamp(datetime.utcnow())}
    #     room_key_checkout_list.append(room_checkout)
    #
    #     # Save the updated check-out data
    #     JsonStore(file_store_checkout, room_key_checkout_list).load_json_write()
    #
    #     return True