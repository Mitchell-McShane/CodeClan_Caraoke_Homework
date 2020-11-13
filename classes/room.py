class Room:
    def __init__(self, name, cost, theme):
        self.name = name
        self.cost = cost
        self.theme = theme
        self.guests = []
        self.songs = []

    def guest_list(self):
        return len(self.guests)