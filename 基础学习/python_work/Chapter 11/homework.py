#11-1 and11-2
'''测试city_hw.py 模块'''
# import unittest
# from city_hw import city_country_test

# class NameTestCase(unittest.TestCase):
#     def test_city_country(self):
#         message = city_country_test('shanghai', 'china')
#         self.assertEqual(message,'Shanghai, China')

#     def test_city_country_population(self):
#         message = city_country_test('shanghai', 'china', 10000)
#         self.assertEqual(message,'Shanghai, China - Population 10000')
#         pass
# unittest.main()

#11-3

import unittest
from employee_hw import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.new_person = Employee('joe','dig',500)

    def test_give_default_raise(self):
        self.new_person.give_raise()
        # self.assertEqual(self.new_person.full_name, 'Joe Dig')
        self.assertEqual(self.new_person.money, 5500)

unittest.main()