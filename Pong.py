#pong

import turtle
import os
import random


rand = [-1,1]
rand_vel = [-0.3, 0.3] #change the speed of the ball here


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score

score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)



#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball

ball = turtle.Turtle()
ball.speed(0) #speed of animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = random.choice(rand_vel)
ball.dy = random.choice(rand_vel)

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0  Jugador B: 0", align="center",font=("courier", 24, "normal"))


#Paddles movement

def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)


#keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop

while True:
    wn.update()

    #move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking (ball)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= random.choice(rand)
        score_a += 1
        pen.clear()
        pen.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.dy *= random.choice(rand)
        score_b += 1
        pen.clear()
        pen.write("Jugador A: {}  Jugador B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    #paddle colition

    if paddle_b.ycor() >= 250:
        paddle_b.goto(350,250)

    if paddle_b.ycor() <= -250:
        paddle_b.goto(350,-250)

    if paddle_a.ycor() >= 250:
        paddle_a.goto(-350,250)

    if paddle_a.ycor() <= -250:
        paddle_a.goto(-350,-250)

    #paddle and ball colitions

    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
