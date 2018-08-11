import unittest

from auburn_football import Coach

class test_coach(unittest.TestCase):

    def setUp(self):
        self.coach1 = Coach('Gus', 'Malzahn', 52, 'Head Coach', 7000000, 7)
        self.coach2 = Coach('Chip', 'Lindsey', 41, 'Offensive Coordinator', 700000, 2)

    def tearDown(self):
        pass

    #Test to make sure the salary is a positive number
    def test_apply_bonus(self):
        self.coach1.apply_bonus()
        self.coach2.apply_bonus()

        self.assertEqual(self.coach1.pay, 7490000)
        self.assertEqual(self.coach2.pay, 714000)

        self.coach1.pay = 7500000
        self.coach2.pay = 650000

        self.coach1.apply_bonus()
        self.coach2.apply_bonus()

        self.assertEqual(self.coach1.pay, 8025000)
        self.assertEqual(self.coach2.pay, 663000)


if __name__ == '__main__':
    unittest.main()
