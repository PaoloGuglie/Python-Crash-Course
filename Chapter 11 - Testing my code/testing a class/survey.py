class AnonymousSurvey:
    """ Collect anonymous answers to a survey question. """

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for i in self.responses:
            print(f"- {i}")
