import unittest
from chapter_11.city_function import get_city_country

class CitiesName(unittest.TestCase):
    def test_city_country(self):
        formated_name = get_city_country('Dublin', 'Ireland')
        self.assertEqual(formated_name, 'Dublin Ireland')

    def test_city_population(self):
        formated_name = get_city_country('Dublin', 'Ireland', '6000')
        self.assertEqual(formated_name, 'Dublin Ireland 50000')

unittest.main()