# Project Title
Circular Garden
## Description 
 This program calculates the area, circumference, square root, and the area rounded up down to use for the making for a circular garden using the given radius input of the user.
## How to run
 Please click the "run program button of your IDE, and when prompted, input your radius that you want to use.
## Input Needed
 You can use any positive number (For the following Sample Output, I will use 5)
# Sample Output
Enter radius 5

Area of the garden: 78.54

Circumference  of the garden: 31.42

Square root of the area: 8.86

Area rounded down: 78 square meters

Area rounded up: 79 square meters

## Problem Identification
The School plans to create a circular garden, Develop a Python Program  that will help determine information based on a radius entered by the user.
## Problem Decomposition
Use Math Library to calculate for the needed values

Collect users input value (radius)

Use math.pi, math.sqrt, math.floor, and math.ceil

Print the processed values

## Pattern Recognition
repeatedly using math functions (like math.pi, math.sqrt, etc..)

using print to output the processed values

using .2f to reduce the value's decimal places to a maximum of 2 decimal places.

repeatedly using area to calculate for sqrt, rounded up/down

## Data Representation

Variable names: radius(for user inputted radius)

area

circ(CIRCUMFERENCE PROCESSED)

sqrt(square root)

rounded_down

rounded_up

## Algorithm Development
## PSEUDO CODE ( python to pseudo code converter used, Sir you allowed this. )

START
    
    // Collect the radius value inputted by the user
    DISPLAY "Enter radius: "
    INPUT radius
    
    // Calculate the different values
    SET area TO pi * (radius squared)
    SET circ TO 2 * pi * radius
    SET sqrt TO SQUARE_ROOT(area)
    SET rounded_down TO ROUND_DOWN(area)
    SET rounded_up TO ROUND_UP(area)
    
    // Output the calculated results rounded to 2 decimal places
    DISPLAY "Area of the garden: ", area, " square meters"
    DISPLAY "Circumference of the garden: ", circ, " meters"
    DISPLAY "Square root of the area: ", sqrt
    DISPLAY "Area rounded down: ", rounded_down, " square meters"
    DISPLAY "Area rounded up: ", rounded_up, " square meters"

END

## Author

8-Adelfa

John Owen D. Depidep



