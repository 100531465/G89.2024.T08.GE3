import unittest
from uc3m_travel.access_manager import AccessManager

class TestHotelManagerSingleton(unittest.TestCase):
    def test_singleton_manager(self):
        manager1 = AccessManager()
        manager2 = AccessManager()
        manager3 = AccessManager()

        self.assertEqual(manager1, manager2)
        self.assertEqual(manager2, manager3)
        self.assertEqual(manager3, manager1)