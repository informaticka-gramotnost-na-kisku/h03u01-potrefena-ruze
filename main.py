import Turtle

color="#FF0022"
speed=0
angle=60
size=50

def one_side(pen):
  retroAngle = angle /2
      
  pen.forward(size/3)
  pen.right(retroAngle)
  pen.forward(size/6)
  pen.right(-retroAngle*2)
  pen.forward(size/6)
  pen.right(retroAngle)
  pen.forward(size/3)
  
  pen.right(angle)
    
def patvar(pen):
  for _ in range(0, 36):
    for i in range(0, 6):
      one_side(pen)
     
    retroAngle = 105 
    pen.right(-retroAngle)
    pen.back(size/2 + 10)
    pen.forward(size/2 + 10)
    pen.right(retroAngle)
      
    pen.forward(size)
    pen.right(angle/2)
  

myPen = turtle.Turtle()
myPen.speed(speed)
myPen.color(color)

myPen.penup()
myPen.goto(0,100) #position cursor at the bootom right of the screen
myPen.pendown()

patvar(myPen)
#one_side(myPen)
myPen.penup()
myPen.goto(-100, -100)
