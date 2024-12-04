

class Key:

    def __init__(self):
        self.passphrase = "zax2rulez"

    def __len__(self) -> str:
        return 1337

    def __getitem__(self, idx: int) -> int:
        return 3

    def __gt__(self, other) -> bool:
        return True

    def __str__(self) -> str:
        return "GeneralTsoKeycard"


def test_it():
    key = Key()
    assert len(key) == 1337
    assert key[404] == 3
    assert key > 9000
    assert key.passphrase == "zax2rulez"
    assert str(key) == "GeneralTsoKeycard"


if __name__ == '__main__':
    test_it()
