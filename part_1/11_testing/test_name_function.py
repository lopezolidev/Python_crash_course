import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Humberto Fernandez Moran' work?"""
        formatted_name = get_formatted_name('humberto', 'moran', 'fernandez')
        self.assertEqual(formatted_name, 'Humberto Fernandez Moran')

if __name__ == '__main__':
    unittest.main()
"""
.     ← ran and passed 1 test
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""
# failling case, different output and positional argument errors:
"""
F
======================================================================
FAIL: test_first_last_name (__main__.NamesTestCase.test_first_last_name)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/path/to/file/part_1/11_testing/test_name_function.py", line 10, in test_first_last_name
    self.assertEqual(formatted_name, 'Lea Seydux')
AssertionError: 'Janis Joplin' != 'Lea Seydux'
- Janis Joplin
+ Lea Seydux


----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)

...............................................................................

E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase.test_first_last_name)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/path/to/file/part_1/11_testing/test_name_function.py", line 9, in test_first_last_name
    formatted_name = get_formatted_name('janis', 'joplin')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)


...............................................................................


#when second function added
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
"""

