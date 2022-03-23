'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################

my_turtle=turtle.Turtle()

def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  myturtle.up()
  myturtle.goto(top_left_x, top_left_y)
  my_turtle.down()
  for i in range(0,4):
    myturtle.forward(width)
    myturtle.right(90)

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  myturtle.up()
  myturtle.goto(x_start,0)
  myturtle.down()
  myturtle.goto(x_end,0)
  myturtle.up()
  myturtle.goto(0,y_start)
  myturtle.down()
  myturtle.goto(0,y_end)

def drawCircle(myturtle=None, radius=0):
  myturtle.up()
  myturtle.goto(0,-1)
  myturtle.down()
  myturtle.circle(radius, steps=360)

def setUpDartboard(mywindow=None,myturtle=None):
  mywindow.setworldcoordinates(-1,-1,1,1)
  drawSquare(myturtle=myturtle, width=2, top_left_x=- 
  -1, top_left_y=1)
  drawLine(myturtle=myturtle, x_start=-1, y_start=0, 
  x_end=1,y_end=0)
  drawLine(myturtle=myturtle, x_start=0, y_start=-1, x_end=0, y_end=1)
  drawCircle(myturtle=myturtle, radius=1)

def isInCircle(myturtle=None, circle_center_x=0,circle_center_y=0, radius=0):
  distance= myturtle.distance(circle_center_x, circle_center_y)
  return(bool(distance<=radius))

def throwDart(myturtle=None):
  myturtle.up()
  x=random.uniform(-1,1)
  y=random.uniform(-1,1)
  myturtle.goto(x,y)
  if isInCircle(myturtle=myturtle, circle_center_x=0, circle_center_y=0, radius=1):
    myturtle.color("blue")
  else:
    myturtle.color("orange")
  myturtle.down()
  myturtle.dot()
  myturtle.color("red")

def playDarts(myturtle=None):
  playerapoints=0
  playerbpoints=0
  for i in range(0,10):
    throwDart(myturtle=myturtle)
    if isInCircle(myturtle=myturtle, circle_center_x=0, circle_center_y=0, radius=1):
      playerapoints= playerapoints +1
    throwDart(myturtle=myturtle)
    if isInCircle(myturtle=myturtle,circle_center_x=0, circle_center_y=0, radius=1):
      playerbpoints=playerbpoints +1
    if playerapoints > playerbpoints:
      print("Player A is the winner!")
    else:
      if playerapoints < playerbpoints:
        print("Player B is the winner!")
      else:
        print("Player A and B have tied!")

def montePi(myturtle=None, num_darts=0):
  inside_count=0
  outside_count=0
  for i in range(0, num_darts):
    throwDart(myturtle=myturtle)
  if isInCircle(myturtle=myturtle, circle_center_x=0, circle_center_y=0, radius=1):
   inside_count = outside_count +1
  return((inside_count/num_darts)*4)

    
#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
