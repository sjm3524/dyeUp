import time
import sys
import RPi.GPIO as GPIO
# from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# initialize the sdk
cred = credentials.Certificate("/home/pi/Documents/dyeup-34223-firebase-adminsdk-i2doi-866cf1b0de.json")
# cred = credentials.Certificate("/Users/joshnoble/Downloads/dyeup-34223-firebase-adminsdk-i2doi-866cf1b0de.json")
app = firebase_admin.initialize_app(cred, {'databaseURL' : 'https://dyeup-34223-default-rtdb.firebaseio.com/'})

# fb = firebase.FirebaseApplication("https://dyeup-34223-default-rtdb.firebaseio.com/", None)
ref = db.reference()

# define global variables
player = None
playerOne = None
playerTwo = None
playerThree = None
playerFour = None
gameID = None
activeStatus = None

def checkActive():
    global activeStatus

    # check if game is active
    game_ref = ref.child('games/')
    activeStatus = game_ref.child(gameID + '/isActive').get()
    # print("activeStatus: {}".format(activeStatus))

    if activeStatus == True:
        print("game is active!")
    else:
        # clear buttons
        print("game is NOT active!")
        clearButtons()

def getGameID():
    global gameID

    # get active gameID
    game_ref = ref.child('games/')
    snapshot = game_ref.order_by_key().limit_to_last(1).get() 
    for key in snapshot:
        gameID = key
        print("gameID: {}".format(gameID))

def buttonSetup():
    game_ref = ref.child('games/' + gameID)

    # get players
    global playerOne, playerTwo, playerThree, playerFour
    playerOne = game_ref.child('player1').get()
    playerTwo = game_ref.child('player2').get()
    playerThree = game_ref.child('player3').get()
    playerFour = game_ref.child('player4').get()
    # print("player1: ", playerOne, ", player2: ", playerTwo, ", player3: ", playerThree, ", player4: ", playerFour)

def clearButtons():
    global playerOne, playerTwo, playerThree, playerFour
    playerOne = None
    playerTwo = None
    playerThree = None
    playerFour = None
    print("No active game")

def incPoint():
    global gameID
    new_point_ref = ref.child('games/' + gameID + '/points')
    new_point_ref.push({"id": player, "type": 0})

    # update user stats (not necessary bc function already in place)
    # user_ref = ref.child('users/' + player)
    # points = user_ref.child('points').get()    
    # points += 1
    # user_ref.update({"points": points})

def incPlunk():
    global gameID
    new_point_ref = ref.child('games/' + gameID + '/points')
    new_point_ref.push({"id": player, "type": 1})

    # update user stats (not necessary bc function already in place)
    # user_ref = ref.child('users/' + player)
    # points = user_ref.child('points').get()    
    # points += 1
    # user_ref.update({"points": points})

    # plunks = user_ref.child('plunks').get()    
    # plunks += 1
    # user_ref.update({"plunks": plunks})

def removePrevious():
    global playerOne, playerTwo, playerThree, playerFour
    global gameID

    # get last point ID
    last_ID_ref = ref.child('games/' + gameID + '/points')
    snapshot = last_ID_ref.order_by_key().limit_to_last(1).get() 
    for key in snapshot:
        lastPointID = key
        print("lastPointID: {}".format(lastPointID))

    # get score type and userID of scorer
    last_point_ref = ref.child ('games/' + gameID + '/points/' + lastPointID)
    scoreType = last_point_ref.child('type').get()
    userID = last_point_ref.child('id').get()
    print("scoreType: {}".format(scoreType))
    print("userID: {}".format(userID))

    # subtract point/plunk from user stats
    if (scoreType == 0):
        user_ref = ref.child('users/' + userID)
        points = user_ref.child('points').get()    
        points -= 1
        user_ref.update({"points": points})

    elif (scoreType == 1):
        user_ref = ref.child('users/' + userID)
        points = user_ref.child('points').get()    
        points -= 1
        user_ref.update({"points": points})

        plunks = user_ref.child('plunks').get()    
        plunks -= 1
        user_ref.update({"plunks": plunks})

    # subtract point from team score
    if (userID == playerOne or userID == playerTwo):
        # remove point t1score
        t1score = ref.child('games/' + gameID + '/t1Score').get()
        # print("t1score: {}".format(t1score))
        t1score -= 1
        ref.child('games/' + gameID).update({"t1Score": t1score})

    elif (userID == playerThree or userID == playerFour):
        # remove point t2score
        t2score = ref.child('games/' + gameID + '/t2Score').get()
        # print("t2score: {}".format(t2score))
        t2score -= 1
        ref.child('games/' + gameID).update({"t2Score": t2score})

    # delete the point from the game 
    last_point_ref.delete()

# ==============================================================

while True:

    # if button1 pressed (playerOne)
    if GPIO.input(10) == GPIO.HIGH:

        pressCount = 1
        pressStatus = True
        buttonHold = True

        # 5 second loop to check for buttons presses/hold
        t_end = time.time() + 5
        while time.time() < t_end:
            if GPIO.input(10) == GPIO.LOW:
                pressStatus = False
                buttonHold = False
            if (GPIO.input(10) == GPIO.HIGH) and (pressStatus == False):
                pressCount = 2

        print("pressCount: {}".format(pressCount))
        print("pressStatus: {}".format(pressStatus))
        print("buttonHold: {}".format(buttonHold))
        # get the gameID and check if game is active
        getGameID()
        checkActive()

        if activeStatus == True:
            buttonSetup()
            player = playerOne
            # print("button1 pushed, playerOne - UID: {}".format(player))
            
            if (buttonHold == True):
                print("button held for 5 seconds")
                removePrevious()
                time.sleep(5) # delay so another button press isn't recroded
            elif (pressCount == 1):
                incPoint()
                print("button pressed once")
            elif (pressCount == 2):
                incPlunk()
                print("button pressed twice")
            # elif (pressCount == 3):
            #     print("button pressed thrice")

    # if button2 pressed (playerTwo)
    # if GPIO.input(11) == GPIO.HIGH:

    #     pressCount = 1
    #     pressStatus = True
    #     buttonHold = True

    #     # 5 second loop to check for buttons presses/hold
    #     t_end = time.time() + 5
    #     while time.time() < t_end:
    #         if GPIO.input(11) == GPIO.LOW:
    #             pressStatus = False
    #             buttonHold = False
    #         if (GPIO.input(11) == GPIO.HIGH) and (pressStatus == False):
    #             pressCount = 2

    #     print("pressCount: {}".format(pressCount))
    #     print("pressStatus: {}".format(pressStatus))
    #     print("buttonHold: {}".format(buttonHold))
    #     # get the gameID and check if game is active
    #     getGameID()
    #     checkActive()

    #     if activeStatus == True:
    #         buttonSetup()
    #         player = playerTwo
    #         # print("button2 pushed, playerTwo - UID: {}".format(player))
            
    #         if (buttonHold == True):
    #             print("button held for 5 seconds")
    #             removePrevious()
    #             time.sleep(5) # delay so another button press isn't recroded
    #         elif (pressCount == 1):
    #             incPoint()
    #             print("button pressed once")
    #         elif (pressCount == 2):
    #             incPlunk()
    #             print("button pressed twice")
    #         # elif (pressCount == 3):
    #         #     print("button pressed thrice")

    # # if button3 pressed (playerThree)
    # if GPIO.input(12) == GPIO.HIGH:

    #     pressCount = 1
    #     pressStatus = True
    #     buttonHold = True

    #     # 5 second loop to check for buttons presses/hold
    #     t_end = time.time() + 5
    #     while time.time() < t_end:
    #         if GPIO.input(12) == GPIO.LOW:
    #             pressStatus = False
    #             buttonHold = False
    #         if (GPIO.input(12) == GPIO.HIGH) and (pressStatus == False):
    #             pressCount = 2

    #     print("pressCount: {}".format(pressCount))
    #     print("pressStatus: {}".format(pressStatus))
    #     print("buttonHold: {}".format(buttonHold))
    #     # get the gameID and check if game is active
    #     getGameID()
    #     checkActive()

    #     if activeStatus == True:
    #         buttonSetup()
    #         player = playerThree
    #         # print("button2 pushed, playerThree - UID: {}".format(player))
            
    #         if (buttonHold == True):
    #             print("button held for 5 seconds")
    #             removePrevious()
    #             time.sleep(5) # delay so another button press isn't recroded
    #         elif (pressCount == 1):
    #             incPoint()
    #             print("button pressed once")
    #         elif (pressCount == 2):
    #             incPlunk()
    #             print("button pressed twice")
    #         # elif (pressCount == 3):
    #         #     print("button pressed thrice")

    #     # if button2 pressed (playerOne)
    
    # # if button4 pressed (playerFour)
    # if GPIO.input(13) == GPIO.HIGH:

    #     pressCount = 1
    #     pressStatus = True
    #     buttonHold = True

    #     # 5 second loop to check for buttons presses/hold
    #     t_end = time.time() + 5
    #     while time.time() < t_end:
    #         if GPIO.input(13) == GPIO.LOW:
    #             pressStatus = False
    #             buttonHold = False
    #         if (GPIO.input(13) == GPIO.HIGH) and (pressStatus == False):
    #             pressCount = 2

    #     print("pressCount: {}".format(pressCount))
    #     print("pressStatus: {}".format(pressStatus))
    #     print("buttonHold: {}".format(buttonHold))
    #     # get the gameID and check if game is active
    #     getGameID()
    #     checkActive()

    #     if activeStatus == True:
    #         buttonSetup()
    #         player = playerFour
    #         # print("button2 pushed, playerFour - UID: {}".format(player))
            
    #         if (buttonHold == True):
    #             print("button held for 5 seconds")
    #             removePrevious()
    #             time.sleep(5) # delay so another button press isn't recroded
    #         elif (pressCount == 1):
    #             incPoint()
    #             print("button pressed once")
    #         elif (pressCount == 2):
    #             incPlunk()
    #             print("button pressed twice")
    #         # elif (pressCount == 3):
    #         #     print("button pressed thrice")
print("exited while loop")
