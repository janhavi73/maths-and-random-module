import random
while True:
    user_action=input("choose 'rock paper or scissors'")
    possible_action=["rock","paper" or "scissors"]
    computer_action=random.choice(possible_action)
    print(f"\nyou chose {user_action} and compuer chose {computer_action}")

    if user_action==computer_action:
        print(f"computer and yourself picked the same thing, its a tie!")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("you win!")
        else:
            print("you lose.")    
            
    elif user_action=="paper":
        if computer_action=="rock":
            print("you win!")
        else:
            print("you lose.")    

    elif user_action=="paper":
        if computer_action=="rock":
            print("you win!")
        else:
            print("you lose.")    
    elif user_action=="scissors":
        if computer_action=="paper":
            print("you win!")
        else:
            print("you lose.")  
    play_again=input("do you want to play again('y or n')?" )
    if play_again=="n":
        print("thank you for plaing")

    break   
