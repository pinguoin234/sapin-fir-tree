from turtle import *
from math import *
c=[(1,0,0),(0,1,0),(0,0.5,0.75),(1,1,0)]
x=-10
y=-40
def carre(x1,y1,x2,y2,r,g,b):
  hideturtle()
  pencolor(r,g,b)
  width(5)
  penup()
  goto(x1,y1)
  pendown()
  goto(x1,y2)
  goto(x2,y2)
  goto(x2,y1)
  goto(x1,y1)
  for i in range((y2-y1)/5):
    penup()
    goto(x1,y1+i*5)
    pendown()
    forward(x2-x1)
penup()
goto(x,y)
carre(x-45,y-10,x+55,y+95,0,0,1)
carre(x,y,x+10,y+20,0.8,0.4,0)
goto(x+5,y+20)
pencolor(0,0.5,0)
for j in range(3):
  q=[32-j*5,10,5,3]
  for i in range(4-j*2):
    forward(q[i])
    circle(20-i*5,-90)
    left(90)
  goto(x+5,y+20)
  for i in range(4-j*2):
    left(180)
    forward(q[i])
    circle(-(20-i*5),-90)
    left(90)
  goto(x+5,y+20)
carre(x-6,y+25,x+16,y+40,0,0.5,0)
goto(x+5,y+20)
left(90)
forward(57)
def dot(x,y,c):
  penup()
  goto(x,y)
  pencolor(c)
  pendown()
  forward(0.1)
left(-20)
pencolor(1,1,0)
pensize(3)
for i in range(5):
  forward(10)
  left(144)
pensize(5)
x1=[25+x,15+x,5+x,-5+x,15+x,5+x,-5+x,10+x,0+x,5+x]
y1=[23+y,25+y,27+y,29+y,40+y,42+y,44+y,54+y,56+y,66+y,0+y]
d=0
while 1<2:
  d+=1
  if d>len(c)-1:
    d=0
  for i in range(10):
    x1.append(0)
    y1.append(0)
    dot(x1[i],y1[i],c[floor(d)])
    for i in range(200):
      left(1)