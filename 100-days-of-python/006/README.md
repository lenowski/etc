## Day 6

`Exercise`


### Escaping the Maze 
Reeborg was exploring a dark maze and the battery in its flashlight ran out.[^exercise]

Write a program using an if/elif/else statement so Reeborg can find the exit. 

#### Solution
```python  
def turn_right():
    for i in range(0,3):
        turn_left()
   
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

[^exercise]: [Reborg's World maze exercise.](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Maze&url=worlds/tutorial_en/maze1.json)