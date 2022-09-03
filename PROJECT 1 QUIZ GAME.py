# PROJECT 2 QUIZ GAME

print("WELCOME TO THE COMPUTER QUIZ!")
print("IF YOU WANT TO PLAY TYPE 'YES' IF NOT TYPE 'NO'")

def comp_game(game):
    if game == "no" or game == "NO":
        print("Its Ok ")
    elif game == "yes" or game == "YES":
        print("lets start the game")
game= input("Please enter your decision: ")
comp_game(game)
i=0
while i<1:
    if game == "no" or game == "NO":
       break
    i+=1
    print("QUESTION NUMBER 1 - WHAT IS THE CAPITAL OF INDIA ?")
    a1=input("enter your answer: ")
    if a1 == "delhi" or a1 == "DELHI":    
        a1=1
        print("Correct Answer")
    else:    
        a1=0
        print("wrong answer")

    print("QUESTION NUMBER 2 - WHAT IS THE CAPITAL OF CANADA ?" )
    a2=input("enter your answer: ")
    if a2 == "ottawa" or a2 == "OTTAWA":    
        a2=1
        print("Correct Answer")
    else:
        a2=0
        print("wrong answer")

    print("QUESTION NUMBER 3 - WHICH ANIMAL IS KNOWN AS THE SHIP OF THE DESERT ?")
    a3=input("enter your answer: ")
    if a3 == "camel" or a3 == "CAMEL":
        a3=1
        print("Correct answer")
    else:
        a3=0
        print("wrong answer")

    print("QUESTION NUMBER 4 - HOW MANY COLOURS IN THE RAINBOW ?")
    a4=int(input("enter your answer: "))
    if a4 == 7:
        a4=1
        print("correct answer")
    else:
        a4=0
        print("wrong answer")

    print("QUESTION NUMBER 5 - HOW MANY BONES DO HUMANS HAVE IN AN EAR?")
    a5=int(input("enter your answer: "))
    if a5 == 3:
        a5=1
        print("correct answer")
    else:
        a5=0
        print("wrong answer")
    add= a1+a2+a3+a4+a5
    print(f"YOUR TOTAL SCORE IS {add} OUT OF 5")

    if add == 0 or add == 1:
        print("POOR PERFORMANCE")
    elif add == 2 or add == 3:
        print("AVERAGE PERFORMANCE")
    elif add == 4:
        print("GOOD PERFORMANCE")
    else: 
        print("TOP TIER PERFORMANCE")

print("SEE YOU NEXT TIME")









