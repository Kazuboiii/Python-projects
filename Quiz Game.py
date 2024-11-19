questions=("Who sang the title song for the latest Bond film, No Time to Die?",
           "Which flies a green, white, and orange (in that order) tricolor flag?",
           "What company makes the Xperia model of smartphone?",
           "Which city is home to the Brandenburg Gate",
           "Which of the following is NOT a fruit?")

options=(("A. Adele" ,"B. Sam Smith" ,"C. Billie Eilish"),
         ("A. Ireland","B. Ivory Cost","C. Italy "),
         ("A. Samsung", "B. Sony", "C. Nokia"),
         ("A.Vienna", "B.Zurich", "C.Berlin"),
         ("A.Rhubarb", "B.Tomatoes", "C.Avocados"))

answers=("C","A","B","C","A")
guesses=[]
score=0
question_num=0

for question in questions:
    print("---------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Enter (A,B,C) as one of your answer:").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT!!!")

    else:
        print("INCORRECT!!!")
        print(F"THE CORRECT ANSWER IS {answers[question_num]} ")
    question_num+=1

print("---------------------------------")
print("ANSWERS:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("GUESSES:", end=" ")
for guess in guesses:
    print(guess,end=" ")
print()
print("---------------------------------")

Total=score/ len(questions)*100
print("---------------------------------")
print("             RESULTS             ")
print("---------------------------------")
print()
print(f"-- YOUR FINAL SCORE IS {Total}% --")
print()
print("---------------------------------")