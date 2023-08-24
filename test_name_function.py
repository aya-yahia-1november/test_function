import unittest
from name_function import  get_format_name

class NameTestCase(unittest.TestCase):
    def test_frist_last_name(self):
        format_name=get_format_name('aya','yahia')
        self.assertEquals(format_name,'Aya Yahia')

    def test_frist_last_medlle_names(self):
        formatted_name=get_format_name("aya","helmy","yahia")
        self.assertEquals(formatted_name,'Aya Yahia Helmy')
#unittest.main()