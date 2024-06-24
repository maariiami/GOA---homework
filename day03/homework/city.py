from turtle import*

# step 1: draw a square
speed(10)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)      #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("purple")
left(30)
forward(25)

color("black")
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(200,200)
pendown()

color("purple")
right(180)
forward(25)

color("black")
begin_fill()
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(0,0)
pendown()

left(90)
color("green")
forward(200)
right(90)
forward(200)
right(90)
forward(200)

left(120)
color("red")
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()

left(30)
color("green")
forward(25)
left(90)
color("blue")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(0,200)
pendown()

left(90)
color("purple")
forward(25)
right(90)
color("blue")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(0,0)
pendown()

right(180)
color("green")
forward(70)
right(90)
color("yellow")
begin_fill()
forward(120)
left(90)
forward(60)
left(90)
forward(120)
end_fill()

right(90)
color("green")
forward(70)
color("orange")
forward(200)
right(90)
forward(200)
right(90)
forward(200)

left(120)
color("red")
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()

left(30)
color("orange")
forward(25)
left(90)
color("pink")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

right(90)
color("orange")
forward(75)
right(90)
color("orange")
forward(200)
right(90)
color("green")
forward(25)

color("pink")
begin_fill()
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

right(90)
color("green")
forward(125)
right(90)
color("orange")
forward(70)

right(90)
color("yellow")
begin_fill()
forward(120)
left(90)
forward(60)
left(90)
forward(120)
end_fill()

right(90)
color("orange")
forward(70)
color("white")
forward(90)

color("brown")
begin_fill()
right(90)
forward(80)
left(90)
forward(20)
left(90)
forward(80)
end_fill()
left(180)
forward(80)
right(90)
forward(10)
begin_fill()
color("green") 
circle(radius=30)
end_fill()

penup()
goto(200,0)
pendown()

left(45)
color("white")
forward(400)
color("yellow")
begin_fill()
circle(radius=50)
end_fill()
















     
exitonclick()
