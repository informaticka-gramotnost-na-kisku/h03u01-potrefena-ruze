import turtle

angle=60
size=50

turtle.speed(0)
turtle.tracer(100)
turtle.hideturtle()
turtle.color("#FF0022")

def one_side():
  turtle.forward(size/3)
  turtle.right(angle /2)
  turtle.forward(size/6)
  turtle.right(-angle)
  turtle.forward(size/6)
  turtle.right(angle /2)
  turtle.forward(size/3)
  turtle.right(angle)
    
def patvar():
  for _ in range(0, 36):
    for i in range(0, 6):
      one_side()
     
    retroAngle = 105 
    turtle.right(-retroAngle)
    turtle.back(size/2 + 10)
    turtle.forward(size/2 + 10)
    turtle.right(retroAngle)
      
    turtle.forward(size)
    turtle.right(angle/2)
  
patvar()
turtle.getscreen()._root.mainloop()
