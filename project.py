#import pyautogui
import random
from quiz import quiz_questions

def check(ques, ans):
    global score, wrong_attempt, correct_attempt
    if ans.lower() == "true" or ans.lower() == "false":
        if ans.lower() is quiz_questions.get(ques).get("answer"):
            print("Correct answer")
            score += 10
            correct_attempt += 1
        else:
            print("Wrong answer")
            score -= 5
            wrong_attempt +=1
    else:
        print("not a valid input")

#header

head = "QUIZ"
print(head.center(70, "#"))


# Introduction to the program

print("""This is a quiz program
You will get 5 true/false questions to answer
Each right question increase the score by 10 point while a negative marking of -5 point will be implimented for every wrong question

NOTE: only true/false are accepted for a answer""")



asked_ques = []
score = 0
correct_attempt = 0
wrong_attempt = 0
   


for i in range(5):
    ques = random.choice(list(quiz_questions.keys()))
    if ques not in asked_ques:
        question = quiz_questions.get(ques, -1).get("question", None)
        print(question)
        answer = input("answer: ")
        check(ques, answer)        
        asked_ques.append(ques)



#Final resul

print(f"Right attempts: {correct_attempt}")
print(f"Your score is {score}")
