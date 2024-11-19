
print("Welcome to the tip calculator!")
bill =input("what is the total bill? $")
tip=input("How much tip would like to give? 10, 12, or 15? ")
tip= a=10; b=12 ;c=15
tip= a=1.10;b=1.12;c=1.15
spilt= input("How many people to spilt the bill?")
bill = float(bill);tip = float(tip); spilt= float(spilt)
total=tip*bill/spilt
total= float(total)
print("Each person should pay:");print(round(total,2))