import turtle

# The Koch snowflake can be constructed by starting with an equilateral triangle, then recursively altering each line segment as follows:
#
# divide the line segment into three segments of equal length.
# draw an equilateral triangle that has the middle segment from step 1 as its base and points outward.
# remove the line segment that is the base of the triangle from step 2.

def drawTriangle(points, myTurtle):
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])

def getMid(p1, p2):
    return ( (p1[0] + p2[0]) / 3, (p1[1] + p2[1]) / 3)

def koch(points, myTurtle):
    drawTriangle(points, myTurtle)

def draw():
    window = turtle.Screen()
    turtleScreen = turtle.Turtle()
    points = [[-100, -50], [0, 100], [100, -50]]

    koch(points, turtleScreen)
    window.exitonclick()

draw()
