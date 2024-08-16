from turtle import Turtle
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake():
    def __init__(self):
        self.turtles=[]
        self.create_turtle()
        self.head=self.turtles[0]

    def create_turtle(self):
        for position in STARTING_POSITIONS:
          self.add(position)

    def add(self,position):
        t = Turtle()
        t.color("white")
        t.shape("square")
        t.penup()
        t.goto(position)
        self.turtles.append(t)

    def extend(self):
        self.add(self.turtles[-1].position())
    def move(self):
        for t_num in range(len(self.turtles)-1,0,-1):
            new_x=self.turtles[t_num-1].xcor()
            new_y=self.turtles[t_num-1].ycor()
            self.turtles[t_num].goto(new_x,new_y)
        tu=self.head
        tu.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)