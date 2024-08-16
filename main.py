import time
import turtle
from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("My snake game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkeypress(snake.up,"w")
screen.onkeypress(snake.down,"s")
screen.onkeypress(snake.left,"a")
screen.onkeypress(snake.right,"d")




is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor()<-295 or snake.head.xcor()>295 or snake.head.ycor()<-295 or snake.head.ycor()>295:
        is_game_on=False
        score.game_is_over()

    for t in snake.turtles[1:len(snake.turtles)]:
        if snake.head.distance(t)<10:
            is_game_on=False
            score.game_is_over()


screen.exitonclick()