from turtle import Turtle, Screen
import random

colors = ['purple' , 'blue' , 'green' , 'yellow' , 'orange' , 'red']
all_turtles = []
screen = Screen()
screen.setup(width=500 , height=400)
user_bet = screen.textinput(title='Make your bet' , prompt="Which turtle will cross the line first? ")


# making multiple turtles
for i in range(len(colors)):
    new_turtles = Turtle(shape='turtle')
    new_turtles.penup()
    new_turtles.color(colors[i])
    new_turtles.goto(-240 , -100 + (30 * i))
    all_turtles.append(new_turtles)

# print(all_turtles[0].pencolor())
is_race_over = False
winner = ''
while not is_race_over:

    finish_line = 210

    for turtle in all_turtles:
        rand_num = random.randint(0,10)
        turtle.fd(rand_num)

        # print(f'{turtle.pencolor()} {turtle.xcor()}')
        if turtle.xcor() >= finish_line:
            winner = turtle.pencolor()
            is_race_over = True
            break

if user_bet == winner:
    print(f'You won the bet. The winner is {winner} Turtle.')
else:
    print(f'Sorry! You lost the bet the winner is {winner} Turtle.')
screen.exitonclick()