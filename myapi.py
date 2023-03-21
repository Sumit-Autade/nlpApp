import paralleldots

class Api:
    def __init__(self):
        paralleldots.set_api_key('6rf62NTMruNIYLU4KI0sJOYRePZgUqz1aXxKa4HFnmQ')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self,text):
        response = paralleldots.ner(text)
        return response

    def emotion_prediction(self,text):
        response = paralleldots.emotion(text)
        return response
