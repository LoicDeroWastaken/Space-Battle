### main program of LTL (Louis Tom Loïc) SPACE BATTLE Inc. ###

from datetime import datetime, timedelta
import os

### VALUES ###

alphaColumns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numLines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
completeBoard = []
ships = ["SpaceCruiser", "USS Enterprise", "X-Wing",
         "Millenium Falcon", "Stellair Destroyer"]
teamBluePos = {}
teamRedPos = {}
bluetouchedPositions = []
bluemissedPositions = []
redtouchedPositions = []
redmissedPositions = []
teamBlueTurn = True
teamRedTurn = False

### FUNCTIONS ###


def start():
    '''the function that initalize the game board'''

    print("\n\n\n")
    for a in alphaColumns:
        for i in numLines:
            case = a + str(i)
            completeBoard.append(case)
    if len(completeBoard) == 100:
        print("#SPACE BATTLE# : the game board is fully charged, welcome in the new Space Battle ! Enjoy the game !\n")
        team_blue_init()
        team_red_init()
        time_check()
        # winner_def()
    else:
        print("#SPACE BATTLE ERROR# : an error occured, the program will restart.")
        start()


def team_blue_init():
    '''the function that place the blue team ships'''

    imp = input(
        "#SPACE BATTLE# : Please press [ENTER] to skip to the BLUE TEAM configuration...\n")
    if imp:
        print("#SPACE BATTLE ERROR# : an error occurred, please retry.\n")
        team_blue_init()
    else:
        # print("#!SPACE BATTLE NOTICE!# : Please refer to the notice on the right top of your screen for the ship placement.\n")
        print("#SPACE BATTLE BLUE TEAM# : BLUE team, it's your turn to choose your ships positions !\n")
        for sh in ships:
            if sh == "SpaceCruiser":
                coorda, coordb = input(
                    "#SPACE BATTLE BLUE TEAM# : BLUE team, enter the 2 coordinates of your SpaceCruiser with a "
                    "space between them :\n").split()
                pos1 = coorda.upper()
                pos2 = coordb.upper()
                if coorda and coordb:
                    if completeBoard.count(pos1) and completeBoard.count(pos2):
                        if pos1 != pos2:
                            print(
                                "#SPACE BATTLE BLUE TEAM# : Location of your ship saved !\n")
                            fullcoord = []
                            fullcoord.append(pos1)
                            fullcoord.append(pos2)
                            teamBluePos[sh] = fullcoord
                            continue
                        else:
                            print(
                                "#SPACE BATTLE ERROR# : You entered the two same cases, the placement choice will restart.")
                            team_blue_init()
                    else:
                        print(
                            "#SPACE BATTLE ERROR# : At least one of the position is not on the board, the placement choice will restart.")
                        team_blue_init()
                else:
                    print(
                        "#SPACE BATTLE ERROR# : An error occurred, or missing one postion, the placement choice will restart.")
                    team_blue_init()
            if sh == "USS Enterprise":
                coorda, coordb, coordc = input(
                    "#SPACE BATTLE BLUE TEAM# : BLUE team, enter the 3 coordinates of your USS "
                    "Enterprise with a space between them:\n").split()
                pos1 = coorda.upper()
                pos2 = coordb.upper()
                pos3 = coordc.upper()
                if coorda and coordb and coordc:
                    if completeBoard.count(pos1) and completeBoard.count(
                            pos2) and completeBoard.count(pos3):
                        if pos1 != pos2 and pos1 != pos3 and pos2 != pos3:
                            print(
                                "#SPACE BATTLE BLUE TEAM# : Location of your ship saved !\n")
                            fullcoord = []
                            fullcoord.append(pos1)
                            fullcoord.append(pos2)
                            fullcoord.append(pos3)
                            teamBluePos[sh] = fullcoord
                            continue
                        else:
                            print(
                                "#SPACE BATTLE ERROR# : You entered at least two same cases, the placement choice will restart.")
                            team_blue_init()
                    else:
                        print(
                            "#SPACE BATTLE ERROR# : At least one of the position is not on the board, the placement choice will restart.")
                        team_blue_init()
                else:
                    print(
                        "#SPACE BATTLE ERROR : An error occurred, or missing one postion, the placement choice will restart.")
                    team_blue_init()

            if sh == "X-Wing":
                coorda, coordb, coordc = input(
                    "#SPACE BATTLE BLUE TEAM# : BLUE team, enter the 3 coordinates of your X-"
                    "Wing with a space between them:\n").split()
                pos1 = coorda.upper()
                pos2 = coordb.upper()
                pos3 = coordc.upper()
                if coorda and coordb and coordc:
                    if completeBoard.count(pos1) and completeBoard.count(
                            pos2) and completeBoard.count(pos3):
                        if pos1 != pos2 and pos1 != pos3 and pos2 != pos3:
                            print(
                                "#SPACE BATTLE BLUE TEAM# : Location of your ship saved !\n")
                            fullcoord = []
                            fullcoord.append(pos1)
                            fullcoord.append(pos2)
                            fullcoord.append(pos3)
                            teamBluePos[sh] = fullcoord
                            continue
                        else:
                            print(
                                "#SPACE BATTLE ERROR# : You entered at least two same cases, the placement choice will restart.")
                            team_blue_init()
                    else:
                        print(
                            "#SPACE BATTLE ERROR# : At least one of the position is not on the board, the placement choice will restart.")
                        team_blue_init()
                else:
                    print(
                        "#SPACE BATTLE ERROR : An error occurred, or missing one postion, the placement choice will restart.")
                    team_blue_init()

            if sh == "Millenium Falcon":
                coorda, coordb, coordc, coordd = input(
                    "#SPACE BATTLE BLUE TEAM# : BLUE team, enter the 4 coordinates of your Millenium "
                    "Falcon with a space between them:\n").split()
                pos1 = coorda.upper()
                pos2 = coordb.upper()
                pos3 = coordc.upper()
                pos4 = coordd.upper()
                if coorda and coordb and coordc and coordd:
                    if completeBoard.count(pos1) and completeBoard.count(
                            pos2) and completeBoard.count(pos3) and completeBoard.count(pos4):
                        if pos1 != pos2 and pos1 != pos3 and pos1 != pos4 and pos2 != pos3 and pos2 != pos4 and pos3 != pos4:
                            print(
                                "#SPACE BATTLE BLUE TEAM# : Location of your ship saved !\n")
                            fullcoord = []
                            fullcoord.append(pos1)
                            fullcoord.append(pos2)
                            fullcoord.append(pos3)
                            fullcoord.append(pos4)
                            teamBluePos[sh] = fullcoord
                            continue
                        else:
                            print(
                                "#SPACE BATTLE ERROR# : You entered at least two same cases, the placement choice will restart.")
                            team_blue_init()
                    else:
                        print(
                            "#SPACE BATTLE ERROR# : At least one of the position is not on the board, the placement choice will restart.")
                        team_blue_init()
                else:
                    print(
                        "#SPACE BATTLE ERROR : An error occurred, or missing one postion, the placement choice will restart.")
                    team_blue_init()

            if sh == "Stellair Destroyer":
                coorda, coordb, coordc, coordd, coorde = input(
                    "#SPACE BATTLE BLUE TEAM# : BLUE team, enter the 5 coordinates of your Stellair "
                    "Destroyer with a space between them:\n").split()
                pos1 = coorda.upper()
                pos2 = coordb.upper()
                pos3 = coordc.upper()
                pos4 = coordd.upper()
                pos5 = coorde.upper()
                if coorda and coordb and coordc and coordd and coorde:
                    if completeBoard.count(pos1) and completeBoard.count(
                            pos2) and completeBoard.count(pos3) and completeBoard.count(pos4) and completeBoard.count(pos5):
                        if pos1 != pos2 and pos1 != pos3 and pos1 != pos4 and pos1 != pos5 and pos2 != pos3 and pos2 != pos4 and pos2 != pos5 and pos3 != pos4 and pos3 != pos5 and pos4 != pos5:
                            print(
                                "#SPACE BATTLE BLUE TEAM# : Location of your ship saved !\n")
                            fullcoord = []
                            fullcoord.append(pos1)
                            fullcoord.append(pos2)
                            fullcoord.append(pos3)
                            fullcoord.append(pos4)
                            fullcoord.append(pos5)
                            teamBluePos[sh] = fullcoord
                            continue
                        else:
                            print(
                                "#SPACE BATTLE ERROR# : You entered at least two same cases, the placement choice will restart.")
                            team_blue_init()
                    else:
                        print(
                            "#SPACE BATTLE ERROR# : At least one of the position is not on the board, the placement choice will restart.")
                        team_blue_init()
                else:
                    print(
                        "#SPACE BATTLE ERROR : An error occurred, or missing one postion, the placement choice will restart.")
                    team_blue_init()


def team_red_init():
    '''the function that place the red team ships'''

    imp = input(
        "#SPACE BATTLE# : Please press [ENTER] to skip to the RED TEAM configuration...\n")
    if imp:
        print("#SPACE BATTLE ERROR# : an error occurred, please retry.\n")
        team_red_init()
    else:
        # print("#!SPACE BATTLE NOTICE!# : Please refer to the notice on the right top of your screen for the ship placement.\n")
        print("#SPACE BATTLE BLUE TEAM# : RED team, it's your turn to choose your ships positions !\n")
        for sh in ships:
            if sh == "SpaceCruiser":
                coorda, coordb = input(
                    "#SPACE BATTLE RED TEAM# : RED team, enter the 2 coordinates of your SpaceCruiser with a "
                    "space between them :\n").split()
                pos1 = coorda.upper()
                pos2 = coordb.upper()
                if coorda and coordb:
                    if completeBoard.count(pos1) and completeBoard.count(pos2):
                        if pos1 != pos2:
                            print(
                                "#SPACE BATTLE RED TEAM# : Location of your ship saved !\n")
                            fullcoord = []
                            fullcoord.append(pos1)
                            fullcoord.append(pos2)
                            teamRedPos[sh] = fullcoord
                            continue
                        else:
                            print(
                                "#SPACE BATTLE ERROR# : You entered the two same cases, the placement choice will restart.")
                            team_red_init()
                    else:
                        print(
                            "#SPACE BATTLE ERROR# : At least one of the position is not on the board, the placement choice will restart.")
                        team_red_init()
                else:
                    print(
                        "#SPACE BATTLE ERROR# : An error occurred, or missing one postion, the placement choice will restart.")
                    team_red_init()

            if sh == "USS Enterprise":
                coorda, coordb, coordc = input(
                    "#SPACE BATTLE RED TEAM# : RED team, enter the 3 coordinates of your USS "
                    "Enterprise with a space between them:\n").split()
                pos1 = coorda.upper()
                pos2 = coordb.upper()
                pos3 = coordc.upper()
                if coorda and coordb and coordc:
                    if completeBoard.count(pos1) and completeBoard.count(
                            pos2) and completeBoard.count(pos3):
                        if pos1 != pos2 and pos1 != pos3 and pos2 != pos3:
                            print(
                                "#SPACE BATTLE RED TEAM# : Location of your ship saved !\n")
                            fullcoord = []
                            fullcoord.append(pos1)
                            fullcoord.append(pos2)
                            fullcoord.append(pos3)
                            teamRedPos[sh] = fullcoord
                            continue
                        else:
                            print(
                                "#SPACE BATTLE ERROR# : You entered at least two same cases, the placement choice will restart.")
                            team_red_init()
                    else:
                        print(
                            "#SPACE BATTLE ERROR# : At least one of the position is not on the board, the placement choice will restart.")
                        team_red_init()
                else:
                    print(
                        "#SPACE BATTLE ERROR : An error occurred, or missing one postion, the placement choice will restart.")
                    team_red_init()

            if sh == "X-Wing":
                coorda, coordb, coordc = input("#SPACE BATTLE RED TEAM# : RED team, enter the 3 coordinates of your X-"
                                               "Wing with a space between them:\n").split()
                pos1 = coorda.upper()
                pos2 = coordb.upper()
                pos3 = coordc.upper()
                if coorda and coordb and coordc:
                    if completeBoard.count(pos1) and completeBoard.count(
                            pos2) and completeBoard.count(pos3):
                        if pos1 != pos2 and pos1 != pos3 and pos2 != pos3:
                            print(
                                "#SPACE BATTLE RED TEAM# : Location of your ship saved !\n")
                            fullcoord = []
                            fullcoord.append(pos1)
                            fullcoord.append(pos2)
                            fullcoord.append(pos3)
                            teamRedPos[sh] = fullcoord
                            continue
                        else:
                            print(
                                "#SPACE BATTLE ERROR# : You entered at least two same cases, the placement choice will restart.")
                            team_red_init()
                    else:
                        print(
                            "#SPACE BATTLE ERROR# : At least one of the position is not on the board, the placement choice will restart.")
                        team_red_init()
                else:
                    print(
                        "#SPACE BATTLE ERROR : An error occurred, or missing one postion, the placement choice will restart.")
                    team_red_init()

            if sh == "Millenium Falcon":
                coorda, coordb, coordc, coordd = input(
                    "#SPACE BATTLE RED TEAM# : RED team, enter the 4 coordinates of your "
                    "Millenium "
                    "Falcon with a space between them:\n").split()
                pos1 = coorda.upper()
                pos2 = coordb.upper()
                pos3 = coordc.upper()
                pos4 = coordd.upper()
                if coorda and coordb and coordc and coordd:
                    if completeBoard.count(pos1) and completeBoard.count(
                            pos2) and completeBoard.count(pos3) and completeBoard.count(pos4):
                        if pos1 != pos2 and pos1 != pos3 and pos1 != pos4 and pos2 != pos3 and pos2 != pos4 and pos3 != pos4:
                            print(
                                "#SPACE BATTLE RED TEAM# : Location of your ship saved !\n")
                            fullcoord = []
                            fullcoord.append(pos1)
                            fullcoord.append(pos2)
                            fullcoord.append(pos3)
                            fullcoord.append(pos4)
                            teamRedPos[sh] = fullcoord
                            continue
                        else:
                            print(
                                "#SPACE BATTLE ERROR# : You entered at least two same cases, the placement choice will restart.")
                            team_red_init()
                    else:
                        print(
                            "#SPACE BATTLE ERROR# : At least one of the position is not on the board, the placement choice will restart.")
                        team_red_init()
                else:
                    print(
                        "#SPACE BATTLE ERROR : An error occurred, or missing one postion, the placement choice will restart.")
                    team_red_init()

            if sh == "Stellair Destroyer":
                coorda, coordb, coordc, coordd, coorde = input(
                    "#SPACE BATTLE RED TEAM# : RED team, enter the 5 coordinates of your Stellair "
                    "Destroyer with a space between them:\n").split()
                pos1 = coorda.upper()
                pos2 = coordb.upper()
                pos3 = coordc.upper()
                pos4 = coordd.upper()
                pos5 = coorde.upper()
                if coorda and coordb and coordc and coordd and coorde:
                    if completeBoard.count(pos1) and completeBoard.count(
                        pos2) and completeBoard.count(pos3) and completeBoard.count(pos4) and completeBoard.count(
                            pos5):
                        if pos1 != pos2 and pos1 != pos3 and pos1 != pos4 and pos1 != pos5 and pos2 != pos3 and pos2 != pos4 and pos2 != pos5 and pos3 != pos4 and pos3 != pos5 and pos4 != pos5:
                            print(
                                "#SPACE BATTLE RED TEAM# : Location of your ship saved !\n")
                            fullcoord = []
                            fullcoord.append(pos1)
                            fullcoord.append(pos2)
                            fullcoord.append(pos3)
                            fullcoord.append(pos4)
                            fullcoord.append(pos5)
                            teamRedPos[sh] = fullcoord
                            continue
                        else:
                            print(
                                "#SPACE BATTLE ERROR# : You entered at least two same cases, the placement choice will restart.")
                            team_red_init()
                    else:
                        print(
                            "#SPACE BATTLE ERROR# : At least one of the position is not on the board, the placement choice will restart.")
                        team_red_init()
                else:
                    print(
                        "#SPACE BATTLE ERROR : An error occurred, or missing one postion, the placement choice will restart.")
                    team_red_init()
        print("#SPACE BATTLE# : The game is ready to be played, be prepared.\n")


def time_check():
    '''the function that launch the game based on the remaining time'''

    now = datetime.now()
    limit = now + timedelta(minutes=15)
    time_limit = limit.strftime("%H:%M")

    global teamBlueTurn, teamRedTurn

    while True:
        now = datetime.now()
        time_now = now.strftime("%H:%M")
        if time_now == time_limit:
            print(
                "#SPACE BATTLE# : The game ended because of no remaining time, let's see who won !\n")
            check_blue_ships()
            check_red_ships()
            blueshipsleft = len(teamBluePos.keys())
            redshipsleft = len(teamRedPos.keys())
            if blueshipsleft > redshipsleft:
                print(
                    "#SPACE BATTLE# : The winner is... BLUE TEAM by time out ! Well played !")
                print(
                    f"blue : {blueshipsleft} ships left VS red : {redshipsleft} ships left")
                break
            elif redshipsleft > blueshipsleft:
                print(
                    "#SPACE BATTLE# : The winner is... RED TEAM by time out ! Well played !")
                print(
                    f"red : {redshipsleft} ships left VS blue : {blueshipsleft} ships left")
                break
            elif blueshipsleft == redshipsleft:
                print("#SPACE BATTLE# : The winner is... NOBODY ! EX AEQUO !\n")
                break
        elif teamBluePos == {}:
            print(
                "#SPACE BATTLE# : The winner is... RED TEAM ! They sank all the blue ships ! Well played !\n")
            break
        elif teamRedPos == {}:
            print(
                "#SPACE BATTLE# : The winner is... BLUE TEAM ! They sank all the red ships ! Well played !\n")
            break
        elif teamBlueTurn:
            teamBlueTurn = False
            teamRedTurn = True
            print(teamBluePos)
            blue_turn()
        elif teamRedTurn:
            teamBlueTurn = True
            teamRedTurn = False
            print(teamRedPos)
            red_turn()


def blue_turn():
    '''the function that initialize the blue team round'''

    print("#SPACE BATTLE# : It's up to the BLUE TEAM to take the shoot\n")
    choice = input(
        "#SPACE BATTLE BLUE TEAM# : Enter now the coordinates on the map where you want to shoot : \n")
    shoot = choice.upper()
    if completeBoard.count(shoot):
        for spaceship in teamRedPos:
            posforthisship = teamRedPos.get(spaceship)
            if posforthisship.count(shoot):
                posforthisship.remove(shoot)
                teamRedPos[spaceship] = posforthisship
                bluetouchedPositions.append(shoot)
                print("#SPACE BATTLE BLUE TEAM# :  That's a hit ! Well done\n")
                break
            else:
                bluemissedPositions.append(shoot)
                print(
                    "#SPACE BATTLE BLUE TEAM# :  That's a miss ! So unlucky, try again next round !\n")
                continue
    else:
        print("#SPACE BATTLE ERROR# :  The coordinates you entered are not on the map, the shoot choice will restart.\n")
        blue_turn()


def red_turn():
    '''the function that initialize the red team round'''

    print("#SPACE BATTLE# : It's up to the RED TEAM to take the shoot\n")
    choice = input(
        "#SPACE BATTLE RED TEAM# : Enter now the coordinates on the map where you want to shoot : \n")
    shoot = choice.upper()
    if completeBoard.count(shoot):
        for spaceship in teamBluePos:
            posforthisship = teamBluePos.get(spaceship)
            if posforthisship.count(shoot):
                posforthisship.remove(shoot)
                teamBluePos[spaceship] = posforthisship
                redtouchedPositions.append(shoot)
                print("#SPACE BATTLE RED TEAM# :  That's a hit ! Well done\n")
                break
            else:
                redmissedPositions.append(shoot)
                print(
                    "#SPACE BATTLE RED TEAM# :  That's a miss ! So unlucky, try again next round !\n")
                continue
    else:
        print(
            "#SPACE BATTLE ERROR# :  The coordinates you entered are not on the map, the shoot choice will restart.\n")
        red_turn()


def check_red_ships():
    sinkedredships = []
    for sshp in teamRedPos:
        if len(teamRedPos.get(sshp)) == 0:
            sinkedredships.append(sshp)

    for sinked in sinkedredships:
        teamRedPos.pop(sinked)


def check_blue_ships():
    sinkedblueships = []
    for sshp in teamBluePos:
        if len(teamBluePos.get(sshp)) == 0:
            sinkedblueships.append(sshp)

    for sinked in sinkedblueships:
        teamBluePos.pop(sinked)

### LAUNCH ###


if __name__ == "__main__":
    start()
else:
    print("#SPACE BATTLE LAUNCHING# : an error occurred, please restart manually the game or contact the developers")
