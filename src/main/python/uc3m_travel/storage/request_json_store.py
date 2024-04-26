"""
This module implements the json stores for the reservation function.
"""

from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.hotel_management_exception import HotelManagementException


class ReservationJsonStore(JsonStore):
    """ReservationJsonStore singleton class"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        """If instance doesn't exist, create instance"""
        if cls._instance is None:
            cls._instance = super(ReservationJsonStore, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """If it hasn't been initialized, initalize"""
        if not hasattr(self, '_init'):
            self._file_name = JSON_FILES_PATH + "store_reservation.json"
            super().__init__()
            self._init = True

    def add_item(self, item):
        """If reservation item doesn't exist, add reservation item"""
        reservation_found = self.find_item(
            item['localizer'], key="_HotelReservation__localizer")
        if reservation_found:
            raise HotelManagementException("Reservation already exists")
        super().add_item(item)

