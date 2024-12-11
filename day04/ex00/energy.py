import unittest
from itertools import zip_longest


def fix_wiring(cables, sockets, plugs):
    cables = filter(lambda x: isinstance(x, str), cables)
    sockets = filter(lambda x: isinstance(x, str), sockets)
    plugs = filter(lambda x: isinstance(x, str), plugs)
    cables_and_sockets = zip(cables, sockets)
    gen = map(lambda x: (x, next(plugs, None)), cables_and_sockets)

    for (c, s), p in gen:
        if p:
            yield f'plug {c} into {s} using {p}'
        else:
            yield f'weld {c} to {s} without plug'


def fix_wiring_one_line(cbls, scts, plgs):
    return map(
        lambda x: f'plug {x[0][0]} into {x[0][1]} using {x[1]}' \
                if x[1] else f'weld {x[0][0]} to {x[0][1]} without plug',
        zip_longest(
            zip(
                filter(lambda x: isinstance(x, str), cbls),
                filter(lambda x: isinstance(x, str), scts),
            ),
            filter(lambda x: isinstance(x, str), plgs),
        )
    )


class TestFixWiring(unittest.TestCase):
    
    def setUp(self):
        self.sockets1 = ['socket1', 'socket2', 'socket3', 'socket4']
        self.cables1 = ['cable1', 'cable2', 'cable3', 'cable4']
        self.plugs1 = ['plug1', 'plug2', 'plug3']

        self.sockets2 = [1, 'socket1', 'socket2', 'socket3', 'socket4']
        self.cables2 = ['cable2', 'cable1', False]
        self.plugs2 = ['plugZ', None, 'plugY', 'plugX']

        self.expected1 = (
            x for x in [
                'plug cable1 into socket1 using plug1',
                'plug cable2 into socket2 using plug2',
                'plug cable3 into socket3 using plug3',
                'weld cable4 to socket4 without plug',
            ]
        )

        self.expected2 = (
            x for x in [
                'plug cable2 into socket1 using plugZ',
                'plug cable1 into socket2 using plugY',
            ]
        )


    def test_fix_wiring_1(self):
        gen = fix_wiring(self.cables1, self.sockets1, self.plugs1)
        expected = (x for x in self.expected1)
        for got, want in zip(gen, expected):
            self.assertEqual(got, want)
        self.assertEqual(next(gen, -100500), -100500)
        self.assertEqual(next(expected, -100500), -100500)


    def test_fix_wiring_2(self):
        gen = fix_wiring(self.cables2, self.sockets2, self.plugs2)
        expected = (x for x in self.expected2)
        for got, want in zip(gen, expected):
            self.assertEqual(got, want)
        self.assertEqual(next(gen, -100500), -100500)
        self.assertEqual(next(expected, -100500), -100500)


    def test_fix_wiring_one_line_1(self):
        gen = fix_wiring_one_line(self.cables1, self.sockets1, self.plugs1)
        expected = (x for x in self.expected1)
        for got, want in zip(gen, expected):
            self.assertEqual(got, want)
        self.assertEqual(next(gen, -100500), -100500)
        self.assertEqual(next(expected, -100500), -100500)


    def test_fix_wiring_one_line_2(self):
        gen = fix_wiring(self.cables2, self.sockets2, self.plugs2)
        expected = (x for x in self.expected2)
        for got, want in zip(gen, expected):
            self.assertEqual(got, want)
        self.assertEqual(next(gen, -100500), -100500)
        self.assertEqual(next(expected, -100500), -100500)


if __name__ == '__main__':
    unittest.main()

