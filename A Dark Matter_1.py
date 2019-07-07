# Name: Morris Bobssonsby
# Date: 11/07/19
# Description: Text-Based Space Adventure

import random
import time

from sys import exit


debug_flag = True


def displayIntro():
    print("Name: Morris Bobssonsby")
    time.sleep(2)
    print("# Date: 11/07/19")
    time.sleep(2)
    print("'A Dark Matter'")
    time.sleep(3)
    print("Welcome, I hope you slept okay and you dont ache too much!")
    print("You have been out for a while, but I suppose that's what Cryo-sleep does eh?")
    print("Now I know you are still groggy, but you have some big decisions to make!")
    print("First, lets just get you choosing")
    print("Do you want some orange juice with bits")
    print("Or do you want a nice cold water")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2":     # Input Validation
        path = input("Which will you choose? (1 = Orange Juice with Bits!, 2 = A cold glass of Water): ")

    return path

def checkPath(chosenPath):
    print("You take the juice and have a long sip")
    time.sleep(2)
    print("There is a tense presence in the room")
    time.sleep(2)
    correctPath = random.randint(1, 2)
   # if debug_flag:
       # print(correctPath)

    secretpath = 8
    secretpath2 = 9

    if chosenPath == str(correctPath):
        print("Ah, Good Choice my friend" )
        time.sleep(2)
        print("I fear if you had chosen the other")
        print("You would be dead")

    else:
        print("You fiend!")
        time.sleep(2)
        print("How could you?!")
        time.sleep(1)
        print("Choose to drink the very fluid that courses through my tubes")
        time.sleep(1)
        print("I will kill you where you stand")
        time.sleep(2)
        print("Give me a second!")
        time.sleep(1)
        print("A crackle of lightning energy thunders from above you, it courses around you but then dies down")
        time.sleep(4)
        print("Argh! Never mind, I will kill you at some other point")
        time.sleep(1)
        print("For now you are forgiven, But be warned!")

def displayIntro_2():
    print("You are still with us")
    time.sleep(2)
    print("You stand up and take a look around.")
    time.sleep(2)
    print("there is a gun on the far table near the door.")
    time.sleep(2)

def choosePath_2():
    path = ""
    while path != "1" and path != "2":     # Input Validation
        path = input("Do you want to want to pick it up? (Yes = 1 or No = 2): ")

    return path

def checkPath_2(chosenPath_2):
    correctPath_2 = 2

    if chosenPath_2 == str(correctPath_2):
        print("That is good, Weapons are heavily forbidden here")
    else:
        print("What have you done?!")
        time.sleep(2)
        print("Weapons are not permitted here")
        print("Put it down at once")
        time.sleep(3)
        print("Well?!")
        time.sleep(2)
        print("You put the gun down and walk towards the door")
        time.sleep(2)
        print("You notice a small piece of paper taped to the door saying: TORAB ")

def displayIntro_3():
    print("Come through this door over here")
    time.sleep(2)
    print("I have something to show you!")
    time.sleep(3)
    print("Why are you looking so scared?")
    time.sleep(2)
    print("Tell me what you see on the table")
    print("My sensors cant read it")
    time.sleep(3)
    print("What do you See?")


def choosePath_3():
    path = input("")

    return path

def checkPath_3(chosenPath_3):
    correctPath_3 = "Dark Matter"
    correctPath_4 = "Light Matter"
    correctPath_5 = "A Large feast, Piping hot"
    correctPath_6 = "A Mime"

    nomatch_flag = False

    if chosenPath_3 == str(correctPath_3):
        print("Ah I see, How curious")
    elif chosenPath_3 == correctPath_4:
        print("Ah I see, That's not Possible")
    elif chosenPath_3 == correctPath_5:
        print("See am I not a wonderful host, Sit down and eat!")

    elif chosenPath_3 == correctPath_6:
        print("Wow that's Immature")

    else:
        print("Hmm, Well that not really my intended cargo but we will keep it anyway")


    if chosenPath_3 == str(correctPath_5):
        print("THE GAME IS OVER AND YOU ARE FULL AND WEALTHY")

def displaySet_1():
    print("You have made it pretty far already")
    time.sleep(2)
    print("But now its time for a real challenge")
    time.sleep(2)
    print("Follow Me!")

def table():
    print("The table was empty apart from a small torn up napkin which had the words TORAB in large letters")
    print("You put it in your pocket")
    roomPlay_2()



def safe():
    print("The Safe is old and made of thick iron")
    time.sleep(2)
    print("There is a small keypad on which to type words ")

    print("Enter the password to try the safe.")

    combination = input("> ")

    if combination == "TORAB":
        print("Success!  The safe opens. Inside, you find a key and some cash.")

        global key
        key = True

        roomPlay_2()

    elif combination != "TORAB":
        print("That didn't seem to work. There must be a clue around somewhere.")

        roomPlay_2()
    else:
        dead("\tYou notice a strange substance on your fingers.  You smell it and die instantly.")


def window():
    print("The Man begins to turn slowly as you approach")
    time.sleep(2)
    print("Ah Boris its a pleasure to see you, do you not remember an old friend")
    time.sleep(2)
    print("1 = My Names not Boris, I am Morris Bobssonsby, Son of Tarquin the great. 2 = Ah yes nice to see you it has been a while, I havent seen you since Ohio")

    action = input("> ")

    if action == "1":
        answer_1()
    else:
        print("What Ho! Some sort of imposter!")
        time.sleep(2)
        print("Your name is Morris Bobssonsby, Son of Tarquin the great. ")
        time.sleep(2)
        print("You should know that better than anyone else!")
        displayOutro()

def answer_1():
    print("Good work that was a trick to see if you are really you, can never tell these days")
    roomPlay_2()

def roomPlay_1():
    print("The next room is much darker than all the rest")
    time.sleep(2)
    print("There are a number of things in this room to interact with")
    time.sleep(1)
    print("There is a large mahogany table in the center of the room which had a strange undulating shape on the surface, there was a old iron safe, still dusty but standing in the corner")
    print("There was a window on the far side of the room with a tall man standing, peering out into the vast emptiness")
    time.sleep(2)
    print("I had a strange feeling from this room and did not know if I should even be in here ")
    time.sleep(2)

    print("Enter '1' to investigate the Table.")
    print("Enter '2' to investigate the Safe.")
    print("Enter '3' to investigate the Man in the Corner.")
    print("Enter '4' to exit the room.")

    action = input("> ")

    if action == "1":
        table()
    elif action == "2":
        safe()
    elif action == "3":
        window()
    elif action == "4":
        roomPlay_2()
    else:
        pass

def room_2():
    print("You have entered a new room")
    time.sleep(2)
    print("It has a tall ceiling ")

def roomPlay_2():

    print("You leave that item and look around the room some more")
    print("Enter '1' to investigate the Table.")
    print("Enter '2' to investigate the Safe.")
    print("Enter '3' to investigate the Man in the Corner.")
    print("Enter '4' to exit the room.")

    action = input("> ")

    if action == "1":
        table()
    elif action == "2":
        safe()
    elif action == "3":
        window()
    elif action == "4":
        room_2()

def offset_1():
    print("As you go to explore the rest of the room, the ceiling suddenly shakes and debris comes flying from above")
    time.sleep(1)
    print("You dive off into a doorway narrowly avoiding the blast ")

def displayOutro():
    print("You have died in some unfortunate way, try again")

class Character:


    def __init__(self, name, age):

        self.name = name
        self.age = age


    def say_my_name(self):
        print(self.name)


    def how_old_am_I(self):
        print(self.age)

    def get_older(self):
        self.age += 1
        print('Ive got older')




playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    # displayIntro()
    # choice = choosePath()
    # checkPath(choice)
    # displayIntro_2()
    # choice_2 = choosePath_2()
    # checkPath_2(choice_2)
    # displayIntro_3()
    # choice_3 = choosePath_3()
    # checkPath_3(choice_3)
    # displaySet_1()
    roomPlay_1()
    time.sleep(2)
    offset_1()
    displayOutro()

    playAgain = input("Do you want to play again? (yes or y to continue)")

# Bob = Character("Bob", 36)
# print("Whats your name?")
# Bob.say_my_name()
# print("How old are you?")
# Bob.how_old_am_I()
# Bob.get_older()
# Bob.how_old_am_I()
#
# print('------------')
# Tim = Character("Tim", 26)
# print("Whats your name?")
# Tim.say_my_name()
# print("How old are you?")
# Tim.how_old_am_I()
# Tim.get_older()
# Tim.how_old_am_I()




