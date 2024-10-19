import turtle
import math

def draw_fluffy_oval():
    screen = turtle.Screen()
    screen.title("Eid Al Adha")
    screen.bgcolor("green")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(3)
    
    # Write the text "عيد "
    pen.penup()
    pen.goto(220, -50)
    pen.color("white")
    pen.write("عيـــــد", align="center", font=("Arial", 70, "bold"))


    # Draw the fluffy woolish oval body
    pen.penup()
    pen.goto(150, -50)
    pen.pendown()
    pen.color("white")
    pen.seth(90)
    
    
    # Right circles
    for angle in range(0, 180, 30):
        radius = 60 if angle % 60 == 0 else 50
        x = 50 + radius * math.sin(math.radians(angle))
        y = radius * math.cos(math.radians(angle))
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.begin_fill()
        pen.circle(15 + (angle % 60) / 3)  # Varying size circles
        pen.end_fill()

    # Left circles
    for angle in range(180, 360, 30):
        radius = 60 if angle % 60 == 0 else 50
        x = -50 + radius * math.sin(math.radians(angle))
        y = radius * math.cos(math.radians(angle))
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.begin_fill()
        pen.circle(15 + (angle % 60) / 3)  # Varying size circles
        pen.end_fill()

    # Bottom circles
    for x in [-50,-25, 0, 25, 50]:
        pen.penup()
        pen.goto(x, -60)
        pen.pendown()
        pen.begin_fill()
        pen.circle(20)  # Varying size circles
        pen.end_fill()

    # Top circles
    for x in [-50,-25, 0, 25, 50]:
        pen.penup()
        pen.goto(x, 60)
        pen.pendown()
        pen.begin_fill()
        pen.circle(20)  # Varying size circles
        pen.end_fill()

    # Draw and fill the woolish oval body
    pen.penup()
    pen.goto(42, 40)
    pen.pendown()
    pen.begin_fill()
    pen.seth(135)  # Tilt the oval
    for _ in range(2):
        pen.circle(92, 90)  # Half of the oval (width)
        pen.circle(62, 90)  # Half of the oval (height)
    pen.end_fill()


    # Draw the head
    pen.penup()
    pen.goto(70, 90)
    pen.pendown()
    pen.color("lightgray")
    pen.begin_fill()
    pen.circle(55)  # Head circle
    pen.end_fill()

    #The wool piece over his head
    # Draw the central part of the wool
    x_shifting = 30
    y_shifting = 90

    def draw_circle(pen, x, y, radius):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.begin_fill()
        pen.circle(radius)
        pen.end_fill()
        pen.hideturtle()


    def draw_sheep_head():
        pen = turtle.Turtle()
        pen.speed(0)
        pen.width(3)
        pen.color("white")

        # Draw the bottom big circles
        draw_circle(pen, -45 + x_shifting, -15 + y_shifting, 25)
        draw_circle(pen, 0 + x_shifting, -20 + y_shifting, 25)
        draw_circle(pen, 45 + x_shifting, -15 + y_shifting, 25)

        # Draw the top small circles
        draw_circle(pen, -60 + x_shifting, 3 + y_shifting, 19)
        draw_circle(pen, -30 + x_shifting, 10 + y_shifting, 20)
        draw_circle(pen, 0 + x_shifting, 17 + y_shifting, 22)
        draw_circle(pen, 30 + x_shifting, 10 + y_shifting, 20)
        draw_circle(pen, 60 + x_shifting, 3 + y_shifting, 19)

    draw_sheep_head()


    # Ears
    def draw_ear(x, y, angle, outer_radius, inner_radius):
        # Draw outer ear
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color("darkgray")
        pen.seth(angle)
        pen.begin_fill()
        for _ in range(2):
            pen.circle(outer_radius, 90)
            pen.circle(outer_radius // 2, 90)
        pen.end_fill()

        # Draw inner ear
        pen.penup()
        pen.goto(x + 3, y - 5)
        pen.pendown()
        pen.color("pink")
        pen.begin_fill()
        for _ in range(2):
            pen.circle(inner_radius, 90)
            pen.circle(inner_radius // 2, 90)
        pen.end_fill()



    # Draw the left ear
    draw_ear(-15, 90, 175, 30, 20)

    # Draw the right ear
    draw_ear(75, 80, 275, 30, 20)



    # Draw the legs
    def draw_leg(pen, x, y):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color("gray")
        pen.begin_fill()
        for _ in range(2):
            pen.forward(15)
            pen.right(90)
            pen.forward(50)
            pen.right(90)
        pen.end_fill()

        pen.penup()
        pen.goto(x, y - 40)
        pen.pendown()
        pen.color("black")
        pen.begin_fill()
        for _ in range(2):
            pen.forward(15)
            pen.right(90)
            pen.forward(10)
            pen.right(90)
        pen.end_fill()

    def draw_sheep_legs():
        pen = turtle.Turtle()
        pen.speed(0)
        pen.width(3)

        # Draw the legs
        draw_leg(pen, -80, -70)
        draw_leg(pen, -50, -70)
        draw_leg(pen, 0, -70)
        draw_leg(pen, 30, -70)
        pen.hideturtle()


    draw_sheep_legs()




    # The eyes
    def draw_eye(pen, x, y):
    # Draw the outer black part of the eye
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color("black")
        pen.begin_fill()
        pen.circle(10)
        pen.end_fill()

        # Draw the inner white highlight
        pen.penup()
        pen.goto(x - 3, y + 12)
        pen.pendown()
        pen.color("white")
        pen.begin_fill()
        pen.circle(3)
        pen.end_fill()

    def draw_sheep_eyes():
        screen = turtle.Screen()
        screen.title("Sheep Eyes Drawing with Turtle")

        pen = turtle.Turtle()
        pen.speed(0)
        pen.width(3)

        # Draw the eyes
        draw_eye(pen, 10, 45)
        draw_eye(pen, 60, 45)
        pen.hideturtle()

    
    draw_sheep_eyes()



    # Draw the nose and mouth
    pen.penup()
    pen.goto(35, 40)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.circle(5)  # Nose circle
    pen.width(6)
    pen.goto(39, 40)
    pen.forward(15)
    pen.end_fill()
    pen.penup()
    pen.goto(20, 25)
    pen.pendown()
    pen.setheading(-60)
    pen.circle(10, 120)
    pen.penup()
    pen.goto(60, 25)
    pen.pendown()
    pen.setheading(-120)
    pen.circle(-10, 120)

    pen.hideturtle()

    # Write the text "سعيد"
    pen.penup()
    pen.goto(-280, -50)
    pen.color("white")
    pen.write("سعيــــد", align="center", font=("Arial", 70, "bold"))

    screen.mainloop()

draw_fluffy_oval()
