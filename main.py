import random

def gamewin(comp, you):

    # If two values are equal declare tie
    if comp == you:
        return  None
    # When computer choose s
    elif comp == "s":
        if you == "r":
            return  True
        if you == "p":
            return False
    # when computer choose r
    elif comp == "r":
        if you == "p":
            return  True
        if you == "s":
            return False
    # When computer choose p
    elif comp == "p":
        if you == "s":
            return  True
        if you == "r":
            return False

print("Comp Turn: Rock(r) Paper(p) Scissor(s) ?")
randomNo = random.randint(1,3)
if randomNo == 1:
    comp = "r"
elif randomNo == 2:
    comp = "p"
elif randomNo == 3:
    comp = "s"
print("Computer Choosing......\nComputer ne chun liya")
you  = input("YOur Turn: Rock(r) Paper(p) Scissor(s) ?\n")

print("computer choose  =", comp, "\nnd Your's =", you)
print(f"{comp} V/S {you}")

if gamewin(comp, you) == None  :
    print("Ooops! It's a tie, Both comp and you choose same")
elif gamewin(comp, you):
    print("Ayooo! You Won,",you, "beats", comp)
else :
    print(f"Awww, You lost, {comp} beats {you}, \nNo worries Try again\nBest of Luck for you next Game")