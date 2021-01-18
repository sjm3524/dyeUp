import RPi.GPIO as GPIO
from firebase import firebase

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

firebase = firebase.FirebaseApplication("https://dyeup-34223-default-rtdb.firebaseio.com/", None)

# global var 
player, playerOne, playerTwo, playerThree, playerFour = ""

while True:
    # if new game, reconfigure buttons to the respecitve users
        buttonSetup()



    # if button1 pressed
        player = playerOne

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




def buttonSetup():
    playerOne = 'tHD9bLCP8RdGBEjR6rrLuKJAAey2'
    # assign Player 2 UID
    # assign Player 3 UID
    # assign Player 4 UID

# def incPoint():


# def incPlunk():


# def removePrevious():
    # note: need to store previous point first

# def doSomething():
    # what functionality do we want here? end game? 