class AnonymousSurvey():
    '''收集匿名调查问卷答案'''

    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)
        pass

    def store_response(self,response):
        self.responses.append(response)
        pass

    def show_results(self):
        print("Survey results")
        for response in self.responses:
            print('- ' + response)
        pass

