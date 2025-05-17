import unittest
from city_functions import city_country  # Import the function from the correct module

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country('santiago', 'chile'), 'Santiago, Chile')
        self.assertEqual(city_country('tokyo', 'japan'), 'Tokyo, Japan')
        self.assertEqual(city_country('delhi', 'india'), 'Delhi, India')
        self.assertEqual(city_country('shanghai', 'china'), 'Shanghai, China')
        self.assertEqual(city_country('new york', 'usa'), 'New York, USA')
        self.assertEqual(city_country('los angeles', 'usa'), 'Los Angeles, USA')
        self.assertEqual(city_country('london', 'uk'), 'London, UK')
        self.assertEqual(city_country('paris', 'france'), 'Paris, France')
        self.assertEqual(city_country('berlin', 'germany'), 'Berlin, Germany')
        self.assertEqual(city_country('madrid', 'spain'), 'Madrid, Spain')
        self.assertEqual(city_country('rome', 'italy'), 'Rome, Italy')
        self.assertEqual(city_country('moscow', 'russia'), 'Moscow, Russia')
        self.assertEqual(city_country('toronto', 'canada'), 'Toronto, Canada')
        self.assertEqual(city_country('sydney', 'australia'), 'Sydney, Australia')
        self.assertEqual(city_country('rio de janeiro', 'brazil'), 'Rio De Janeiro, Brazil')

if __name__ == '__main__':
    unittest.main()