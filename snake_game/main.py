from turtle import Screen, Turtle
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(n = 2)

##### make a snake with some segments
starting_position = ([0,0], [-20, 0], [-40, 0])
segments = []
for position in starting_position:
    new_segment = Turtle()
    new_segment.speed("fastest")
    new_segment.color('white')
    new_segment.shape("square")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()


game_is_on = True
while game_is_on:
    for segment in segments:
        segment.speed("fastest")
        segment.forward(5)










screen.exitonclick()