import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def test_store_single_response(self):
        my_survey = AnonymousSurvey('')
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        my_survey = AnonymousSurvey('')
        responses = ['English', 'Spanish', 'Mandarin']
        for i in responses: my_survey.store_response(i)

        for i in responses:
            self.assertIn(i, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
