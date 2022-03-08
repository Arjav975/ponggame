from turtle import Turtle


class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def move_up(self):
        new_y_coord = self.ycor() + 20
        self.goto(self.xcor(), new_y_coord)

    def move_down(self):
        new_y_coord = self.ycor() - 20
        self.goto(self.xcor(), new_y_coord)
