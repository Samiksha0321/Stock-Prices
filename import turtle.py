import turtle
import random

def draw_spiral(min_radius, max_radius, min_value, max_value):
  radius = min_radius
  value = random.randint(min_value, max_value)
  turtle.penup()
  turtle.goto(radius, value)
  turtle.pendown()

  while radius <= max_radius:
    turtle.forward(radius)
    radius += 1
    value = random.randint(min_value, max_value)
    turtle.goto(radius, value)

def main():
  draw_spiral(0, 100, 0, 100)

if __name__ == "__main__":
  main()