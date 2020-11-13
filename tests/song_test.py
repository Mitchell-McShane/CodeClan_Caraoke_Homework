import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Bakamitai", "Yakuza 0")

    def test_song_has_name(self):
        self.assertEqual("Bakamitai", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Yakuza 0", self.song.artist)
