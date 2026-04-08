import turtle

wn = turtle.Screen()
wn.title("PK Pong Project")
wn.bgcolor("black")
wn.setup(width=1000, height=750)
wn.tracer(0)

# Pause start 
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        pen.goto(0, 0)
        pen.write("Paused", align="center", font=("Courier", 36, "bold"))
    else:
        pen.clear()
        pen.goto(0, 330)
        pen.write(f"Red:{score_a}  Blue:{score_b}", align="center", font=("Courier", 24, "normal"))

paused = False

#Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("Red")
paddle_a.shapesize(stretch_wid=7,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-450,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("Blue")
paddle_b.shapesize(stretch_wid=7,stretch_len=1)
paddle_b.penup()
paddle_b.goto(+450,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0 , 330)
pen.write("Red:0  Blue:0 ", align = "center", font =("Courier", 24,"normal"))


#Moving paddles
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 300:  
        paddle_a.sety(y + 50)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -300:  
        paddle_a.sety(y - 50)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 300:
        paddle_b.sety(y + 50)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -300:
        paddle_b.sety(y - 50)

#KeyBinds
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(toggle_pause, "space")

#Loop
while True:
    wn.update()

    if paused:
        continue

    # Ball move 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball and Paddel Border
    if ball.ycor() > 370:
        ball.sety(370)
        ball.dy *= -1
    
    if ball.ycor() < -370:
        ball.sety(-370)
        ball.dy *= -1
        

    if ball.xcor() > 490:
       ball.goto(0, 0)
       ball.dx *= -1
       score_a += 1
       pen.clear()
       pen.write("Red:{} Blue:{} ".format(score_a,score_b),align = "center", font =("Courier", 24,"normal"))


    if ball.xcor() < -490:
       ball.goto(0, 0)
       ball.dx *= -1
       score_b += 1 
       pen.clear()
       pen.write("Red:{} Blue:{} ".format(score_a,score_b),align = "center", font =("Courier", 24,"normal"))


    # Paddle and ball collisions
    if (ball.xcor() > 440 and ball.xcor() < 450 and (ball.ycor() < paddle_b.ycor() + 70 and ball.ycor() > paddle_b.ycor() -70)):
        ball.setx(440)
        ball.dx *= -1
        
    
    if (ball.xcor() < -440 and ball.xcor() > -450 and (ball.ycor() < paddle_a.ycor() + 70 and ball.ycor() > paddle_a.ycor() -70)):
        ball.setx(-440)
        ball.dx *= -1
       

    