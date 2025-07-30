import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # When player cross the wall it strat from previous position
    if player.ycor() > 280:
        player.reset()
        scoreboard.level_up()
        scoreboard.update_score()
        car_manager.increase_speed()

    # When player collision with cars the game is over there
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            screen.exitonclick()


