import turtle as turtle_module
import random
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list=[(215, 173, 129), (245, 252, 249), (160, 179, 189), (54, 103, 151), (133, 75, 55), (242, 245, 250), (117, 83, 94), (179, 140, 151), (131, 173, 124), (159, 106, 149), (40, 45, 63), (64, 12, 28), (81, 95, 185), (83, 131, 107), (52, 63, 80), (192, 92, 75), (224, 191, 145), (52, 43, 36), (104, 44, 56), (98, 142, 118), (183, 187, 209), (70, 67, 52), (212, 180, 190), (38, 71, 86), (83, 56, 51), (175, 202, 181), (222, 178, 167), (171, 199, 205)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_or_dots=100

for dot_count in range(1,number_or_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0) 