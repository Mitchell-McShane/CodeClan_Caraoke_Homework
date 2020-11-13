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

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.assertEqual(2, self.room.guest_list())

    def test_check_out_guest(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_in_guest(self.guest_2)
        self.room.check_out_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_list())

    def test_song_in_the_list(self):
        self.assertEqual(0, self.room.song_list())

    def test_add_song_in_the_list(self):
        song_1 = Song("Bakamitai", "Yakuza 0")
        self.room.add_song_in_the_list(song_1)
        self.assertEqual(1, self.room.song_list())