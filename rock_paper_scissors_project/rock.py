
from random import randint

game_active = True 

while game_active:
    print("Lets play Rock, Paper, Scissors")
    win = 0
    lose = 0
    name = input("What's your name? ")
    name_formatted = name.title()
    print(f"\nHey {name_formatted} input your command!")
    playing_active = True
    while playing_active:
        option = input("\nRules, Play, Strategy or Quit. : ")
        if option.lower() == "rules":
            print("\nThe rock is a closed fist; paper is a flat hand with fingers and thumb extended and the palm facing downward; and scissors is a fist with the index and middle fingers fully extended toward the opposing player. Rock wins against scissors; paper wins against rock; and scissors wins against paper.")
        elif option.lower() == "strategy":
            from IPython.display import YouTubeVideo
            video = YouTubeVideo("AnRYS02tvRA")
            display(video)
        elif option.lower() == "quit":
                print(f"Thanks for playing {name_formatted}!")
                playing_active = False
        elif option.lower() == "play":
            user_answer = input("Choose your weapon. Rock/Paper/Scissors :  ")
            comp_int = randint(1,3)
            if comp_int == 1:
                computer_answer = "rock"
            elif comp_int == 2:
                computer_answer = "paper"
            else:
                computer_answer = "scissors"
            if user_answer.lower() == computer_answer:
                print("\nTie!")
            elif (user_answer.lower() == "rock" and computer_answer == "scissors") or (user_answer.lower() == "paper" and computer_answer == "rock") or (user_answer.lower() == "scissors" and computer_answer == "paper"):
                win += 1
                print(f"\nYou win, congratulations {name_formatted}!")
            elif (user_answer.lower() == "scissors" and computer_answer == "rock") or (user_answer.lower() == "rock" and computer_answer == "paper") or (user_answer.lower() == "paper" and computer_answer == "scissors"):
                lose += 1
                print(f"\nYou lose, better luck next time {name_formatted}!")
            print(f"Wins: {win} Loses: {lose}")
        else: 
            print("\nThat's not a valid play. Check the rules if you're having trouble.")   
    game_active = False


    
    
