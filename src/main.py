from game import Game


def prompt_initial_config():
    print("Welcome to Yetzee")
    nr_of_players = int(input("Enter the number of players: "))
    player_names = []
    for i in range(nr_of_players):
        player_names.append(input("Enter name of player " + str((i + 1)) + ": "))
    return nr_of_players, player_names


if __name__ == '__main__':
    nr_of_players, player_names = prompt_initial_config()

    game = Game(nr_of_players=nr_of_players, player_names=player_names)
    game.loop()

