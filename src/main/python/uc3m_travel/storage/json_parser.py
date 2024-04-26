import json

class JsonParser:
    def __init__(self, file_path):
        self.valid_keys = []
        self.content = {}
        self.error_message = None
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.content = json.load(file)
                self.valid_keys = list(self.content.keys())
        except Exception as e:
            self.error_message = str(e)
