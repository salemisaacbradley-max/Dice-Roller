import unittest
from roller import Die, Cup
from creatures import Warrior, Enemy

class WarriorTrails(unittest.TestCase):
    def test_slash(self):
        bandit = Enemy("Bandit Garica", 2, 0)
        ralph = Warrior("Ralph the Cowardly")
        ralph.slash(bandit)
        self.assertLess(bandit.health, bandit.max_hp)

    def test_crush(self):
        gobbo = Enemy("Goblin Skree the Ironsided", 1, 99)
        kenneth = Warrior("Kenneth the Stupid")
        kenneth.crush(gobbo)
        self.assertEqual(gobbo.health, gobbo.max_hp)

if __name__ == '__main__':
    unittest.main()   