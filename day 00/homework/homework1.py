from turtle import *
speed(30)

#we want to paint a house 

#step 1: draw e square 
begin_fill()
width(7)
color("green")

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#color("yellow")end of square

#drawing a door

forward(70)
color("blue")
begin_fill()


left(90)
forward(120) #height of the door 


right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()
color("red")

begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
left(35)


penup()

goto(20,120 )
pendown()

color("brown")

begin_fill()
left(85)



forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(145,160)
pendown()
color("brown")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

exitonclick()
