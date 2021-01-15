import random

run = True
cScore = 0
uScore = 0
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
            print("Alas !!! You Lost\n")
            cScore = cScore+1

        elif comp == 3:
            print("Comp Choice : Scissor")
            print("Congo !!! You Won\n")
            uScore = uScore+1
        
        print("Your Score : ",uScore)
        print("Comp Score : ",cScore)
        print("\nPlay Again !")


    elif user == 2:
        print("Your Choice : Paper")
        if comp == 1:
            print("Comp Choice : Rock")
            print("Congo !!! You Won\n")
            uScore = uScore+1

        elif comp == 2:
            print("Comp Choice : Paper")
            print("Its A Tie !!!\n")

        elif comp == 3:
            print("Comp Choice : Scissor")
            print("Alas !!! You Lost\n")
            cScore = cScore+1

        print("Your Score : ",uScore)
        print("Comp Score : ",cScore)
        print("\nPlay Again !")


    elif user == 3:
        print("Your Choice : Scissor")
        if comp == 1:
            print("Comp Choice : Rock")
            print("Alas !!! You Lost\n")
            cScore = cScore+1

        elif comp == 2:
            print("Comp Choice : Paper")
            print("Congo !!! You Won\n")
            uScore = uScore+1

        elif comp == 3:
            print("Comp Choice : Scissor")
            print("Its A Tie !!!\n")
        print("Your Score : ",uScore)
        print("Comp Score : ",cScore)
        print("\nPlay Again !")


    elif user == 4:
        run = False
        print("\nFinal Score")
        print("Your Score : ",uScore)
        print("Comp Score : ",cScore)
        print("\nThanks For Playing\n")

    else:
        print("Invalid Number")
