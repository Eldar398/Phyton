class Home:

    def __init__(self, address):
        self.address = address


class Room(Home):

    def __init__(self, address, room_name):
        self.address = address
        self.room_name = room_name
        self.light_status = False

    def light_on(self):
        self.light_status = True

    def light_off(self):
        self.light_status = False