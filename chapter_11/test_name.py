import unittest
from chapter_11.name_function import get_formated_name

class NameTestCase(unittest.TestCase):
    def test_first(self):
        formated_name = get_formated_name('sam', 'witaker')
        self.assertEqual(formated_name, 'Sam Witaker')
    
    def test_first_second_middle(self):
        formated_name = get_formated_name('sam','jones' 'witaker')
        self.assertEqual(formated_name, 'Sam Jones Witaker')

unittest.main()