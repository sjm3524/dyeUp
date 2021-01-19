import time
import RPi.GPIO as GPIO
from firebase import firebase
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
app = firebase_admin.initialize_app(cred, {'databaseURL' : 'https://dyeup-34223-default-rtdb.firebaseio.com/'})

fb = firebase.FirebaseApplication("https://dyeup-34223-default-rtdb.firebaseio.com/", None)
ref = db.reference()

def buttonSetup():
    global playerOne, playerTwo, playerThree, playerFour
    
    # need to assign players
    playerOne = 'tHD9bLCP8RdGBEjR6rrLuKJAAey2'
    print("assigned player UIDs")
    return
    

def incPoint():
    user_ref = ref.child('users/' + player)
    points = user_ref.child('points').get()    
    points += 1
    user_ref.update({"points": points})

def incPlunk():
    user_ref = ref.child('users/' + player)
    points = user_ref.child('points').get()    
    points += 1
    user_ref.update({"points": points})

    plunks = user_ref.child('plunks').get()    
    plunks += 1
    user_ref.update({"plunks": plunks})


# def removePrevious():
    # note: need to store previous point first (already done)

# def doSomething():
    # what functionality do we want here? end game? 

# ==============================================================

while True:
    # if new game, reconfigure buttons to the respecitve users
    buttonSetup()

    # for testing only, move in button loop later
    player = playerOne
    print(player)

    # if button1 pressed
    if GPIO.input(10) == GPIO.HIGH:
        player = playerOne
        print("button pushed, UID: ")

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