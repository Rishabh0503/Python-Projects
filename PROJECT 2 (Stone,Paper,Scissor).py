#STONE-PAPER-SCISSOR GAME 
import random

def gamewin(computer,you):
# IF TWO VALUES ARE EQUAL, DECLARE TIE
    if computer == you:
        return None
# CHECK FOR ALL THE POSSIBILITIES WHEN COMPUTER CHOSE "STONE"
    elif computer == "stone" :
        if you == "paper":
            return True
        elif you == "scissor":
            return False
        elif you != "stone":
            return "invalid"
        elif you != "paper":
            return "invalid"
        elif you != "scissor":
            return "invalid"
# CHECK FOR ALL THE POSSIBILITIES WHEN COMPUTER CHOSE "SCISSOR"
    elif computer == "scissor":
        if you == "paper":
            return False
        elif you == "stone":
            return True
        elif you != "stone":
                return "invalid"
        elif you != "paper":
            return "invalid"
        elif you != "scissor":
            return "invalid"
# CHECK FOR ALL THE POSSIBLILITIES WHEN COMPUTER CHOSE "PAPER"
    elif computer == "paper":
        if you == "stone":
            return False
        elif you == "scissor":
            return True
        elif you != "stone":
                return "invalid"
        elif you != "paper":
            return "invalid"
        elif you != "scissor":
            return "invalid"

print("computer's turn: stone(s) paper(p) scissor(sc)?")
random_num = random.randint(1,3)
if random_num == 1:
    computer = "stone"
elif random_num == 2:
    computer = "paper"
elif random_num == 3:
    computer = "scissor"

you = input("your turn: stone(s) paper(p) scissor(sc)?")

game = gamewin(computer,you)

print(f"Computer chose {computer}")
print(f"You chose {you}")

if game == None:
    print("The game is tie")
elif game == True:
    print("You won!")
elif game == False:
    print("You lost!")
elif game == "invalid":
    print(f"{you} is not in the options please re-enter your choice")

