#one
'''获取名字函数'''
# from name_function import get_formatted_name

# print("Enter your name and enter 'q' to quit")
# while True:
#     first = input("\nPlease geve me your first name: ")
#     if first == 'q':
#         break
#     last = input("Please geve me your last name: ")
#     if first == 'q':
#         break

#     formatted_name = get_formatted_name(first,last)
#     print("\tFormatted name: " + formatted_name + '.')


'''测试函数正确性'''
# import unittest
# from name_function import get_formatted_name
# class NameTextCase(unittest.TestCase):
#     '''测试name_function.py'''
#     def test_first_last_name(self):
#         formatted_name = get_formatted_name('nuod','gevo')
#         self.assertEqual(formatted_name, 'Nuod Gevo')
#         #判断 formatted_name 与 Nuod Gevo 是否相等


#     def test_first_middle_last_name(self):
#         formatted_name = get_formatted_name(
#             'mkei', 'divu', 'gien')
#         self.assertEqual(formatted_name,'Mkei Gien Divu')

# unittest.main()

#two
# from survey import AnonymousSurvey

# question = "What language did you first learn to speak? "
# my_survey = AnonymousSurvey(question)

# my_survey.show_question()
# print("Enter 'q' to quit\n" )
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     my_survey.store_response(response)

# print("\nThank you! ")
# my_survey.show_results()

'''测试类AnonymousSurvey'''

#      ****方法一***
# import unittest
# from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase):
#     def test_store_single_response(self):
#         '''测试单个答案是否能存储好'''
#         question = "What language did you first learn to speak? "
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')

#         self.assertIn('English', my_survey.responses)

#     def test_store_three_response():
#         '''测试3个答案能否存储好'''
#         question = "What language did you first learn to speak? "
#         my_survey = AnonymousSurvey(question)
#         responses = ['English','python', 'java']
#         '''依次存储'''
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             '''依次检测是否在responses列表里'''
#             self.assertIn(response, my_survey.responses)

#       ***方法二***
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        """
        创建一个调查对象和一组答案，供给使用
        """
        question = "What language did you first learn to speak? "
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','python', 'java']

    def test_store_single_response(self):
        '''测试单个答案是否能存储好'''
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        '''测试3个答案能否存储好'''

        for response in self.responses:
            '''依次存储'''
            self.my_survey.store_response(response)
        for response in self.responses:
            '''依次检测是否在responses列表里'''
            self.assertIn(response, self.my_survey.responses)
unittest.main()