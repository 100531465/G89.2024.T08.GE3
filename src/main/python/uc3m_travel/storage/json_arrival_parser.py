import json
from .json_parser import JsonParser
class ArrivalJsonParser(JsonParser):
    def __init__(self, file_path):
        super().__init__(file_path)
