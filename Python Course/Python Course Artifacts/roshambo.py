import random
import time
#choosing option
roshambo = ["rock", "paper","scissors"]
computer = random.choice(roshambo)
player = None
while player not in roshambo: #choose only among options in roshambo
    player = input("Rock, Paper, or Scissors?: ").lower()
#timing setup
lead_up = ["Rock...","Paper...","Scissors...","Shoot!"]
for i in range(0,4):
    print(lead_up[i])
    time.sleep(1)
#displaying score
def ScoreDisplay():
    print("Player: "+player)
    print("Computer: "+computer)
if player == computer:
    ScoreDisplay()
    print("Tie!")
elif player == "rock":
    if computer == "paper":
        ScoreDisplay()
        print("You Lose!")
    if computer == "scissors":
        ScoreDisplay()
        print("You Win!")
elif player == "paper":
    if computer == "scissors":
        ScoreDisplay()
        print("You Lose!")
    if computer == "rock":
        ScoreDisplay()
        print("You Win!")
elif player == "scissors":
    if computer == "rock":
        ScoreDisplay()
        print("You Lose!")
    if computer == "paper":
        ScoreDisplay()
        print("You Win!")