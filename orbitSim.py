import turtle
import math

t = turtle.Turtle()
# parameters
x = 10 # x value of the spaceship. Has to be greater than 0, or else the program will crash from the first calculation.
y = 160 # y value of the spaceship
dx = 25 # x velocity (delta-x)
dy = 0 # y velocity (delta-y)
ax = 0 # x acceleration
ay = 0 # y acceleration
pr = 80 # planet radius
pm = 100000 # planet mass

t.penup() # draw planet
t.goto(0,-pr)
t.pendown()
t.circle(pr)
t.penup()
t.goto(x,y)
t.pendown()

while True:
  theta = math.atan(abs(y/x))
  g = -pm/(x**2+y**2) # newton's law of gravitation modified for calculating gravitaitional field strength, with G=1
  ax = abs(g*math.cos(theta)) # calculating magnitude of accelerations in each direction
  ay = abs(g*math.sin(theta))
  if x > 0 and y > 0: # changing direction of acceleration depending on orientation relative to planet
    ax *= -1
    ay *= -1
  elif x > 0 and y < 0:
    ax *= -1
  elif x < 0 and y > 0:
    ay *= -1
  dx += ax # changing dx, dy, x, and y values
  dy += ay
  x += dx
  y += dy
  
  t.goto(x,y)
