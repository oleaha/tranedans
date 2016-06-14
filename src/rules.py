def get_score_ones_to_sixes(dice, value):
	return dice.count(value) * value

def get_equal_dice_score(dice, value, number_of_equal_dice):
	if dice.count(value) >= number_of_equal_dice:
		return value * number_of_equal_dice
	return 0

def get_small_straight_score(dice):
	if all(die in dice for die in [1,2,3,4,5]):
		return 15
	return 0

def get_large_straight_score(dice):
	if all(die in dice for die in [2,3,4,5,6]):
		return 20
	return 0

def get_house_score(dice, value1, value2):
	if all(count in [2,3] for count in [dice.count(value1), dice.count(value2)]):
		return dice.count(value1)*value1 + dice.count(value2)*value2
	return 0

def get_chance_score(dice):
	return sum(dice)

def get_yatzy_score(dice):
	if all(dice[0] == die for die in dice):
		return 50
	return 0

def get_pair_score(dice):
	for i in range(6, -1, -1):
		score = get_equal_dice_score(dice, i, 2)
		if score:
			return score
	return 0

def get_three_of_a_kind_score(dice):
	for i in range(6, -1, -1):
		score = get_equal_dice_score(dice, i, 3)
		if score:
			return score
	return 0

def get_max_house_score(dice):
	return 1

score_round_mapping = [get_score_ones_to_sixes, get_score_ones_to_sixes, get_score_ones_to_sixes,
get_score_ones_to_sixes, get_score_ones_to_sixes, get_score_ones_to_sixes,
get_pair_score, get_three_of_a_kind_score, get_small_straight_score,
get_large_straight_score, get_max_house_score, get_chance_score, get_yatzy_score]
