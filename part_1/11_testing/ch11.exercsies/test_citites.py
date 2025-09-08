import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    """Test for 'city_functions.py'"""

    def test_city_info(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')
    
    def test_city_population(self):
        """Do cities like 'Caracas, Venezuela - 5000000' work?"""
        formatted_city = get_formatted_city('caracas', 'venezuela', 5000000)
        self.assertEqual(formatted_city, 'Caracas, Venezuela - Population 5000000')

if __name__ == '__main__':
    unittest.main()

"""
Failed test:

E
======================================================================
ERROR: test_city_info (__main__.CitiesTestCase.test_city_info)
Do cities like 'Santiago, Chile' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/path/to/file/part_1/11_testing/ch11.exercsies/test_citites.py", line 9, in test_city_info
    formatted_city = get_formatted_city('santiago', 'chile')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: get_formatted_city() missing 1 required positional argument: 'population'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)


,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


Success when third argument is optional:

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK


,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


Success when tested with optional argument:


..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

"""