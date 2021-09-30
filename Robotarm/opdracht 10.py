from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
aantalMoves = 11
for l in range(5):
    aantalMoves = aantalMoves - 2
    robotArm.grab()
    for i in range(0,aantalMoves):
        robotArm.moveRight()
    robotArm.drop()
    for f in range(0,aantalMoves -1):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()