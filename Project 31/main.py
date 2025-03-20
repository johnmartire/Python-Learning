from random import randint
print("""
      
      
   _____                       _______ _            _   _                 _                
  / ____|                     |__   __| |          | \ | |               | |               
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| 
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |    
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|    
                                                                                           
                                                                                           
      
      
      """)

print("Welcome to the number Guessing game!")
print("Im thinking of a number bewtween 1 and 100.")

def guesser():
 number=int (randint(1,100))
 choice=input("Choose a difficulty.Type 'easy' or 'hard': ")
 lives=10
 if choice=='easy':
    lives=10
    print(f"You have {lives} attempts remaining to guess the number")
 if choice=='hard':
    lives=int(5)
    print(f"You have {lives} attempts remaining to guess the number")
 while True:
    guess=(int(input("Make a guess:")))
    
    if guess<number:
        lives=lives-1
        print("Too low")
        print("Guess again")
        print(f"You have {lives} attempts remaining to guess the number")
    if guess>number:
        lives=lives-1
        print("Too high")
        print(f"You have {lives} attempts remaining to guess the number")
    if lives==0:
        print("game over.")
        break
    if guess==number:
        print(f"You Guessed Correctly! the number is {number}")
        break
        

guesser()

while True:
   again=input("Do you want to play again? 'y' or 'n': ")
   if again=='y':
      guesser()
