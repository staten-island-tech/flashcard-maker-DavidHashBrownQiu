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
        
        def text(self):
            (f"{self.question}, {self.answer}")
        

    while True:
        if ask.lower() == "teacher":
            question = input("What's your question? ")
            answer = input("What's your answer? ")
            flashcards = ()
            flash1 = Flashcard(question, answer)
            flash2 = flash1.text()
            flash1.append(flashcards)

            question = input("Continue (Yes/No): ").lower()

            if question == "yes":
                continue

            flash2 = [flash1.dic() for flashcard in flashcards]
            print(f"here are all the questions: {flash2}")
            
            with open("flashcards.json", "w") as file:
                json.dump(flash2, file, indent=4)

            if question == "no":
                break


            
flashcards()    

