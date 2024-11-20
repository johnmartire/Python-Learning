print ("Welcome to the bmi calculator")
height= float (input("Enter your height:"))
weight= float (input("Enter your weight:"))
bmi = weight / (height ** 2)

if bmi >= 18.5:
    print("normal weight",bmi)
elif bmi >= 25:
    print("overweight",bmi) 
else:
    print("underweight ",bmi)
