from random import randint

game_active = True 

while game_active:
    print("Lets play Rock, Paper, Scissors")
    win = 0
    lose = 0
    name = input("What's your name? ")
    print(f"Hey " +  name.title() + " input your command!")
    playing_active = True
    while playing_active:
        option = input("rules, play, or quit. : ")
        if option.lower() == "rules":
            print("The rock is a closed fist; paper is a flat hand with fingers and thumb extended and the palm facing downward; and scissors is a fist with the index and middle fingers fully extended toward the opposing player. Rock wins against scissors; paper wins against rock; and scissors wins against paper.")
        elif option.lower() == "quit":
                print(f"Thanks for playing {name}!")
                playing_active = False
        elif option.lower() == "play":
            user_answer = input("choose your weapon. rock/paper/scissors :  ")
            comp_int = randint(1,3)
            if comp_int == 1:
                computer_answer = "rock"
            elif comp_int == 2:
                computer_answer = "paper"
            else:
                    computer_answer = "scissors"
            if user_answer.lower() == computer_answer:
                print("Tie!")
            elif (user_answer.lower() == "rock" and computer_answer == "scissors") or (user_answer.lower() == "paper" and computer_answer == "rock") or (user_answer.lower() == "scissors" and computer_answer == "paper"):
                win += 1
                print(f"You win, Congratulation {name}!")
            elif (user_answer.lower() == "scissors" and computer_answer == "rock") or (user_answer.lower() == "rock" and computer_answer == "paper") or (user_answer.lower() == "paper" and computer_answer == "scissors"):
                lose += 1
                print("You lose, better luck next time {name}!")
            print(f"Wins: {win} loses: {lose}")
        else: 
            print("That's not a valid play. Check your spelling!")

        

    game_active = False


    
    
