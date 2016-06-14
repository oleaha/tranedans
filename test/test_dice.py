from src.dice import throw_dice


def test_throw_dice_returns_list_of_dice_values():
    assert len(throw_dice(6)) == 6
