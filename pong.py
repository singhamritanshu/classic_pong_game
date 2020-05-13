# Classic pong game in python

import turtle

wn = turtle.Screen()
wn.title("Pong by singhamritanshu(GitHub)")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0) # This is not the speed of the paddle it is for the speed of the animation, it puts the speed to the maximum.
paddle_a.shape("square")
paddle_a.shapesize(stretch_len = 1,stretch_wid = 5)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)# starting position of the paddle.

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0) # This is not the speed of the paddle it is for the speed of the animation, it puts the speed to the maximum.
paddle_b.shape("square")
paddle_b.shapesize(stretch_len = 1,stretch_wid = 5)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)# starting position of the paddle.

# Ball

ball = turtle.Turtle()
ball.speed(0) # This is not the speed of the paddle it is for the speed of the animation, it puts the speed to the maximum.
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)# starting position of the ball
ball.dx = 2
ball.dy = -2

# Player Info

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0  Player B : 0", align="center", font=("Courier", 24, "normal"))

# Score Counting

score_a = 0
score_b = 0



# Function to move paddle_a 

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y) 

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y) 

# Function to move paddle_b 

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y) 


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y) 

# Keboard binding 
wn.listen()

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop

while True:
    wn.update()
    # Movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
        

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisoin
    if (ball.xcor() > 340 and ball.xcor() > 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    
    # Declaring the winner 

    if score_a >= 10 or score_b >= 10:
        if score_a > score_b:
            pen.clear()
            pen.write("Player A won", align="center", font=("Courier", 30, "normal"))
            ball.goto(0,0)
            paddle_a.goto(-350,0)
            paddle_b.goto(350,0)
        else:
            pen.clear()
            pen.write("Player B won", align="center", font=("Courier", 30, "normal"))
            ball.goto(0,0)
            paddle_a.goto(-350,0)
            paddle_b.goto(350,0)

    

    
