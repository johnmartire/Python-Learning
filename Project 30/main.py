import random
cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]

print("""   
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/ 
""")
begin=input("Do you want to play a game of Blackjack? Type 'y' or 'n': " )

if 'y':
    def start():
        def cardpicker():
            return random.choice(cards)
        user=[cardpicker(),cardpicker()]
        user_score=sum(user)
        computer=[cardpicker(),cardpicker()]
        computer_score=sum(computer)
        if computer_score <=17:
            computer.append(cardpicker())
            computer_score=sum(computer)
        print("Your cards",user,"current score: ",user_score)
        print("Computers first card: ",computer[0])
        another_card=input("type 'yes' to get another card,type 'no' to pass: ")
        if another_card=='no':
           print("Your final hand",[user],"final score: ",user_score)
           print("Computers final hand",[computer],"final score: ",computer_score)
        if another_card=='yes':
            user.append(cardpicker())
            user_score=sum(user)
            print("Your final hand",user,"final score: ",user_score)
            print("Computers final hand",computer,"final score: ",computer_score)
        if user_score <= 21 and user_score> computer_score or computer_score>21:
            print("You win!!")
        if computer_score <=21 and computer_score> user_score or user_score > 21:
            print("You lose...")
        if user_score==computer_score:
            print("Draw")
        
        play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            
start()
