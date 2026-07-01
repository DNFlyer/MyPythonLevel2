import turtle
import random
import time

def play_game():
    
#Snake Head
    t = turtle.Turtle()
    t.shape('triangle')
    t.color("red")
    t.penup()
    t.goto(0, 0)

#Trail
    t.pendown()
    t.pencolor("white")
    t.pensize(3)

#Food

        ### Number of FOOD ARTICLES - CAN CHANGE THE VALUE OF LINE 23 ###

    No_Of_Foods = 10    # <--- CAN CHANGE VALUE
    List_Of_Foods = []
    Caught_Food = [False] * No_Of_Foods
    My_Segments = []

    for kk in range(No_Of_Foods):
        Food = turtle.Turtle()
        Food.penup()
        Food.speed(0)
        Food.shape("square")
        Food.color("blue")
        Food.goto(random.randint(-200, 200), random.randint(-200, 200))
        List_Of_Foods.append(Food)

#Score=Board
    Pen = turtle.Turtle()
    Pen.penup()
    Pen.goto(180, 180)
    Pen.color("cyan")
    Pen.ht()

#Report of performace
    User_Report = turtle.Turtle()
    User_Report.penup()
    User_Report.goto(0, 0)
    User_Report.color("cyan")
    User_Report.ht()

    steps = 0
    start_time = time.time()
    game_over = False

#Direction controlling
    t.setheading(0) #First look right, because it is the "right" direction, get it? haha

    def right():
        if t.heading() != 180:  #NO 180 degree turn allowed
            t.setheading(0)

    def left():
        if t.heading() != 0:
            t.setheading(180)

    def up():
        if t.heading() != 270:
            t.setheading(90)

    def down():
        if t.heading() != 90:
            t.setheading(270)

    ts = t.screen
    ts.bgcolor("black")
    ts.onkey(right, "Right")
    ts.onkey(left, "Left")
    ts.onkey(up, "Up")
    ts.onkey(down, "Down")
    ts.listen()

    while not game_over:
        steps += 1
        Pen.write(len(My_Segments) , align="center" , font=("Areal", 24, "normal"))

        #Collecting Food - check collision of snake with food
        for kk in range(len(List_Of_Foods)):
            if not Caught_Food[kk]:
                if t.distance(List_Of_Foods[kk]) < 20:
                    Caught_Food[kk] = True
                    List_Of_Foods[kk].color('green')
                    My_Segments.append(List_Of_Foods[kk])
                    Pen.clear()

        #Move body of snake
        for index in range(len(My_Segments) - 1, 0, -1):
            x = My_Segments[index - 1].xcor()
            y = My_Segments[index - 1].ycor()
            My_Segments[index].goto(x, y)

        if len(My_Segments) > 0:
            My_Segments[0].goto(t.xcor(), t.ycor())

        ### SPEED OF SNAKE - CAN CHANGE THIS VALUE ###

        #Move snake head by PIXELS
        t.forward(20)

        for seg in My_Segments:
            if seg.distance(t) < 5: #Check collision distance - SET at 5 pixels
                game_over = True
                time.sleep(1)
                t.clear()
                t.ht()
                for s in My_Segments:
                    s.ht()
                elapsed = int(time.time() - start_time)
                User_Report.write(f"Game Over! Snake hit itself. Steps: {steps}  Time: {elapsed}s",
                                  align="center", font=("Courier", 24, "normal"))

        #Check if everything eaten and snake back at center
        if len(My_Segments) == No_Of_Foods:
            if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
                game_over = True
                time.sleep(1)
                t.clear()
                t.ht()
                for seg in My_Segments:
                    seg.ht()
                elapsed = int(time.time() - start_time)
                User_Report.write(f"Steps Taken: {steps}  Time: {elapsed}s",
                                  align="center", font=("Courier", 24, "normal"))

        time.sleep(0.1)  #Snake update speed

#Trial UI - fixed
#Ask user if they want to play again
while True:
    play_game()
    choice = turtle.textinput("Play Again?", "Type 'yes' to play again or 'no' to exit :")
    if choice is None or choice.lower() != "yes" :
        break

turtle.exitonclick() #User can click on window to exit. Can also click cancel