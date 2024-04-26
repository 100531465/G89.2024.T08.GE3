import unittest
from uc3m_travel.hotel_reservation import HotelReservation

class TestHotelReservationSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        reservation1 = HotelReservation(
            id_card="12345678Z",
            credit_card_number="1234567890123456",
            name_surname="Jose Lopez",
            phone_number="123456789",
            room_type="single",
            arrival="20/01/2024",
            num_days=3
        )
        reservation2 = HotelReservation(
            id_card="87654321X",
            credit_card_number="9876543210987654",
            name_surname="Lopez Jose",
            phone_number="987654321",
            room_type="double",
            arrival="25/01/2024",
            num_days=5
        )
        self.assertIs(reservation1, reservation2, "Reservation instances should be the same")