import turtle
import math

# everything is in base SI units, scale just helps keep everything on a normal-sized screen

t = turtle.Turtle()
# parameters
x = 0.1 # x value of the spaceship. Has to be greater than 0, or else the program will crash from the first calculation.
y = 160 # y value of the spaceship
dx = 5 # x velocity (delta-x)
dy = 0 # y velocity (delta-y)
ax = 0 # x acceleration
ay = 0 # y acceleration
pr = 80 # planet radius
pm = 6.67*10**16 # planet mass
scale = 1000 # see function above. Essentially saying 1 turtle unit = scale meters

t.penup() # draw planet
t.goto(0,-pr)
t.pendown()
t.circle(pr)
t.penup()
t.goto(x,y)
t.pendown()

while True:
  theta = math.atan(abs(y/x))
  g = -(6.67*10**-11)*pm/(x**2+y**2) # newton's law of gravitation modified for calculating gravitaitional field strength
  ax = abs(g*math.cos(theta)) # calculating magnitude of accelerations in each direction
  ay = abs(g*math.sin(theta))
  ax /= scale # adjusting scale
  ay /= scale
  
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
