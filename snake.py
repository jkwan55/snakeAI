import turtle
import time
import random


class Snake:
    def __init__(self):
        self.delay = 0.1
        self.score = 0
        self.high_score = 0

        # set up the screen
        self.window = turtle.Screen()
        self.window.title("SnakeAI")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=800)
        self.window.screensize(790, 790)
        self.window.tracer(0)

        # snake
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"

        self.wall = turtle.Turtle()
        self.wall.speed(0)
        self.wall.shape("square")
        self.wall.color("green")
        self.wall.penup()
        self.wall.goto(-400, 400)
        self.wall.pensize(20)
        self.wall.pendown()
        for i in range(4):
            self.wall.forward(800)
            self.wall.right(90)
        self.wall.penup()

        # food
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("square")
        self.food.color("red")
        self.food.penup()
        self.food.goto(-380, 380)

        self.segments = []

        # score
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("gray")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

        # Key press, dont need for AI
        self.window.listen()
        self.window.onkeypress(self.buttonUp, "w")
        self.window.onkeypress(self.buttonDown, "s")
        self.window.onkeypress(self.buttonLeft, "a")
        self.window.onkeypress(self.buttonRight, "d")
        self.window.onkeypress(self.buttonUp, "Up")
        self.window.onkeypress(self.buttonDown, "Down")
        self.window.onkeypress(self.buttonLeft, "Left")
        self.window.onkeypress(self.buttonRight, "Right")

        # game loop
        while True:

            self.window.update()

            if self.head.distance(self.food) < 20:
                x = random.randint(-19, 19) * 20
                y = random.randint(-19, 19) * 20
                self.food.goto(x, y)

                self.new_segment = turtle.Turtle()
                self.new_segment.speed(0)
                self.new_segment.shape("square")
                self.new_segment.color("white")
                self.new_segment.penup()
                self.segments.append(self.new_segment)

                self.score += 100

                if self.score > self.high_score:
                    self.high_score = self.score

            for body in range(len(self.segments) - 1, 0, -1):
                x = self.segments[body - 1].xcor()
                y = self.segments[body - 1].ycor()
                self.segments[body].goto(x, y)

            if len(self.segments) > 0:
                x = self.head.xcor()
                y = self.head.ycor()
                self.segments[0].goto(x, y)

            self.move()

            if self.head.xcor() > 390 or self.head.xcor() < -390 or self.head.ycor() > 390 or self.head.ycor() < -390:

                self.head.goto(0, 0)
                self.head.direction = "stop"

                for segment in self.segments:
                    segment.goto(10000, 10000)
                self.segments.clear()
                self.score = 0

            for segment in self.segments:
                if self.head.distance(segment) < 20:
                    time.sleep(0.5)
                    self.head.goto(0, 0)
                    self.head.direction = "stop"

                    for segment in self.segments:
                        segment.goto(10000, 10000)
                    self.segments.clear()
                    self.score = 0

            self.pen.clear()
            self.pen.write("Score: {}  High Score: {}".format(self.score, self.high_score), align="center",
                      font=("Courier", 24, "normal"))

            time.sleep(self.delay)

        self.window.mainloop()

    # movement
    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)
        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)
        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)
        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def buttonUp(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def buttonDown(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def buttonLeft(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def buttonRight(self):
        if self.head.direction != "left":
            self.head.direction = "right"