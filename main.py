import random

run = True
while run:
    comp = random.randint(1, 3)

    print("1 : Rock")
    print("2 : Paper")
    print("3 : Scissor")
    print("4 : Quit")
    print("\n")

    user = int(input("Enter Your Choice : "))

    if user == 1:
        print("Your Choice : Rock")
        if comp == 1:
            print("Comp Choice : Rock")
            print("Its A Tie !!!\n")

        elif comp == 2:
            print("Comp Choice : Paper")
            print("Alas !!! Lost\n")

        elif comp == 3:
            print("Comp Choice : Scissor")
            print("Congo !!! You Won\n")
        print("Play Again !")


    elif user == 2:
        print("Your Choice : Paper")
        if comp == 1:
            print("Comp Choice : Rock")
            print("Congo !!! You Won\n")

        elif comp == 2:
            print("Comp Choice : Paper")
            print("Its A Tie !!!\n")

        elif comp == 3:
            print("Comp Choice : Scissor")
            print("Alas !!! Lost\n")
        print("Play Again !")


    elif user == 3:
        print("Your Choice : Scissor")
        if comp == 1:
            print("Comp Choice : Rock")
            print("Alas !!! Lost\n")

        elif comp == 2:
            print("Comp Choice : Paper")
            print("Congo !!! You Won\n")

        elif comp == 3:
            print("Comp Choice : Scissor")
            print("Its A Tie !!!\n")
        print("Play Again !")


    elif user == 4:
        run = False
        print("Thanks For Playing\n")

    else:
        print("Invalid Number")
