from turtle import *
from time import sleep

colormode(255)
red=(233, 35, 35)
green=(75, 183, 75)
yellow=(252, 210, 9)
blue=(86, 146, 195)
r=(120)
speed(2)
seth(-150)
up()

#--------------------   The red petal  -----------------
color(red)
begin_fill()
fd(r)
down()
right(90)
circle(r, 120)
fd(r*3**.5)
left(120)
circle(2*r, 120)
left(60)
fd(r*3**.5)
end_fill()