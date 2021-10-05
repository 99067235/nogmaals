from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 4
value = 0
for f in range(10):
    robotArm.moveRight()
for i in range(10):
    robotArm.grab()
    color = robotArm.scan()
    value +=1
    if color == "red":
            for g in range(10):
                robotArm.moveRight()
            robotArm.drop()
            for u in range(0,value):
                robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()