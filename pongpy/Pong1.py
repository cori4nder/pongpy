# Simply Pong in Python for Beginners
# By @spannerbyte

import turtle

wn = turtle.Screen()
wn.title("PongPy by @spannerbyte")
wn.bgcolor("White")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("Blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("Blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("Blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1


# Function
def paddle_a_up():
    y = paddle_a.ycor() # .ycor - vem do turtle module
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor() # .ycor - vem do turtle
  y -= 20
  paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # .ycor - vem do turtle module
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor() # .ycor - vem do turtle
  y -= 20
  paddle_b.sety(y)

# Keyboard biding
wn.listen() 
wn.onkeypress(paddle_a_up, "w") 
wn.onkeypress(paddle_a_down, "s") 
wn.onkeypress(paddle_b_up, "Up") 
wn.onkeypress(paddle_b_down, "Down") 

# Main game loop
while True:
  wn.update()

  # Move the ball to the
  ball.setx(ball.xcor() + ball.dx) # xcor é setado em 0, 0 +
  ball.sety(ball.ycor() + ball.dy) # ycor é setado em 0, 0 +

  # Border checking
  if ball.ycor() > 290: # muda a direção da bola ao tocar na borda do lado direito
    ball.sety(290) 
    ball.dy *= -1
  
  if ball.ycor() < -290:
    ball.sety(-290) 
    ball.dy *= -1
  
  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
  
  if ball.xcor() < -390:
     ball.goto(0, 0)
     ball.dx *= -1

  # Paddle and Ball collisions
  if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
     ball.dx *= -1

  elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
      ball.dx *= -1
