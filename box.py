from __future__ import division
import turtle
import time

x=-300
y=-300
turtle.ht()
turtle.pu()
turtle.goto(x,y)
turtle.pd()
turtle.pen( pencolor="black", pensize=4)
turtle.speed(0)
def fillbg(x,y):
    turtle.begin_fill()
    turtle.fillcolor("blue")
    turtle.goto(x,y)
    turtle.goto(x,y+200)
    turtle.goto(x+800,y+200 )
    turtle.goto(x+800,y)
    turtle.goto(x,y)
    turtle.pu()
    turtle.goto(x+400,y+200)
    turtle.pd()
    turtle.goto(x+400,y)
    turtle.pd()
    turtle.end_fill()
fillbg(x,y)

#now prepare for drawing the lines
max_health=100
max_mana=100
lines_length=200
a=60.0
# its an assumption till we have a variable that gives us the current health.
def love():
    b=a/max_health
    print(b)
    c=b*lines_length
    print(c)
    return c
l=love()
print(l)
#done for the health.
def mana ():
    m=0
    
    time.sleep(1)
    m=m+1
    
    print(m)
    print(m+2)
    return m
   

m=mana()
print(m)
run =1
while run == 1:
    mana()
    
    if m >100:
        m=m-50
        
    else:
        
      print ("i hate cooding")
      break
     
   

 

    
  
def kill():                                      #variable for the mana.
    m2= m/max_mana
    print(m2)
    m3 =m2*lines_length
    print(m3)
    return m3

s=kill()
print(s)

# done for the mana.
health=turtle.Turtle()
health.ht()
health.pu()
health.goto(x+100,y+150)
health.pd()
health.pen( pencolor="red", pensize=6)
def draw_health():
    y=-300
    health.goto(l,y+150)
    time.sleep(6)
draw_health()

fun = 1

while fun == 1:
    draw_health()
    if fun >1:
        print("shit is happening")
    else:
        print("its ok")
        break


def clear_every_5_sec():
    health.clear()
    time.sleep(5)
    print("doen")
    return

 
clear_every_5_sec()

    
#woooooooh health line is done.





mana=turtle.Turtle()
mana.ht()
mana.penup()
mana.goto(x+100,y+75)
mana.pd()
mana.pen( pencolor="green", pensize=6)
def draw_mana():
    mana.goto(s,y+75)
    time.sleep(5)
school=0
while school == 0:
    draw_mana()
    if school<1:
        print("i dont know what im doing")
        break
    
draw_mana()
def clear_every_6_sec():
    mana.clear()
    time.sleep(5)
    print("done2")
    return
clear_every_6_sec()



#done for the mana and for players1 everything.

