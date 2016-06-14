from dice import throw_dice


class Game():
    def loop(self):
        for i in range(10):
            print(throw_dice())
