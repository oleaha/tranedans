from dice import throw_dice


class Game:
    def __init__(self, nr_of_players, player_names):
        self.nr_of_players = nr_of_players
        self.player_names = player_names
        print(self.player_names)
        print(self.nr_of_players)

    def loop(self):
        for i in range(10):
            print(throw_dice(5))
