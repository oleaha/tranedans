from src.dice import throw_dice


def test_dice_roll_should_return_1to6():
    assert 1 <= throw_dice() <= 6
