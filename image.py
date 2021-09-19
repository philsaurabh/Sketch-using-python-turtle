"""A scenery of houses and golden stars in the night drawn by Turtle."""

__author__ = "730401165"

from turtle import Turtle, colormode, bgcolor, done
from random import randint

colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    houses: Turtle = Turtle()
    windows: Turtle = Turtle()
    star: Turtle = Turtle()
    moon: Turtle = Turtle()
    count_one: int = 0
    count_two: int = 0
    count_three: int = 0
    bgcolor(0, 0, 0)
    HOUSES_X: int = -350
    HOUSES_Y: int = -325
    NUMBER_OF_HOUSES: int = 5
    SPACE_BETWEEN_HOUSES: int = 230
    NUMBER_OF_WINDOWS: int = 15
    FIRST_WINDOW_X: int = -340
    FIRST_WINDOW_Y: int = -305
    DISTANCE_IN_BUILDING: int = 55
    DISTANCE_OUTSIDE_BUILDING: int = 175
    MOON_X: int = 270
    MOON_Y: int = 255
    NUMBER_OF_STARS: int = 50
    STAR_X: int = -325
    SPACE_BETWEEN_STARS: int = 13
    while count_one < NUMBER_OF_HOUSES:
        draw_houses(houses, HOUSES_X, HOUSES_Y)
        HOUSES_X += SPACE_BETWEEN_HOUSES
        count_one += 1
    while count_two < NUMBER_OF_WINDOWS:
        draw_windows(windows, FIRST_WINDOW_X, FIRST_WINDOW_Y)
        if (count_two % 2 == 0):
            FIRST_WINDOW_X += DISTANCE_IN_BUILDING
        if (count_two % 2 == 1):
            FIRST_WINDOW_X += DISTANCE_OUTSIDE_BUILDING
        count_two += 1
    while count_three < NUMBER_OF_STARS:
        STAR_Y: int = randint(85, 300)
        draw_star(star, STAR_X, STAR_Y)
        STAR_X += SPACE_BETWEEN_STARS
        count_three += 1
    draw_moon(moon, MOON_X, MOON_Y)
    done()


def draw_gray_rectangle(turtle: Turtle, height: int, width: int) -> None:
    """Draws gray rectangles that will become skyscrapers."""
    i: int = 0
    turtle.color(100, 239, 49)
    turtle.begin_fill()
    while(i < 2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        i = i + 1
    turtle.end_fill()
    turtle.hideturtle()
        

def draw_houses(building: Turtle, x: float, y: float) -> None:
    """Draws the skyscrapers using draw_gray_rectangle."""
    building.penup()
    building.goto(x, y)
    building.setheading(0.0)
    building.pendown()
    HEIGHT: int = 140
    WIDTH: int = 120
    draw_gray_rectangle(building, HEIGHT, WIDTH)


def draw_moon(luna: Turtle, x: float, y: float) -> None:
    """Draws a light-yellow circle using the turtle.circle method."""
    luna.penup()
    luna.goto(x, y)
    luna.setheading(0.0)
    luna.pendown()
    luna.pencolor("white")
    luna.fillcolor(222, 219, 82)
    RADIUS: int = 40
    luna.begin_fill()
    luna.circle(RADIUS)
    luna.end_fill()
    luna.hideturtle()


def draw_diamond(diamond: Turtle, length: int) -> None:
    """Draws golden diamonds that will become stars."""
    i: int = 0
    MAX_SPEED: int = 0
    diamond.pencolor("white")
    diamond.speed(MAX_SPEED)
    diamond.fillcolor(222, 219, 82)
    diamond.begin_fill()
    while (i < 2):
        diamond.forward(length)
        diamond.left(145)
        diamond.forward(length)
        diamond.left(35)
        i += 1
    diamond.end_fill()
    diamond.hideturtle()


def draw_star(astro: Turtle, x: float, y: float) -> None:
    """Draws golden diamonds using random integers as angles and size."""
    TILT: int = randint(0, 180)
    SIDE_LENGTH: int = randint(5, 12)
    astro.penup()
    astro.goto(x, y)
    astro.setheading(TILT)
    """By making the setheading and side length of the stars 
    random through the randint TINT and randint SIDE_LENGTH, 
    I could make each star unique in angles, size, and placement
    (shown in line 47) like a real night sky.""" 
    astro.pendown()
    draw_diamond(astro, SIDE_LENGTH)


def draw_white_rectangle(turtle: Turtle, height: int, width: int) -> None:
    """Draws white rectangles that will become windows."""
    i: int = 0
    turtle.color("white")
    turtle.begin_fill()
    while(i < 2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        i = i + 1
    turtle.end_fill()
    turtle.hideturtle()


def draw_windows(glass: Turtle, x: float, y: float) -> None:
    """Draws white windows on each of the 3 skyscrapers."""
    glass.penup()
    glass.goto(x, y)
    glass.setheading(0.0)
    glass.pendown()
    HEIGHT: int = 60
    WIDTH: int = 45
    draw_white_rectangle(glass, HEIGHT, WIDTH)

    
if __name__ == "__main__":
    main()