from random import randint
print("Guess The Number (Hint : Its between 1 and 20)")
print("Allowed number of guesses : 9")
num = randint(1, 20)

for i in range(0, 9):
    print("Guesses left :", 9 - i)
    x = int(input("Enter Your Guessed Number : "))
    if x > num:
        print("you entered a greater Number\n")
    elif x < num:
        print("you entered a smaller Number\n")
    else:
        print("Voila!! You Guessed it right")
        break


else:
    print("Game Over !")