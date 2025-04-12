import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """ The setUp() method allows me to create an instance of the class once
    and the use it in each of my test methods. setUp() is run before the methods
     starting with test_ """

    def setUp(self):
        self.my_survey = AnonymousSurvey('')
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        for i in self.responses: self.my_survey.store_response(i)

        for i in self.responses:
            self.assertIn(i, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
