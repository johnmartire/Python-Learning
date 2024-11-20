height= int (input("Are you tall enough for the roller coaster in cm? Enter your height:"))
bill=0
if height > 120:
    print("You are tall enough!")
    age= int(input("What is your age?"))
    if age <= 12: 
        bill=5
        print("Please pay $5.")
    elif age <= 18:
        bill=7
        print("Please pay $7.")

    else:
        bill=12
        print("Please pay $12.")   
    wants_photo= input("Do you want a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
    # Add $3 to their bill
       bill += 3
    print(f"Your final bill is {bill}")
else: 
    print("you are not tall enough.")   