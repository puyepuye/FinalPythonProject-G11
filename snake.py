# Simple Snake Game in Python 3 for Beginners
# By BLP

import turtle
import time
import random
import time

delay = 0.1
global d
d = 0
# Score
score = 0
high_score = 0

# Snake Enemy

enemy = turtle.Turtle()

enemy.speed(0)

enemy.shape("turtle")

enemy.color("purple")

enemy.penup()

enemy.goto(0, 100)
# Set up the screen
wn = turtle.Screen()
t = turtle.Turtle()
wn.title("Snake Game by BLP")
turtle.bgpic("Untitled_Artwork.png")
wn.setup(width=640, height=640)
wn.tracer(0) # Turns off the screen updates
t.penup()
t.setposition(-320, -320)
t.pendown()

t.forward(640) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
 
# drawing second side
t.forward(640) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
 
# drawing third side
t.forward(640) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
 
# drawing fourth side
t.forward(640) # Forward turtle by s units
t.left(90) # Turn turtle by 90 degree
t.hideturtle()



# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("turtle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("BABIES: 0  BABIES COLLECTED: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
        
def go_down():
    if head.direction != "up":
        head.direction = "down"
        
def go_left():
    if head.direction != "right":
        head.direction = "left"
        

def go_right():
    if head.direction != "left":
        head.direction = "right"
        

def move():
    
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        head.setheading(90)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        head.setheading(270)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        head.setheading(180)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        head.setheading(0)
        
# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1
        pen.clear()
        pen.goto(0, 0)
        pen.write("Game Over", font=("Courier", 50
                                     , "normal"), align='center')
        time.sleep(2)
        pen.clear()
        pen.goto(0, 260)
        pen.write("BABIES: 0  BABIES COLLECTED: 0", align="center", font=("Courier", 24, "normal"))
        

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("turtle")
        new_segment.color("grey")
        
        
        
        new_segment.penup()
        segments.append(new_segment)
        
        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("BABIES: {}  BABIES COLLECTED: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    enemy.goto(x, y)
    if head.distance(enemy) < 20:
        # Move the food to a random spot
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # Dissapear
        enemy.goto(1000, 1000)
        # Clear the segments list
        segments.clear()
        # Reset the score
        score = 0
        # Reset the delay
        delay = 0.1
        pen.clear()
        pen.write(
            "BABIES: {}  BABIES COLLECTED: {}".format(score, high_score),
            align="center",
            font=("Courier", 24, "normal"),
        )
    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0
            t.pendown()
            style = ('Courier', 30, 'bold')
            turtle.write("Game Over", font=style, align='center')
            t.penup()
            time.sleep(20)
            pen.clear()
            
            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            style = ('Courier', 15, 'bold')
            pen.color('cyan')
            #pen.write("Game Over", font='Courier', 15, 'bold', align='center')
            pen.write("BABIES: {}  BABIES COLLECTED: {}".format(score, high_score), align="center", font=("Courier", 15, "normal"))

    time.sleep(delay)

wn.mainloop()
