
def moveOneDisk(height, pole1, pole2, pole3):
    if height >= 1:
        moveDisk(pole1, pole3)

def moveThreeDisks(height, pole1, pole2, pole3):
    if height >= 1:
        moveThreeDisks(height-1, pole1, pole3, pole2)
        print('Moving disk from', pole1, 'to', pole2)
        moveThreeDisks(height-1, pole3, pole2, pole1)

moveThreeDisks(3, 'A', 'B', 'C')

def moveTwoDisks(height, pole1, pole2, pole3):
    if height >= 1:
        moveTwoDisks(height-1, pole1, pole3, pole2)
        print('Moving disk from', pole1, 'to', pole2)
        moveTwoDisks(height-1, pole3, pole2, pole1)
