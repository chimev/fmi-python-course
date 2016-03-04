import unittest
from bmi_calc import body_mass_index, shape_of


class TestBMI(unittest.TestCase):

    def test_body_mass_index_positive_negative(self):
        self.assertEqual(body_mass_index(0, 1), 0.0)
        self.assertEqual(body_mass_index(1, 1), 1.0)
        self.assertEqual(body_mass_index(-1, 1), -1.0)
        self.assertEqual(body_mass_index(1, -1), 1.0)
        self.assertEqual(body_mass_index(-1, -1), -1.0)

    def test_body_mass_index_int_float(self):
        self.assertEqual(body_mass_index(10, 1), 10)
        self.assertEqual(body_mass_index(10, 0.9), 12.3)
        self.assertEqual(body_mass_index(9.9, 1), 9.9)
        self.assertEqual(body_mass_index(9.9, 0.9), 12.2)
        self.assertEqual(body_mass_index(-9.9, -0.9), -12.2)

    def test_shape_of_severe_malnutrition(self):
        self.assertEqual(shape_of(-999999, -1.5), 'тежко недохранване')
        self.assertEqual(shape_of(15, 1), 'тежко недохранване')

    def test_shape_of_average_malnutrition(self):
        self.assertEqual(shape_of(15.1, 1), 'средно недохранване')
        self.assertEqual(shape_of(16, 1), 'средно недохранване')

    def test_shape_of_mild_malnutrition(self):
        self.assertEqual(shape_of(16.1, 1), 'леко недохранване')
        self.assertEqual(shape_of(18.5, 1), 'леко недохранване')

    def test_shape_of_normal_weight(self):
        self.assertEqual(shape_of(18.6, 1), 'нормално тегло')
        self.assertEqual(shape_of(25, 1), 'нормално тегло')

    def test_shape_of_overweight(self):
        self.assertEqual(shape_of(25.1, 1), 'наднормено тегло')
        self.assertEqual(shape_of(30, 1), 'наднормено тегло')
        self.assertEqual(shape_of(76, 1.7), 'наднормено тегло')

    def test_shape_of_first_obesity_degree(self):
        self.assertEqual(shape_of(30.1, 1), 'затлъстяване I степен')
        self.assertEqual(shape_of(35, 1), 'затлъстяване I степен')

    def test_shape_of_second_obesity_degree(self):
        self.assertEqual(shape_of(35.1, 1), 'затлъстяване II степен')
        self.assertEqual(shape_of(40, 1), 'затлъстяване II степен')

    def test_shape_of_third_obesity_degree(self):
        self.assertEqual(shape_of(40.1, 1), 'затлъстяване III степен')
        self.assertEqual(shape_of(999999, 1.5), 'затлъстяване III степен')


if __name__ == '__main__':
    unittest.main(verbosity=2)
