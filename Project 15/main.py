print("Welcome to Python Pizza Deliveries!")
size= input("What size pizza do want? S, M or L:")
pepperoni= input("Do you want pepperoni on your pizza? Y or N:")
extra_cheeze = input ("Do you want extra cheese? Y or N: ")
total_bill=0

if size == "S":
    total_bill = 15
elif pepperoni== "Y":
    total_bill += 2
if size == "M":
    total_bill = 20
if size == "L": 
    total_bill = 25
else:
     print("your input is invalid")

if pepperoni == "Y":
     total_bill += 3
if extra_cheeze == "Y":
 total_bill+= 1
print(f"Your final bill is: $",total_bill)