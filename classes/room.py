class Room:
    def __init__(self, name, cost, theme):
        self.name = name
        self.cost = cost
        self.theme = theme
        self.guests = []
        self.songs = []

    def guest_list(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)

    def check_in_group(self, group):
        for guest in group:
            self.check_in_guest(group)

    def check_out_group(self, group):
        for guest in group:
            self.check_out_guest(group)

    def song_list(self):
        return len(self.songs)

    def add_song_in_the_list(self, song):
        self.songs.append(song)
