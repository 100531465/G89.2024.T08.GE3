"""Class for json storage"""
import json
from uc3m_travel.hotel_management_exception import HotelManagementException


class JsonStore:  # pylint: disable=too-few-public-methods
    """JsonStore class definition"""

    def __init__(self, file_store, list_name):
        self._file_store = file_store
        self._list_name = list_name

    def load_json_store(self):  # pylint: disable=inconsistent-return-statements
        """Method to load json for reading"""
        try:
            with open(self._file_store, "r", encoding="utf-8", newline="") as file:
                return json.load(file)
        except FileNotFoundError as exception:
            if self._list_name in ("data_list", "room_key_list", "room_key_check_out"):
                return []
            if self._list_name == "input_list":
                raise HotelManagementException("Error: file input not found") from exception
            if self._list_name == "store_list":
                raise HotelManagementException("Error: store reservation not found") from exception
            if self._list_name == "room_key_check_in":
                raise HotelManagementException("Error: store checkin not found") from exception
        except json.JSONDecodeError as exception:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from exception

    def load_json_write(self):
        """Method to load json for writing"""
        try:
            with open(self._file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(self._list_name, file, indent=2)
        except FileNotFoundError as exception:
            raise HotelManagementException("Wrong file  or file path") from exception

    def _set_file_store(self, file_store):
        """Sets file store"""
        self._file_store = file_store

    def _set_list_name(self, list_name):
        """Sets list name"""
        self._list_name = list_name
