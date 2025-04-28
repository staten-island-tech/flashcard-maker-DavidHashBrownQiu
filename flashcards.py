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

    clear_question = input("Clear history of questions/answers? ").lower()

    if clear_question == "yes":
        with open("flashcards.json", "w") as file:
            json.dump({}, file, indent=4)
        print("Cleared")

    while True:

        if ask.lower() == "teacher":
            question = input("What's your question? ")
            answer = input("What's your answer? ")
            flash1 = Flashcard(question, answer)
            flashcards.append(flash1)

        if ask.lower() == "student":
            with open("flashcards.json", "r") as file:
                datas = json.load(file)   

            if datas:
                first, second = random.choice(list(datas.items()))
                print(f"Question: {first}")
                _second = input("What's your answer? ").lower()

                if _second == second.lower():
                    correct = correct+1
                    streak = streak+1
                    print(f"Good job! You have a streak of {streak} and a score of {correct}")
                    if streak > 1:
                        correct = correct+streak-1
                        print(f"You gained extra points for your streak! Your score is now {correct}")
                elif _second != second.lower():
                    streak = 0
                    correct = correct-1
                    print(f"You lost your streak of {streak}. Your score is now {correct}")

        question = input("Continue (Yes/No): ").lower()

        if question == "yes":
            continue
        
        flashcards_dict = {}
        for flashcard in flashcards:
            flashcards_dict.update(flashcard.dic())

        with open("flashcards.json", "w") as file:
            json.dump(flashcards_dict, file, indent=4)

        if question == "no":
            print("Done!!")
            break            
 
flashcards()    