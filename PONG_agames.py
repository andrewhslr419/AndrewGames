import turtle
import winsound
#Draw a square
# for i in range(8):
#     turtle.forward(200)
#     turtle.left(90)

wn = turtle.Screen()

wn.title('Pong 2020 by Andrew')
wn.bgcolor('black')
wn.tracer(0)
wn.setup(width=800, height=600)
tracer=(0)

#        Score
score_a = 0
score_b = 0

#      PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('yellow')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#      PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('violet')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
#       BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('green')
ball.penup()
ball.goto(0,0)

ball.dx = 0.5
ball.dy = -0.5

#PEN AND SCORE BOARD
pen = turtle.Turtle()
pen.speed(0)
pen.color('purple')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('PlayerA: 0  PlayerB: 0', align='center', font=('Courier', 24, 'normal'))


#   GAME FUNCTION
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -10
    paddle_b.sety(y)

# KEYBOARD BINDING
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')

wn.onkeypress(paddle_b_up, '-')
wn.onkeypress(paddle_b_down, '+')


# MAIN GAME LOOP
while True:
    wn.update()

    #MOVE THE BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #BORDER CHECKING
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
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write('PlayerA: {} PlayerB: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write('PlayerA: {} PlayerB: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
    #PADDLE AND BALL COLLISIONS
    if ball.xcor() > 340  and ball.xcor() < 350 and (ball.ycor() <
     paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        # winsound.PlaySound("Ball.mp3", winsound.SND_ASYNC)

    if ball.xcor() < -340  and ball.xcor() > -350 and (ball.ycor() <
     paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
