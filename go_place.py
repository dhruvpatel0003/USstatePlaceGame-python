from turtle import Turtle,Screen

class Place:

    def go(self,x,y,answer):
        new = Turtle()
        new.hideturtle()
        new.penup()
        new.goto(int(x), int(y))
        new.write(f"{answer}")

    def remain_state(self,states):
        Screen().clear()
        new = Turtle()
        new.hideturtle()
        new.penup()
        Screen().setup(200,800)
        new.goto(0,-380)
        new.write(f"Remaining states are : \n\n {states}", align="center",font=("Arial", 9, "normal"))

