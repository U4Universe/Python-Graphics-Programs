#program to draw a circle's design 
import turtle
import random

#turtle functions
t = turtle.Turtle()
s= turtle.Screen().bgcolor("#17202A")
t.speed(300)
n=70
h=6

#colors to be chosen for the circle
colors = ["#FFFAFA", "#F0FFF0" , "#F5FFFA", "#F0F8FF" ,"#F5F5F5", "#F5F5DC" , "#FFE4E1"]

for i in range(360):
    line_color = random.choice(colors)
    t.color(line_color)
    t.left(1)
    t.fd(1)
    for j in range(2):
        circle_color = random.choice(colors) 
        t.color(circle_color)
        t.left(2)
        t.circle(100)


t.hideturtle()
turtle.done()
        
