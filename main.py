import turtle


turtle.Screen().bgcolor("grey")
turtle.Screen().setup(300, 400)

turtle = turtle.Turtle()
size = 0

while True:
    for i in range(4):
        turtle.forward(size+1)
        turtle.left(90)

        size= size-5
    size=size+1

    
turtle.mainloop()
turtle.done()