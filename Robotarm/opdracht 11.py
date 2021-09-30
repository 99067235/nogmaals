from pygame import Color
from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

robotArm.speed = 3

# Jouw python instructies zet je vanaf hier:

for f in range(10):
    robotArm.moveRight()
for i in range(10):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()