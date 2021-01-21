import time
# import RPi.GPIO as GPIO
# from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# initialize the sdk
cred = credentials.Certificate("/home/pi/Documents/dyeup-34223-firebase-adminsdk-i2doi-866cf1b0de.json")
# cred = credentials.Certificate("/Users/joshnoble/Downloads/dyeup-34223-firebase-adminsdk-i2doi-866cf1b0de.json")
app = firebase_admin.initialize_app(cred, {'databaseURL' : 'https://dyeup-34223-default-rtdb.firebaseio.com/'})

# fb = firebase.FirebaseApplication("https://dyeup-34223-default-rtdb.firebaseio.com/", None)
ref = db.reference()

player = None
playerOne = None
playerTwo = None
playerThree = None
playerFour = None
gameID = None

def checkActive():
    global gameID

    # get active gameID
    game_ref = ref.child('games/')
    snapshot = game_ref.order_by_key().limit_to_last(1).get() 
    for key in snapshot:
        gameID = key
        print("gameID: {}".format(gameID))
    # print("snapshot: {}".format(snapshot))

    # check if game is active
    activeStatus = game_ref.child(gameID + '/isActive').get()
    print("activeStatus: {}".format(activeStatus))

    if activeStatus == True:
        # assign players to buttons
        print("game is active!")
        buttonSetup()
    else:
        # clear buttons
        print("game is NOT active!")
        clearButtons()

    return

def buttonSetup():
    game_ref = ref.child('games/' + gameID)

    # get players
    global playerOne, playerTwo, playerThree, playerFour
    playerOne = game_ref.child('player1').get()
    playerTwo = game_ref.child('player2').get()
    playerThree = game_ref.child('player3').get()
    playerFour = game_ref.child('player4').get()
    print("player1: ", playerOne, ", player2: ", playerTwo, ", player3: ", playerThree, ", player4: ", playerFour)

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

    # update user stats (may not be necessary if function already in place)
    # user_ref = ref.child('users/' + player)
    # points = user_ref.child('points').get()    
    # points += 1
    # user_ref.update({"points": points})


def incPlunk():
    global gameID
    new_point_ref = ref.child('games/' + gameID + '/points')
    new_point_ref.push({"id": player, "type": 1})

    # update user stats (may not be necessary if function already in place)
    # user_ref = ref.child('users/' + player)
    # points = user_ref.child('points').get()    
    # points += 1
    # user_ref.update({"points": points})

    # plunks = user_ref.child('plunks').get()    
    # plunks += 1
    # user_ref.update({"plunks": plunks})


# def removePrevious():
    # note: need to store previous point first

# def doSomething():
    # what functionality do we want here? end game? 

# ==============================================================

while True:
    # if game is active, assign users to buttons 
    checkActive()

    # test
    player = playerOne
    print("button1 pushed, playerOne - UID: {}".format(player))

    incPoint()
    print("added point player 1!")
    break

    # if button1 pressed (playerOne)
    # if GPIO.input(10) == GPIO.HIGH:
    #     player = playerOne
    #     print("button1 pushed, playerOne - UID: ", player)

    #     pressCount = 1
    #     pressStatus = high
    #     buttonHold = true
    #     for 5 seconds:
    #         if GPIO.input(10) == GPIO.LOW:
    #             pressStatus = low
    #             buttonHold = false
    #             delay
    #         elif (GPIO.input(10) == GPIO.HIGH) && (pressStatus == low):
    #             pressCount += 1
    #             delay
    #         else
    #             delay
        
    #     if (buttonHold == true):
    #         # end game
    #     elif (pressCount == 1):
    #         # incPoint()
    #     elif (pressCount == 2):
    #         # incPlunk()
    #     elif (pressCoutn == 3):
            # remove previous point/plunk


#-------------------------------------------------------------------------------
        # if pressed once
            # increment point
            # incPoint()
        # else if pressed twice
            # increment plunk and point
            # incPlunk()
        # else if pressed thrice
            # remove previous point
            # removePrevious()
        # else if held for 5 seconds
            # do something else
            # doSomething()
        # else
            # return error

    # else if button2 pressed
        # player = playerTwo

        # if pressed once
            # increment point
            # incPoint()
        # else if pressed twice
            # increment plunk and point
            # incPlunk()
        # else if pressed thrice
            # remove previous point
            # removePrevious()
        # else if held for 5 seconds
            # do something else
            # doSomething()
        # else
            # return error

    # else if button3 pressed
        # player = playerThree

        # if pressed once
            # increment point
            # incPoint()
        # else if pressed twice
            # increment plunk and point
            # incPlunk()
        # else if pressed thrice
            # remove previous point
            # removePrevious()
        # else if held for 5 seconds
            # do something else
            # doSomething()
        # else
            # return error
    
    # else if button4 pressed
        # player = playerFour

        # if pressed once
            # increment point
            # incPoint()
        # else if pressed twice
            # increment plunk and point
            # incPlunk()
        # else if pressed thrice
            # remove previous point
            # removePrevious()
        # else if held for 5 seconds
            # do something else
            # doSomething()
        # else
            # return error


print("exited while loop")
