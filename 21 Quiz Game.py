# this is an exersice to practise collections

questions = ("Which is the closed planet to earth?", "Which is the farthest planet on earth?", "Which is the second planet from the sun?")
options =(("1","2","3","4"),
         ("1.1","2.1","3.1","4.1"),
         ("1.2","2.2","3.2","4.4"),
         ("1.3","2.3","3.3","4.3"))
answers =("C", "A", "B")
gueses = []
score = 0
question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess= input("enter option A, B, C, D").upper()
    gueses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print (f"The correct answer is {answers[question_num]}")

    question_num +=1
print(f"your final score is {score}")