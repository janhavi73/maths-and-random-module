import random
playing =True
number=str(random.randint(10,20))

print("i will think of a number between 10-20 and you have to guess it one number by one")
print("the game will end when you get one hero!")
while playing:
    guess=input("give me your best guess\n")
    if number==guess:
        print("yay, you won")
        print("the number was ",number) 
        break

    else:
        print("you aren't there yet, keep guessing!\n")   