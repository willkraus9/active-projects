def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1
    for key in questions:
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess = input("Answer:").upper()
        guesses.append(guess)
        correct_guesses+=check_answer(questions.get(key),guess)
        question_number +=1
    display_score(correct_guesses,guesses)
#---
def check_answer(answer,guess):
    if answer == guess:
        print ("CORRECT!")
        return 1 
    else:
        print("INCORRECT!")
        return 0
#---
def display_score(correct_guesses, guesses):
    print ("RESULTS")
    print("Answers: ",end=" ")
    for i in questions: 
        print(questions.get(i),end=" ")
    print()
    print("Guesses: ",end=" ")
    for i in guesses: 
        print(i,end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("FINAL SCORE: "+str(score)+"%")
    
#---
def play_again():
    response = input("Do you want to play again?[Y/N] ").upper
    if response == 'Y':
        return True
    else:
        return False
#---
questions = {#dictionary
    "Who created Python?: ":"A",
    "What year was Python created?: ":"B",
    "Python is attributed to which comedy group?: ":"C",
    "What shape is the earth?: ":"A"
}

options = [["A: Guido van Rossum","B: Elon Musk", "C: Bill Gates","D: Mark Zuckerberg"],
           ["A: 1989","B: 1991","C: 2000","D: 2016"],
           ["A: Lonely Island", "B: Smosh","C: Monty Python","D: SNL"],
           ["A: Sphere","B: Disk","C: Cube","D: Toroid"]]
new_game()
while play_again():
    new_game()
print("Bye!")