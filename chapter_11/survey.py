class AnonymousSurvey():
    def __init__(self, questions):
        self.questions = questions
        self.responses = []

    def show_questions(self):
        print(self.questions)

    def store_responses(self, new_responses):
        self.responses.append(new_responses)

    def show_responses(self):
        for response in self.responses:
            print('- ' + response)
