from enum import Enum
from roller import *
class EncounterType(Enum):
    ENEMY = "enemy"
    SHOPKEEP = "shopkeep"
    EVENT = "event"
    ELITE = "elite"
    BOSS = "boss"

class Class(Enum):
    WARRIOR = "warrior"
    MAGUS = "magus"
    MERCHANT = "merchant"

class Encounter:
    def __init__(self, creature_type: EncounterType):
        self.type = creature_type
        self.hp = None
        self.mana = None
        self.strength = None
        self.magic = None
        self.speed = None
        self.cores = None

class Player:
    def __init__(self, char_class: Class):
        self.char_class = char_class
        self.mana = None
        self.intellect = None
        self.con = 0
        self.strength = None
        self.magic = None
        self.speed = None
        self.cores = None
        self.level = 1
        self.max_hp = self.con * self.level + 5
        self.health = None
        self.inventory = None

    def level_up(self):
        pass

class Enemy(Encounter):
    def __init__(self, name:str, level:int, ac_mod:int):
        super().__init__(self)
        self.name = name 
        self.level = level
        self.max_hp = 10 + self.level
        self.health = self.max_hp
        self.mana = 2 * self.level
        self.strength = 1.5 * self.level
        self.magic = self.level//2
        self.enemy20 = Die(20, 0) 
        self.enemy20.roll()
        self.speed = self.enemy20.value
        self.cores = None
        self.xp = self.level
        self.ac = ac_mod + self.level//4

    def die(self, player:Player):
        print(f"{self.name} has been killed {player.name}")
        player.inventory.append(self.cores)
        player.xp += self.xp

class Warrior(Player):
    def __init__(self, name):
        super().__init__(char_class=Warrior)
        self.name = name
        self.strength = 3
        self.warrior20 = Die(20, self.strength)
        self.warrior_att_die = Die(12, self.strength)
        self.char_class = Class.WARRIOR
        self.con = 3
        self.level = 1
        self.intellect = 1
        self.inventory = []
        self.xp = 0

    def slash(self, target):
        self.warrior20.roll()
        if self.warrior20.value >= target.ac:
            self.warrior_att_die.roll()
            target.health -= self.warrior_att_die.value
            print(f"{self.name} dealt {self.warrior_att_die.value} damage to {target.name}")
            if target.health <= 0:
                target.die(self)
        else:
            print(f"{self.name} couldn't cut through {target.name}'s armor")

    def crush(self, target):
        self.warrior20.roll()
        if self.warrior20.value >= target.ac:
            self.warrior_att_die.roll()
            target.health -= self.warrior_att_die.value
            print(f"{self.name} dealt {self.warrior_att_die.value} damage to {target.name}")
            if target.health <= 0:
                target.die(self)
        else:
            print(f"{self.name} couldn't crush {target.name}'s armor")


        