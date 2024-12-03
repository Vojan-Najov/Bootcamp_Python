
def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    return {"gold_ingots": purse.get("gold_ingots", 0) + 1}


def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    gold_ingots = purse.get("gold_ingots", 0) - 1
    return {} if gold_ingots < 1 else {"gold_ingots": gold_ingots}


def empty(purse: dict[str, int]) -> dict[str, int]:
    return {}


def split_booty(*args: dict[str, int]) -> tuple[dict[str, int], ...]:
    purges = [empty({}), empty({}), empty({})]
    i: int = 0
    for arg in args:
        for _ in range(arg.get('gold_ingots', 0)):
            purges[i] = add_ingot(purges[i])
            i = (i + 1) % 3

    return tuple(purges)


def test_it():

    res = split_booty({"gold_ingots":3}, {"gold_ingots":2}, {"apples":10})
    assert res == ({"gold_ingots": 2}, {"gold_ingots": 2}, {"gold_ingots": 1})

    res = split_booty({"gold_ingots":3}, {"gold_ingots":1}, {"apples":10})
    assert res == ({"gold_ingots": 2}, {"gold_ingots": 1}, {"gold_ingots": 1})

    res = split_booty({"gold_ingots":3}, {"gold_ingots":0}, {"apples":10})
    assert res == ({"gold_ingots": 1}, {"gold_ingots": 1}, {"gold_ingots": 1})

    res = split_booty({"gold_ingots":1}, {"gold_ingots":1}, {"apples":10})
    assert res == ({"gold_ingots": 1}, {"gold_ingots": 1}, {})

    res = split_booty({"gold_ingots":1}, {"apples":10})
    assert res == ({"gold_ingots": 1}, {}, {})

    res = split_booty({"gold_ingots": 0})
    assert res == ({}, {}, {})

    res = split_booty({"apples":10}, {"apples":10}, {"apples":10})
    assert res == ({}, {}, {})


if __name__ == '__main__':
    test_it()
