import turtle
import time

delay = 0.1

#set up the screen
window = turtle.Screen()
window.title("SnakeAI")
window.bgcolor("black")
window.setup(width=800, height=800)
window.tracer(0)

#snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

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
    head.direction = "up"

def buttonDown():
    head.direction = "down"

def buttonLeft():
    head.direction = "left"

def buttonRight():
    head.direction = "right"

#Key press
window.listen()
window.onkeypress(buttonUp, "w")
window.onkeypress(buttonDown, "s")
window.onkeypress(buttonLeft, "a")
window.onkeypress(buttonRight, "d")

#game loop
while True:
    window.update()
    move()
    time.sleep(delay)

window.mainloop()



if __name__ == "__main__" :
    print("main")
