import random
import time


def again():
    answer = input("Would you like to play again? Y/N")
    if answer == "Y":
        main()
    else:
        quit()


def main():
    playername = input("What is your name?: ")
    playerstats = User(playername, random.randint(0, 5), 75, 125,
                       )
    print("Welcome")
    print(playername)
    print("Please select difficulty")
    answer = input("\n1. easy \n2. medium \n3. hard")
    if answer == "1":
        easy = Opponent("Easy Opponent", random.randint(0, 5), 50, 100,
                        )
        match(easy, playerstats)

    if answer == "2":
        medium = Opponent("Medium Opponent", random.randint(0, 5), 75, 125,
                          )
        match(medium, playerstats)

    if answer == "3":
        hard = Opponent("Hard Opponent", random.randint(0, 5), 100, 150,
                        )
        match(hard, playerstats)


class User:
    def __init__(self, name, attack, health, stamina):
        self.name = name
        self.attack = attack
        self.health = health
        self.stamina = stamina
        self.stamdec = random.randint(0, 5)

    def fight(self, commence):
        commence.health -= self.attack
        commence.stamina -= self.stamdec
        if commence.stamina < 0:
            print("Out of stamina!")
            commence.stamina += 30
            commence.attack = 0
        else:
            commence.health -= self.attack


class Opponent:
    def __init__(self, name, attack, health, stamina):
        self.name = name
        self.attack = attack
        self.health = health
        self.stamina = stamina
        self.stamdec = random.randint(0, 5)

    def fight(self, commence):
        commence.health -= self.attack
        commence.stamina -= self.stamdec
        if commence.stamina < 0:
            print("Out of stamina!")
            commence.stamina += 30
            commence.attack = 0
        else:
            commence.health -= self.attack


def match(opponent, playerstats):
    life = "Life"
    stamina = "Stamina"
    stats = "Stats:"
    roundCount = 1
    while (playerstats.health > 0) and (opponent.health > 0):
        print("{0:<5} {2:>5} {1:>25} {2:>5}".format(playerstats.name, opponent.name, stats))
        print('{2:>12} {0:>6} {2:>20} {1:>6}'.format(playerstats.health, opponent.health, life))
        print('{2:>15} {0:>4} {2:>22} {1:>4}'.format(playerstats.stamina, opponent.stamina, stamina))
        print("\nThe enemy attacks:")
        for i in range(random.randint(0, 4)):
            opponent.fight(playerstats)
            print('The enemy hits you for {0}'.format(opponent.attack))

        time.sleep(1)
        print("\n========ROUND {0} END=========".format(roundCount))

        print("{0:<5} {2:>5} {1:>25} {2:>5}".format(playerstats.name, opponent.name, stats))
        print('{2:>12} {0:>6} {2:>20} {1:>6}'.format(playerstats.health, opponent.health, life))
        print('{2:>15} {0:>4} {2:>22} {1:>4}'.format(playerstats.stamina, opponent.stamina, stamina))
        print("\nYou Attack:")
        for x in range(random.randint(0, 4)):
            playerstats.fight(opponent)
            print('You attack the enemy for {0}'.format(playerstats.attack))

        time.sleep(1)
        print("\n========ROUND {0} END=========".format(roundCount))
        roundCount += 1
    if playerstats.health > opponent.health:
        print("Player {0} wins!".format(playerstats.name))
        again()
    else:
        print("Player {0} wins!".format(opponent.name))
        again()


main()
