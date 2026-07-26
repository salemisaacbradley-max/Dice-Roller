import unittest
from roller import Die, Cup

class RollerTest(unittest.TestCase):
    def test_advantage(self):
        blue = Die(6, 0)
        red = Die(6, 0)
        purple = [blue, red]
        chalice = Cup(purple)
        chalice.roll_all()
        self.assertGreaterEqual(chalice.advantage(), blue.value)
        self.assertGreaterEqual(chalice.advantage(), red.value)

    def test_disadvantage(self):
        blue = Die(6, 0)
        red = Die(6, 0)
        purple = [blue, red]
        chalice = Cup(purple)
        chalice.roll_all()
        self.assertLessEqual(chalice.advantage(disadvantage=True), blue.value)
        self.assertLessEqual(chalice.advantage(disadvantage=True), red.value)

if __name__ == '__main__':
    unittest.main()   