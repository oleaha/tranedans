from src.rules import *

def test_upper_section_score():
	dice_values = [1,4,5,5,6,6]

	assert get_score_ones_to_sixes(dice_values, 5) == 10
	assert get_score_ones_to_sixes(dice_values, 3) == 0

def test_pair_score():
	assert get_equal_dice_score([1,3,3,4,4,6], 4, 2) == 8
	assert get_equal_dice_score([1,2,3,4], 1, 2) == 0

def test_three_of_a_kind():
	assert get_equal_dice_score([1,2,1,1,1], 1, 3) == 3
	assert get_equal_dice_score([1,2,1],1, 3) == 0

def test_four_of_a_kind():
	assert get_equal_dice_score([1,2,1,1,1], 1, 4) == 4
	assert get_equal_dice_score([1,2,1],1, 4) == 0

def test_small_straight():
	assert get_small_straight_score([1,2,6,3,4,5]) == 15
	assert get_small_straight_score([1]) == 0

def test_large_straight_score():
	assert get_large_straight_score([4,2,3,5,6]) == 20
	assert get_large_straight_score([0]) == 0

def test_house_score():
	assert get_house_score([2,2,1,1,1,5,5],1,5) == 13
	assert get_house_score([1,1],1,2) == 0

def test_chance_score():
	assert get_chance_score([2,2,1]) == 5

def test_yatzy():
	assert get_yatzy_score([5,5,5,5,5]) == 50
	assert get_yatzy_score([1,2]) == 0

def test_best_pair_score():
	assert get_pair_score([2,2,5,5]) == 10

def test_three_of_a_kind_score():
	assert get_three_of_a_kind_score([2,2,5,5,6,6,6]) == 18