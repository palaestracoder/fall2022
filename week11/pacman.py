import turtle 
import time

class PacMan:
    x = 0
    y = 0
    mouth = 60
    direction = -3
    color = 'yellow'
    radius = 50

    def __init__(self, t):
        self.t = t

    def draw(self):
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pensize(5)
        self.t.pencolor(self.color)
        self.t.pendown()
        self.t.circle(self.radius, 90 - self.mouth)
        pos = self.t.position()
        self.t.goto(self.x, self.y + self.radius)
        self.t.penup()
        self.t.goto(pos[0], pos[1])
        self.t.circle(self.radius, self.mouth * 2)
        pos = self.t.position()
        self.t.pendown()
        self.t.goto(self.x, self.y + self.radius)
        self.t.penup()
        self.t.goto(pos[0], pos[1])
        self.t.pendown()
        self.t.circle(self.radius, 270 - self.mouth)

    def advance(self):
        self.mouth += self.direction
        if self.mouth < 0:
            self.direction = -self.direction
        if self.mouth > 60:
            self.direction = -self.direction
        self.draw()
        self.x += 2


# prepare turtle drawing canvas
turtle.bgcolor('black')
t = turtle.Turtle()

# things to make turtle draw fast
t.speed(0)
t.hideturtle()
turtle.tracer(0, 0)

# make two shapes
s1 = PacMan(t)
s1.x = -400
s1.y = -50

s2 = PacMan(t)
s2.x = -300
s2.y = 70
s2.mouth = 20
s2.radius = 68
s2.color = "green"

# advance them across the canvas
for x in range(0, 420):
    t.clear()
    s1.advance()
    s2.advance()
    turtle.update()
    time.sleep(0.005)
