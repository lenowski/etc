"""
Test your knowledge of US geography by guessing the names of each state on a map.

Instructions:
- Enter the name of a US state when prompted.
- A map will appear with the correct states marked.
- Continue until all the states are correctly guessed, or type 'Exit' to end the game
  and generate a 'missed_states.csv' file.
"""

import turtle

import pandas as pd

IMAGE = "src/us_states_game/assets/states__map.gif"
DATA = "src/us_states_game/assets/states__data.csv"


def main():
    # Set up turtle screen and shape
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(IMAGE)
    turtle.shape(IMAGE)

    # Load U.S. states data
    data = pd.read_csv(DATA)
    states_list = data.state.to_list()
    states_count = len(data)
    guessed_states = []

    while len(guessed_states) < states_count:
        answer_state = screen.textinput(
            title=f"{len(guessed_states)}/{len(states_list)} States Correct",
            prompt="What's another state's name?",
        ).title()

        # Exit the game and save missed states if user types "Exit"
        if answer_state == "Exit":
            missed_states = [
                state for state in states_list if state not in guessed_states
            ]
            pd.Series(missed_states).to_csv("missed_states.csv")
            break

        # Check if the guessed state is correct
        if answer_state in states_list:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(float(state_data.x), float(state_data.y))
            t.write(answer_state)
            guessed_states.append(answer_state)

    turtle.bye()


if __name__ == "__main__":
    main()
