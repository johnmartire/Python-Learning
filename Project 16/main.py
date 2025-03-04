height= int (input("Are you tall enough for the roller coaster in cm? Enter your height:"))
bill=0
if height > 120:
    print("You are tall enough!")
    age= int(input("What is your age?"))
    if age <= 12: 
        bill=5
        print("Child tickets are $5.")
    elif age <= 18:
        bill=7
        print("youth tickets are $7.")
    if age >=45 or age <=55:
        print("Everything is going to be ok. have a free ride on us!")
    else:
        bill=12
        print("Adult tickets are $12.")   
    wants_photo= input("Do you want a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
    # Add $3 to their bill
       bill += 3
    print(f"Your final bill is {bill}")
else: 
    print("you are not tall enough.")