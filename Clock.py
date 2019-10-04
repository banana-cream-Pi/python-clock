#I tried to follow all the "pretty code" guide lines sorry if I missed some. :)
'''
Problems:
    minute, and hour hands do not erase their previous versions.
    minute and hour hands only apear after a minute or in the case of the hour hand and hour has passed.
    the minute hands don't always update when they're supposed to
'''
#I'm not imorting anything sinister don't worry.
from turtle import *
from time import *
import random as r
#Messy Code:
#Radius of clock
d = 500
#hiding turtle
ht()
#angles that the hands use
#second hand
x = 0
#minute hand
y = 0
#hour hand
z = 0
#makes the turtle update every 100 actions
tracer(100)
#setting speed so it's not boring
speed(0)
#set up so circle is in center
penup()
rt(90)
fd(d)
lt(90)
pendown()
#Draw circle
circle(d)
pu()
home()
rt(90)
fd(d)

#defing varible "degrees"
degrees = 0
#loop for making the 1-12 postions.
for i in range(12):
    home()
    rt(degrees)
    fd(d / 10 * 9)
    pd()
    fd((d / 10) / 1)
    pu()
    degrees += 30
#loop for drawing the 12, 3, 6, and 9 postions more prominent.
for i in range(4):
    home()
    rt(degrees)
    fd(d / 10 * 8)
    pd()
    fd((d / 10) * 2)
    pu()
    degrees += 90
#loop for minute postions
for i in range(60):
    home()
    rt(degrees)
    fd(d / 10 * 9.5)
    pd()
    fd((d / 10) * .5)
    pu()
    degrees += 6
#Going home with out a trace
pu()
home()
#center dot
pd()
dot((d / 10) / 2)
#going
pu()
home()
#updates the screen once the clock face has been drawn 
update()
#set's tracer back to one
tracer(1)
#defins the hands
def secondhand():
    global x
    for i in range(61):
        lt(90)
        x += 1
        rt(x * 6)
        fd(d - d / 4)
        sleep(1)
        for i in range(3):
            undo()
        pu()
        home()
        pd()
        
    x+=1
        
def minutehand():
    global y
    lt(90)
    y += 1
    rt(y * 6)
    fd(d-d/4) 
    pu()
    home()
    pd()
    
def hourhand():
    global z
    z += 1
    rt(z * 6 * 60)
    fd(d - d / 3)
    pu()
    home()
    pd()
    lt(90)
width(d / 20)
#makes the hands work
while True:
    for i in range(60):
        secondhand()
        minutehand()
        sleep(1)
        
    hourhand()
