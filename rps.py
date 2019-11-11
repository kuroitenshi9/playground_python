
import random 

def game():
    winner = {
        "r" : "s",
        "s" : "p",
        "p" : "r"
        }


    user = input("""Choose one figure using this code: 
    r - rock, 
    p - paper, 
    s - scissors:\n """)
    computer = random.choice(["k", "p", "n"])
    print("Computer chose", computer)
    if computer == user:
        return "draw"
    elif winner[computer] == user:
        return "you lose"
    else:
        return "you won"
while True:
    print("*" * 30)
    print("Welcome in paper-stone-scissors")
    print("*" * 30)
    answer = input("Do you wanna play? Y/N: ")
    if answer.upper() == "Y":
        print(game())
    else:
        print("You suck!")
        break



