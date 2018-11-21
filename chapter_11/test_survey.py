import unittest
from chapter_11.survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language you first learned to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'French', 'Spanish', 'Mandarin']
    def test_store_single_resopnse(self):
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_three_responses(self):
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
