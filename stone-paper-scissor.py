import random


u = 0
b = 0

for i in range(1, 6):
    n = int(input("\nEnter Your Choice: 1.Stone 2.Paper 3.Scissor \n"))

    if n == 1:
        user = "stone"
    elif n == 2:
        user = "paper"
    else:
        user = "scissor"

    bot = random.choice(["stone", "paper", "scissor"])

    if bot == user:
        print("Its a Tie ! Try Again")
        print("Bot's :", bot)
        print("Yours :", user)
    elif bot == "stone":
        if user == "paper":
            print("You Won !")
            print("Bot's :", bot)
            print("Yours :", user)
            u += 1
        else:
            print("You Lose !")
            print("Bot's :", bot)
            print("Yours :", user)
            b += 1
    elif bot == "paper":
        if user == "scissor":
            print("You Won !")
            print("Bot's :", bot)
            print("Yours :", user)
            u += 1
        else:
            print("You Lose !")
            print("Bot's :", bot)
            print("Yours :", user)
            b += 1
    else:
        if user == "stone":
            print("You Won !")
            print("Bot's :", bot)
            print("Yours :", user)
            u += 1
        else:
            print("You Lose !")
            print("Bot's :", bot)
            print("Yours :", user)
            b += 1

print("---------------------------------------------------------------------")
if u == b and u!=0:
    print("\nMATCH TIED !")
elif u > b:
    print("\nYOU ARE WINNER !")
else:
    print("\nYOU LOSE THE GAME !")

print("Your Score : ", u)
print("Bot's Score : ", b)



