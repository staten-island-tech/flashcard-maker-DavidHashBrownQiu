import json

ask = input("Which one are you? Teacher or student? ")

def flashcards():
    correct = 0

    class Flashcard:
        def __init__(self, question, answer):
            self.question = question
            self.answer = answer

        def dic(self):
            return{self.question: self.answer}

    if ask.lower() == "teacher":
        question = input("What's your question? ")
        answer = input("What's your answer?")
        flashcards = []
        flash1 = Flashcard(question, answer)
        print(flash1.dic())
            
            

    

"""with open("flashcards.json", "w") as file:
    json.dump()"""