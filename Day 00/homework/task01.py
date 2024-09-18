from turtle import *
#we want to paint a house

#step 1:draw a square
speed(30) 
width(7)
color("blue")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

#end of square 

#step 2: print a door 

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of a door 
#step 3:print the roof 


penup()
goto (200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of a roof 
#step 4:print the windows

color("blue")
left(30)
forward(40)
color("brown")
begin_fill()
left(90)
forward(40)
right(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
end_fill()
#end of first window 

color("blue")
forward(40)
right(90)
forward(200)
right(90)
forward(40)
color("brown")
begin_fill()
right(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
end_fill()


#end of the windows 


#end of a house 





 

exitonclick()