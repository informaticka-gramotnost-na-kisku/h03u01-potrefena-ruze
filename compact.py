import turtle
turtle.speed(0); turtle.tracer(100); turtle.hideturtle()

def draw(axiom, size, angle=30):
  xlen = len(axiom.replace('/', '').replace('\\', '')); elem = size / xlen if xlen > 0 else size
  for i in axiom: {'~': (lambda: turtle.bk(elem)), '-':  (lambda : turtle.fd(elem)), '/':  (lambda : turtle.rt(angle) ), '\\': (lambda : turtle.rt(-angle)) }[i]()

for _ in range((6*2+1)):
  for _ in range(6): draw('-----/--\\\\--/-----', 50); draw('/', 50, 360/6)
  draw('/-~\\', 50 * 4/3,  77); draw('-/', 50)
  
turtle.getscreen()._root().mainloop()
