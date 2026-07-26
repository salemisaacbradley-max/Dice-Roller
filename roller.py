#d20, d100, d12, d10, d8, d6, d4, d2 and d* should be a class
import random
class Die:
    def __init__ (self, sides:int, modifier:int):
        if sides < 2:
            raise ValueError ("A die must have at least two sides")
        elif type(sides) != int:
            raise ValueError("Number of sides must be an integer")
        elif type(modifier) != int:
            raise ValueError("Modifier must be an Integer")
        self.sides = sides
        self.mod = modifier
        self.value = None

    def roll(self):
        self.value = random.randint(1 + self.mod, self.sides + self.mod)
        return self.value

    def __repr__(self):
        return f"D{self.sides} rolled {self.value}"

class Cup:
    def __init__(self, dice_set: list[Die]):
        self.dice = dice_set

    def roll_all(self):
        return [die.roll() for die in self.dice]

    def add_die(self, die) -> None:
        self.dice.append(die)

    def remove_die(self, die: Die) -> None:
        if len(self.dice) <= 0:
            raise ValueError("No dice to remove")
        else:
            print(f"Removing {die}")
            if die not in self.dice:
                print(f"No die matching {die} was found")
            else:
                self.dice.remove(die)
                print(f"Removed {die}")

    def get_total(self):
        if any(die.value is None for die in self.dice):
            self.roll_all()
        return sum(die.value for die in self.dice)

    def advantage(self, disadvantage=False):
        #intended to be used for choosing between two equal dice
        if any(die.value is None for die in self.dice):
            self.roll_all()
        if disadvantage == True:
            return min(die.value for die in self.dice)
        return max(die.value for die in self.dice)
    