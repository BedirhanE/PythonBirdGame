
import random
import turtle,time
pencere =turtle.Screen()
pencere.title("flappy Bird ")
pencere.bgcolor("blue")
pencere.bgpic("background.gif")
pencere.setup(width=600 , height=680)
pencere.tracer(0)


pencere.register_shape("bird.gif")

bird = turtle.Turtle()
bird.speed(0)
bird.color("yellow")
bird.shape("bird.gif")
bird.penup()
bird.goto(-180,0)
bird.dx=0
bird.dy=1

puan = 100
yaz = turtle.Turtle()
yaz.speed(0)
yaz.color("black")
yaz.shape("square")
yaz.hideturtle()
yaz.penup()
yaz.goto(0,280)
yaz.write("Puan: {} ".format(puan), align ="center",font =("Courier",24,"bold"))


yercekimi = -0.3

def bird_up(x,y):
    bird.dy = bird.dy + 8

    if bird.dy >8:
         bird.dy = 8

borular = []

pencere.listen()
pencere.onscreenclick(bird_up)

starting_time =time.time()
while True :

    time.sleep(0.02)
    pencere.update()

    bird.dy = bird.dy + yercekimi

    if(time.time()-starting_time> random.randint(5,15)):
        starting_time = time.time()
        ust_boru = turtle.Turtle()
        ust_boru.speed(0)
        ust_boru.color("red")
        ust_boru.shape("square")
        ust_boru.h=random.randint(10,20)
        ust_boru.shapesize(ust_boru.h, 2, outline=None)
        ust_boru.penup()
        ust_boru.goto(300, 250)
        ust_boru.dx = -2
        ust_boru.dy = 0

        alt_boru = turtle.Turtle()
        alt_boru.speed(0)
        alt_boru.color("red")
        alt_boru.shape("square")
        alt_boru.h = 40 - ust_boru.h - random.randint(1,10)
        alt_boru.shapesize(alt_boru.h, 2, outline=None)
        alt_boru.penup()
        alt_boru.goto(300, -250)
        alt_boru.dx = -2
        alt_boru.dy = 0

        borular.append((ust_boru,alt_boru))

    y = bird.ycor()
    y = y + bird.dy
    bird.sety(y)

    if len(borular) > 0 :
      for boru in  borular:
       x = boru[0].xcor()
       x = x + boru[0].dx
       boru[0].setx(x)
       x = boru[1].xcor()
       x = x + boru[1].dx
       boru[1].setx(x)
       if boru[0].xcor()<-300:
           boru[0].hideturtle()
           boru[1].hideturtle()
           borular.pop(borular.index((boru)))
       if (bird.xcor()+10>boru[0].xcor()-20) and (bird.xcor()-10>boru[0].xcor()+20):
           if (bird.ycor()+10>boru[0].ycor()-boru[0].h*10) or (bird.ycor()-10<boru[1].ycor()+boru[1].h*10):
               puan = puan - 1
               yaz.clear()
               yaz.write("Puan: {} ".format(puan), align="center", font=("Courier", 24, "bold"))

    if puan < 0:
        yaz.clear()
        yaz.write(" KAYBETTİNİZ :( ", align="center", font=("Courier", 24, "bold"))
