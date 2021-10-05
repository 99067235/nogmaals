from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
aantalMoves = 0

for i in range (9):
    robotArm.grab()
    value = robotArm.scan()
    if value == "":
        break
    else:
        aantalMoves +=1
        for u in range(0,aantalMoves,1):
            robotArm.moveRight()
        robotArm.drop()
        for e in range(0,aantalMoves,1):
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()