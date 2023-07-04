from turtle import Turtle,Screen
import pandas as pd
from go_place import Place


screen = Screen()
turtle = Turtle()

screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
length = len(data["state"])
state_list = data["state"].to_list()
place = Place()

def question():
    count = 1
    result = 0
    flage = True
    remaning = []

    while count != length and flage:

        answer = screen.textinput(f"Guess the state {result}/50","What the next state? ")
        new_answer = answer.title()
        remaning.append(new_answer)

        if new_answer in state_list:
            state = data[data["state"] == f"{new_answer}"]
            x_axis = state.x
            y_axis = state.y
            place.go(x_axis,y_axis,new_answer)
            result += 1
        elif new_answer == "Exit":
            flage = False
        else:
            continue
        count += 1

    if not flage:
        # for names in remaning:
        #     if names in state_list:
        #         state_list.remove(f"{names}")
        new_state_list = [states for states in state_list if states not in remaning]
        print("this...",new_state_list)
        state_dict = pd.DataFrame({'state':new_state_list})
        state_dict.to_csv("new.csv")
        place.remain_state(state_dict)

question()


screen.listen()
screen.exitonclick()