import json
import random

def flashcards():
    ask = input("Which one are you? Teacher or student? ")
    correct = 0
    streak = 0

    class Flashcard:
        def __init__(self, question, answer):
            self.question = question
            self.answer = answer

        def dic(self):
            return{self.question: self.answer}
        
        def text(self):
            return(f"{self.question}, {self.answer}")
        
    flashcards = []

    question = input("Clear history of questions/answers? ").lower()

    if question == "yes":
        with open("flashcards.json", "w") as file:
            json.dump({}, file, indent=4)
        print("Cleared")

    while True:

        if ask.lower() == "teacher":
            question = input("What's your question? ")
            answer = input("What's your answer? ")
            flash1 = Flashcard(question, answer)
            flashcards.append(flash1)

        elif ask.lower() == "student":
            with open("flashcards.json", "r") as file:
                data = json.load(file)
        
            for first, second in data.items():
                print(f"{first}: {second}")

            if answer == ask:
                correct = correct+1
                print(f"Good job! You're streak is now {streak}")


        question = input("Continue (Yes/No): ").lower()

        if question == "yes":
            continue
        
        x = [flashcard.dic() for flashcard in flashcards]

        with open("flashcards.json", "w") as file:
            json.dump(x, file, indent=4)

        if question == "no":
            break            




            
flashcards()    