from random import randrange
import unittest

def turrets_generator():
    while True:
        upper_bound = 100
        neuroticism = randrange(0, upper_bound + 1)
        upper_bound -= neuroticism
        openness = randrange(0, upper_bound + 1)
        upper_bound -= openness
        conscientiousness = randrange(0, upper_bound + 1)
        upper_bound -= conscientiousness
        extraversion = randrange(0, upper_bound + 1)
        agreeableness = upper_bound - extraversion
        yield type(
            'Turret',
            (),
            {
                'neuroticism': neuroticism,
                'openness': openness,
                'conscientiousness': conscientiousness,
                'extraversion': extraversion,
                'agreeableness': agreeableness,
                'shoot': lambda self: 'Shooting',
                'search': lambda self: 'Searching',
                'talk': lambda self: 'Talking',
            }
        )()


class TestTurret(unittest.TestCase):

    def test_turrets_generator(self):
        do = randrange(100, 1000)
        print(f'num of the tests: {do}')
        for turret in turrets_generator():
            self.assertEqual(turret.shoot(), 'Shooting')
            self.assertEqual(turret.search(), 'Searching')
            self.assertEqual(turret.talk(), 'Talking')

            self.assertIn(turret.neuroticism, range(0, 101)),
            self.assertIn(turret.openness, range(0, 101)),
            self.assertIn(turret.conscientiousness, range(0, 101)),
            self.assertIn(turret.extraversion, range(0, 101)),
            self.assertIn(turret.agreeableness, range(0, 101)),
            
            self.assertEqual(
                sum(
                    (turret.neuroticism, 
                    turret.openness,
                    turret.conscientiousness,
                    turret.extraversion,
                    turret.agreeableness)
                ),
                100
            )
            do -= 1
            if not do:
                break


if __name__ == '__main__':
    unittest.main()

