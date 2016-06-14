from src.dice import throw_dice


def test_throw_dice_returns_list_of_dice_values():
    values = throw_dice(5)
    assert len(values) == 5
    for value in values:
        assert 1 <= value <= 6
