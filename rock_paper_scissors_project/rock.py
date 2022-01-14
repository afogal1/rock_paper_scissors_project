from random import randint

game_active = True 

while game_active:
    print("Lets play Rock, Paper, Scissors")
    name = input("What's your name? ")
    print(f"Hey " +  name.title() + " input your command!")
    playing_active = True
    while playing_active:
        option = input("Rules, play, change name, or quit. : ")
        if option.lower() == "rules":
            print("blah blah blah")
        elif option.lower() == "play":
            user_answer = input("choose your weapon. Rock/Paper/Scissors :  ")
            if user_answer == computer:
                print("Tie!")
            elif (user_answer == "rock" and computer == "scissors") or (user_answer == "paper" and computer == "rock") or (user_answer == "scissors" and computer == "paper"):
                print("You win!")
            elif (user_answer == "scissors" and computer == "rock") or (user_answer == "rock" and computer == "paper") or (user_answer == "paper" and computer == "scissors"):
                print("You lose!")
            
            
            else: 
                print("...")

            

    
    
