
def squeaker(func):
    def decorated(*args):
        print("SQUEAK")
        return func(*args)

    return decorated


@squeaker
def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    return {"gold_ingots": purse.get("gold_ingots", 0) + 1}


@squeaker
def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    gold_ingots = purse.get("gold_ingots", 0) - 1
    return {} if gold_ingots < 1 else {"gold_ingots": gold_ingots}


@squeaker
def empty(purse: dict[str, int]) -> dict[str, int]:
    return {}


def test_it():
    purses: [dict[str, int]] = [
        {},
        {'tmp': 2},
        {'tmp': 2, 'gold_ingots': 33},
        {'tmp': 2, 'gold_ingots': -33},
        {'tmp': 2, 'gold_ingots': 0},
        {'gold_ingots': 33},
        {'gold_ingots': 1},
        {'gold_ingots': -1},
        {'gold_ingots': 2, 'tmp': 3, 'qwe': 4},
    ]
    
    for purse in purses:
        copy_purse = {k: v for k, v in purse.items()}
        new_purse = empty(purse)
        assert new_purse == {}
        assert purse == copy_purse
        assert new_purse is not purse

    for purse in purses:
        copy_purse = {k: v for k, v in purse.items()}
        new_purse = get_ingot(purse)
        assert len(new_purse) in (0, 1)
        assert purse == copy_purse
        assert new_purse is not purse
        if 'gold_ingots' not in purse or purse['gold_ingots'] < 2:
            assert len(new_purse) == 0
        else:
            assert new_purse['gold_ingots'] == purse['gold_ingots'] - 1

    for purse in purses:
        copy_purse = {k: v for k, v in purse.items()}
        new_purse = add_ingot(purse)
        assert len(new_purse) in (0, 1)
        assert purse == copy_purse
        assert new_purse is not purse
        assert new_purse['gold_ingots'] == purse.get('gold_ingots', 0) + 1

    assert add_ingot(get_ingot(add_ingot(empty(purse)))) == {"gold_ingots": 1}


if __name__ == '__main__':
    test_it()

