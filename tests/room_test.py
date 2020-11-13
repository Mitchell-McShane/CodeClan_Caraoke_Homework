import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Utahime", 100, "Karaoke Bar")
        self.guest_1 = Guest("Akira Nishikiyama", 200)
        self.guest_2 = Guest("Goro Majima", 300)
    
    def test_room_has_name(self):
        self.assertEqual("Utahime", self.room.name)

    def test_room_has_cost(self):
        self.assertEqual(100, self.room.cost)

    def test_room_has_theme(self):
        self.assertEqual("Karaoke Bar", self.room.theme)

    def test_room_has_guest_list(self):
        self.assertEqual(0, self.room.guest_list())