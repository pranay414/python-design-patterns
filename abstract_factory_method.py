"""
Implements abstract factory design pattern.
"""
class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))

class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'

class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t--- Frog World ---'

    def make_character(self):
        return Frog(self.name)

    def make_obstacle(self):
        return Bug()

class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        return('{} the Wizard battles against {} and {}!'.format(self, obstacle, obstacle.action()))

def Ork():
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'

def WizardWorld():
    def __init__(self, name):
        print(self)
        self.name = name

    def __str__(self):
        return '\n\n\t---Wizard  World---'

    def make_character(self, name):
        return Wizard(self.name)

    def make_obstacle(self):
        return Ork()

class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_game(name):
    try:
        age = input('Welcome {}. How old are you?'.format(name))
        age = int(age)
    except ValueError as ve:
        print('Age {} is invalid, please try again!'.format(age))
        return (False, age)
    return (True, age)

def main():
    name = input('Hello, what\'s your name?')
    valid_input = False
    while not valid_input:
        valid_input, age = validate_game(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()

if __name__ == '__main__':
    main()