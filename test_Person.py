import unittest

from auburn_football import Person


class Coach(unittest.TestCase):

    def setUp(self):
        self.person1 = Person('Gus', 'Malzahn', 52)
        self.person2 = Person('Jarrett', 'Stidham', 24)

    def tearDown(self):
        pass

    def test_full_name_func(self):

        self.person1.full_name_func()
        self.person2.full_name_func()

        self.assertEqual(self.person1.full_name_func(), 'Gus Malzahn')
        self.assertEqual(self.person2.full_name_func(), 'Jarrett Stidham')


if __name__ == '__main__':
    unittest.main()
