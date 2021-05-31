# Readme iRobot

RobotGraphy Code is implemented to get robot location with provided instructions.

#### Attributes
>  __init__
>  iRobotLoc
>  updateLocation

__init__
takes two argument start and limit
start --> type tuple, to get initial coordinates of Robot
limit --> type tuple, have grid map limit like: 5X4     

iRobotLoc
Return robot location , tuple type
Internally call updateLocation fun

updateLocation
It has main logic to process data and return
robot location.


# Problem Statement :  

Your company iRobot has created a new robot which can follow instructions

The robot can move along a map that is a 2D grid.
The following  5x4 grid will be numbered as follows:


      0  1  2  3  4
    +--+--+--+--+--+
0   |  |  |  |  |  |
    +--+--+--+--+--+
1   |  |  |  |  |  |
    +--+--+--+--+--+
2   |  |  |  |  |  |
    +--+--+--+--+--+
3   |  |  |  |  |  |
    +--+--+--+--+--+


The robot can take 2 types of instructions:
1. Directional instructions - N,E,W,S viz. North, East, West, South
2. Movement instructions - M - which tells it to move 1 step in the direction it is facing

The robot relays its position via a 3  data points - its co-ordinates and the direction it is facing

Coordinates are always in the form row by column - so (2,3) means robot is in the 3rd column of the 2nd row.
For ease of implementation, all grid numbering starts from 0.


      0  1  2  3  4
    +--+--+--+--+--+
0   |  |  |  |  |  |
    +--+--+--+--+--+
1   |  |  |  |  |  |
    +--+--+--+--+--+
2   |  |  |  | R|  |
    +--+--+--+--+--+
3   |  |  |  |  |  |
    +--+--+--+--+--+


For eg: If the robot is on (0,0) in the grid and facing North - it will relay its position as (0,0,N)

Assume the initial position of the robot is (0,0,S) and the grid is 5x4, your program should be able to
take a list of instructions and output the location of the robot after the command is executed

For eg:

COMMAND : MSMMEMM
Robot Location: (3,2,E)

Note:
Robot cannot move beyond the grid coordinates. If it receives a command to move beyond the grid boundaries, it remains stationary.
For eg: If current position of the grid is (3,0,S) and it receives ‘M’ instruction then it will not move as any movement south will cause it go out of the grid.

If Robot gets an instruction to turn in a direction that it already facing, it will not take any action
For eg: If robot is facing North and it gets an 'N' instruction, then it will not take any action

Input will always be command(s)
Output will always be the position of the robot after the command is executed

You are free to use any mode for providing the input - file, command line argument etc.
The output should be printed on the terminal


Please add a readme document to help us run the program
