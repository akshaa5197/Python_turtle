from turtle import Turtle,Screen
from turtle import*
screen=Screen()
screen.setup(400,400)

#screen.bgcolor('green')#it gives screen bg color
#color('green')# circle filled with green otherwise it was black
write('TURTLE IMPLEMENTATION',move=False,align='center',font=('Arial'))
dot(300)
color('red')
style=('Arial',40,'bold')
write('HELLO',font=style,align='center')#green bg pe red hello
hideturtle()# chhota arrow nhi aaega
penup()#very important othetwise extra lines
goto(0,-80)#for aligining 1 text wrt to other else both were overlapping

color('yellow')
style1=('TimesNewRoman',40,'bold')

write('akanksha',font=style1,align='center')

colours={'verylime':'#A7E30E','reallyraspberry':'#FA057F'}

print(colours['reallyraspberry'])#for making the key
screen.bgcolor(colours['reallyraspberry'])



