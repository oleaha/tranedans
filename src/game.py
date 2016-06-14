from dice import throw_dice


rounds = {
    0: "Ones",
    1: "Twos",
    2: "Three",
    3: 'Fours',
    4: 'Fives',
    5: 'Sixes',
    6: "One pair",
    7: "Two pairs",
    8: "Three of a kind",
    9: "Four of a kind",
    10: "Small Straight",
    11: "Large Straight",
    12: "Full House",
    13: "Chance",
    14: "Yatzy"
}


class Game:
    def __init__(self, nr_of_players, player_names):
        self.nr_of_players = nr_of_players
        self.player_names = player_names

    def loop(self):
        for i in range(1):
            print('Round ', rounds[i])
            kept = []
            for _ in range(3):
                dice = throw_dice(5-len(kept))
                print('You threw: ', dice)
                to_keep = input('Keep dice numbers: ')
                if to_keep:
                    to_keep = map(int, to_keep.split(','))
                    for index in to_keep:
                        kept.append(dice[index])
                print('Kept: ', kept)
