from collections import Counter
from itertools import combinations
from random import randrange


class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        '''
        simulate number of matches
        equal to self.matches
        '''

        for _ in range(self.matches):
            action1 = next(player1)
            action2 = next(player2)
            if action1 == 'cooperate':
                if action2 == 'cooperate':
                    self.registry[str(player1)] += 2
                    self.registry[str(player2)] += 2
                elif action2 == 'cheat':
                    self.registry[str(player1)] -= 1
                    self.registry[str(player2)] += 3
            elif action1 == 'cheat':
                if action2 == 'cooperate':
                    self.registry[str(player1)] += 3
                    self.registry[str(player2)] -= 1
                elif action2 == 'cheat':
                    pass # nothing happening

            player1.other_choices.append(action2)
            player2.other_choices.append(action1)
        player1.reset()
        player2.reset()

    def top3(self):
        '''
        print top three
        '''
        print('\n'.join(f'{n} {v}' for n, v in self.registry.most_common(3)))


class Player():
    '''
    Base class
    '''

    def __init__(self, player_id=None):
        self.id = player_id
        self.other_choices = []

    def __str__(self) -> str:
        return f'{self.id}' if self.id else ''

    def __iter__(self):
        return self

    def reset(self):
        self.other_choices.clear()


class Cheater(Player):
    '''
    Always cheats
    '''

    def __str__(self) -> str:
        return 'cheater' + super().__str__()

    def __next__(self) -> str:
        return 'cheat'


class Cooperator(Player):
    '''
    Always cooperates
    '''

    def __str__(self) -> str:
        return 'cooperator' + super().__str__()

    def __next__(self) -> str:
        return 'cooperate'


class Copycat(Player):
    '''
    Starts with cooperating, but then just
    repeats whatever the other guy is doing
    '''

    def __str__(self) -> str:
        return 'copycat' + super().__str__()
    
    def __next__(self) -> str:
        if self.other_choices:
            return self.other_choices[-1]
        else:
            return 'cooperate'


class Grudger(Player):
    '''
    Starts by always cooperating, but switches to
    Cheater forever if another guy cheats even once
    '''

    def __str__(self) -> str:
        return 'grudger' + super().__str__()

    def __next__(self) -> str:
        if 'cheat' in self.other_choices:
            return 'cheat'
        else:
            return 'cooperate'


class Detective(Player):
    '''
    First four times goes with [Cooperate, Cheat, Cooperate, Cooperate],
    and if during these four turns another guy cheats even once - switches
    into a Copycat. Otherwise, switches into Cheater himself
    '''

    def __str__(self) -> str:
        return 'detective' + super().__str__()

    def __next__(self) -> str:
        nchoices = len(self.other_choices)
        if nchoices == 1:
            return 'cheat'
        elif nchoices < 4:
            return 'cooperate'
        elif 'cheat' in self.other_choices[:4]:
            return self.other_choices[-1]
        else:
            return 'cheat'


class Random(Player):
    '''
    Either cooperates or cheats arbitrarily
    '''

    def __str__(self) -> str:
        return 'random' + super().__str__()

    def __next__(self) -> str:
        if randrange(2):
            return 'cooperate'
        else:
            return 'cheat'


class Copykitten(Player):
    def __str__(self) -> str:
        return 'copykitten' + super().__str__()

    def __next__(self) -> str:
        if len(self.other_choices) > 2 and \
        all(x == 'cheat' for x in self.other_choices[-2:]):
            return 'cheat'
        else:
            return 'cooperate'


class ThinkTwiser(Player):
    def __str__(self) -> str:
        return 'thinktwiser' + super().__str__()

    def __next__(self) -> str:
        nmatches = len(self.other_choices)
        if nmatches == 1:
            return 'cooperate'
        elif nmatches == 2 and self.other_choices[-1] == 'cooperate':
            return 'cooperate'
        elif nmatches > 2 and self.other_choices[-1] == 'cooperate':
            return 'cooperate'
        else:
            return 'cheat'


def simulation():
    print(f"{'Simulation of Game':#^40}")
    game = Game()
    players = [Cheater(), Cooperator(), Copycat(), Grudger(), Detective()]
    for player1, player2 in combinations(players, r=2):
        game.play(player1, player2)
        print(f'{player1} VS {player2}')
    print('\nTop 3:')
    game.top3()
    print('#' * 40)
    print()

    print(f"{'Simulation of Game with Random':#^40}")
    game = Game(matches=5)
    players = [
        Cheater(), Cooperator(), Copycat(), Grudger(), Detective(),
        Random(),
    ]
    for player1, player2 in combinations(players, r=2):
        game.play(player1, player2)
        print(f'{player1} VS {player2}')
    print('\nTop 3:')
    game.top3()
    print('#' * 40)
    print()

    print(f"{'Simulation of Game with Bonus':#^40}")
    game = Game()
    players = [
        Cheater(), Cooperator(), Copycat(), Grudger(), Detective(),
        Copykitten(), ThinkTwiser()
    ]
    for player1, player2 in combinations(players, r=2):
        game.play(player1, player2)
        print(f'{player1} VS {player2}')
    print('\nTop 3:')
    game.top3()
    print('#' * 40)



if __name__ == '__main__':
    simulation()
    
