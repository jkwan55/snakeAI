import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#set up the screen
window = turtle.Screen()
window.title("SnakeAI")
window.bgcolor("black")
window.setup(width=800, height=800)
window.screensize(790, 790)
window.tracer(0)

#snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

wall = turtle.Turtle()
wall.speed(0)
wall.shape("square")
wall.color("green")
wall.penup()
wall.goto(-400, 400)
wall.pensize(20)
wall.pendown()
for i in range(4):
    wall.forward(800)
    wall.right(90)
wall.penup()


#food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(-380, 380)

segments = []

#score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("gray")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#movement
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def buttonUp():
    if head.direction != "down":
        head.direction = "up"

def buttonDown():
    if head.direction != "up":
        head.direction = "down"

def buttonLeft():
    if head.direction != "right":
        head.direction = "left"

def buttonRight():
    if head.direction != "left":
        head.direction = "right"

#Key press
window.listen()
window.onkeypress(buttonUp, "w")
window.onkeypress(buttonDown, "s")
window.onkeypress(buttonLeft, "a")
window.onkeypress(buttonRight, "d")
window.onkeypress(buttonUp, "Up")
window.onkeypress(buttonDown, "Down")
window.onkeypress(buttonLeft, "Left")
window.onkeypress(buttonRight, "Right")

#game loop
while True:

    window.update()

    if head.distance(food) < 20:
        x = random.randint(-19, 19) * 20
        y = random.randint(-19, 19) * 20
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        score += 100

        if score > high_score:
            high_score = score


    for body in range(len(segments)-1, 0, -1):
        x = segments[body-1].xcor()
        y = segments[body-1].ycor()
        segments[body].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    if head.xcor()>390 or head.xcor()<-390 or head.ycor()>390 or head.ycor()<-390:

        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(10000, 10000)
        segments.clear()

        score = 0

    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(10000, 10000)
            segments.clear()
            score = 0

    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

window.mainloop()


if __name__ == "__main__" :
    print("main")
