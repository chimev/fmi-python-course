import unittest
from bmi_calc import shape_of


class TestBMI(unittest.TestCase):
    def test_shape_of(self):

        self.assertEqual(shape_of(10, 1), 'тежко недохранване')
        self.assertEqual(shape_of(10, 0.9), 'тежко недохранване')
        self.assertEqual(shape_of(9.9, 1), 'тежко недохранване')
        self.assertEqual(shape_of(9.9, 0.9), 'тежко недохранване')
        self.assertEqual(shape_of(-9.9, -0.9), 'тежко недохранване')

        self.assertEqual(shape_of(15, 1), 'тежко недохранване')
        self.assertEqual(shape_of(15.1, 1), 'средно недохранване')
        self.assertEqual(shape_of(16, 1), 'средно недохранване')
        self.assertEqual(shape_of(16.1, 1), 'леко недохранване')
        self.assertEqual(shape_of(18.5, 1), 'леко недохранване')
        self.assertEqual(shape_of(18.6, 1), 'нормално тегло')
        self.assertEqual(shape_of(25, 1), 'нормално тегло')
        self.assertEqual(shape_of(25.1, 1), 'наднормено тегло')
        self.assertEqual(shape_of(30, 1), 'наднормено тегло')
        self.assertEqual(shape_of(30.1, 1), 'затлъстяване I степен')
        self.assertEqual(shape_of(35, 1), 'затлъстяване I степен')
        self.assertEqual(shape_of(35.1, 1), 'затлъстяване II степен')
        self.assertEqual(shape_of(40, 1), 'затлъстяване II степен')
        self.assertEqual(shape_of(40.1, 1), 'затлъстяване III степен')

        self.assertEqual(shape_of(76, 1.7), 'наднормено тегло')
        self.assertEqual(shape_of(999999, 1), 'затлъстяване III степен')

if __name__ == '__main__':
    unittest.main()
