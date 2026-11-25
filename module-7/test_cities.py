# Test cases for the city_country function
import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city_country = city_country('Santiago', 'Chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
    