from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen):
    super().__init__()
    self.hideturtle()
    self.speed(0)
    self.shape("square")
    self.color("Green")
    self.penup()
    self.showturtle()
    self.alive = True
    self.direction = "right"
    screen.onkey(self.left, "a")
    screen.onkey(self.right, "d")
    screen.onkey(self.up, "w")
    screen.onkey(self.down, "s")



  def up(self):
    if self.direction != "down":
      self.setheading(90)
      self.direction = "up"

  def down(self):
    if self.direction != "up":
      self.setheading(270)
      self.direction = "down"

  def left(self):
    if self.direction != "right":
      self.setheading(180)
      self.direction = "left"

  def right(self):
    if self.direction != "left":
      self.setheading(0)
      self.direction = "right"

  def move(self):
    self.forward(2)
    if self.xcor() > 230 or self.xcor() < -230:
        self.alive = False
        self.hideturtle()
    if self.ycor() > 230 or self.ycor() < -230:
        self.alive = False
        self.hideturtle()
    
  def die(self):
    pass


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    self.shape("square")
    self.color(generate_color())
    self.goto(other.pos())

  def move(self, other):
    for i in range(len(body)-1, 0, -1):
      body[i].goto(body[i-1].pos())
    if body:
      body[0].goto(other.pos())

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.speed(0)
    self.shape("circle")
    self.color("red")
    self.penup()
    self.goto(random.randint(-230, 230), random.randint(-230, 230))
    self.showturtle()

  def relocate(self):
    self.goto(random.randint(-230, 230), random.randint(-230, 230))

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()

body = []


playing_area()

p1 = Head(screen)
apple1 = Apple()

while p1.alive:
  p1.move()
  if p1.distance(apple1) < 20:
    apple1.relocate()

  for segment in body:
    segment.move(segment)

screen.exitonclick()
