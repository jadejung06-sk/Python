from turtle import Turtle # ★
STARTING_POSITIONS = ([0,0], [-20, 0], [-40, 0]) # ★
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake() # ★ 
        self.head = self.segments[0]

    ##### make a snake with some self.new_segments
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        self.new_segment = Turtle()
        self.new_segment.speed("fastest")
        self.new_segment.color('white')
        self.new_segment.shape("square")
        self.new_segment.penup()
        self.new_segment.goto(position)
        self.segments.append(self.new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000) # ★
        self.segments.clear() # ★
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    ##### after reseting

    # def start_snake(self):

    ##### animate the snake
    def move(self):
        for num in range(len(self.segments)-1, 0, -1): # ★
            new_position = self.segments[num -1].position()
            self.segments[num].goto(new_position)
        self.head.forward(MOVE_DISTANCE)
    #############################################

    ##### control the direction
    def up(self):
        if self.head.heading() != DOWN: # ★
            self.head.setheading(UP)  
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    ########################################