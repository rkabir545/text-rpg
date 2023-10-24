# created on 10/13/23 by Raaiq
# a text based rpg game
import random

# this room gives a brief overview of the game, then allows the user to proceed to the next room
def roomStart():
    print("""You are a secret agent for the government,
and you have been called in for a dangerous mission. It has been
reported that a group of terrorists is planning an attack on a
secret government facility. Your task is to infiltrate the facility and stop
the terrorists from executing their plan. You are equipped with various
weapons and gadgets to help you succeed.""")
    input("Press Enter to Continue")
    roomOne()

# intro to the first room, tells you what the objective is and the surrounding,
# it also brings you to the roomOnePuzzle() after completing roomOnePuzzle(),
# it asks the user to proceed to the next room
def roomOne(): 
    print("You have made it to room 1! The Warehouse...")
    print("""As you enter the undercover location for your mission,
you come across a dark warehouse that holds a
series of items you will need for the work ahead.
However, the entrance is secured with a security lock.
You must use your skills to hack into the security system
and gain access to the warehouse.""")
    roomOnePuzzle()
    input("Press Enter to Continue")
    roomTwo()
    
# within the function roomOnePuzzle(), it prompts the user a choice between a gun and a laptop
# whichever item will allow them to unlock the lock, the gun will reprompt the user
# the laptop choice will boot up and ask you to choose a number between 1-5
# the number is random, every choice chosen by the user will not change the random number until failed
#  after the 3 tries given. which essentially, brings the user back to the original question.
# if the number is chosen correctly it will bring you back to roomOne() and proceed to roomTwo()
def roomOnePuzzle():
    user_choice = input("""You are equipped with a laptop and a gun, choose an object that will help you unlock the security lock: """)
    if user_choice == "laptop":
        print("Good Choice")
        input("Laptop is equipped! Press Enter to Use it!")
        print("Laptop booting up...")
        random_numbers = (1,2,3,4,5)
        random_number = random.choice(random_numbers) 

        tries = 0
        while tries < 3:
            number_choice = int(input("""In order to unlock the security lock, you will need to pick a number between
1-5, you have 3 tries, fail and you will die. Select the Number: """))
            if number_choice == random_number:
                print("You have unlocked the security lock!")
                return
            else:
                print("Try again, the number is incorrect")
                tries += 1
        print("You have failed after 3 tries. You Died.")
        roomOne()
    else:
        print("Wrong choice.")
        roomOne()
        
# introduction to the second room, gives a brief overview and then brings you to roomTwoPuzzle()
# after roomTwoPuzzle() is finished, it will ask the user to proceed to the next room.    
def roomTwo():
    print("You have made it to room 2! The Computer Room...")
    print("""You manage to access the warehouse and retrieve
the necessary items, but you find a locked safe that contains more
gadgets that could be useful for your mission. You must apply your
knowledge of computer systems to break into the safe and access the equipment.""")
    roomTwoPuzzle()
    input("Press Enter to Continue")    
    roomThree()
    
# upon entering this room, you will be prompted with choices of colors in order to solve a puzzle
# if the colors aren't put into order. then the code will loop until the correct output is given by the user
def roomTwoPuzzle():
    print("""You find a note on the safe that says: To open the safe, you must solve this puzzle = 
There are three buttons on the safe: red, green, and blue. The safe will open if you press the 
buttons in the correct order. The order of the buttons is:
1. The color that is not between red and blue
2. The color that is between red and blue
3. The color that is neither red nor blue""")

    answer = ""
    while answer != "green, blue, red":
        answer = input("What is the order of the buttons? red, green, or blue?: ")
        if answer != "green, blue, red":
            print("Hint: The first button is the color that is not between red and blue.")
            print("Incorrect. Try again.")

    print("Correct! The safe opens.")
    print("You found a guitar, chopsticks, laser, and a usb drive!")
    return
  # If the player answered incorrectly, give them a hint

# introduction to the third room, gives a brief overview and then brings you to roomThreePuzzle()
# after roomThreePuzzle() is finished, it will ask the user to proceed to the next room. 
def roomThree():
    print("You have made it to room 3! The Lobby...")
    print("""As you approach the government facility's front door,
you find a guard blocking your path. You need to find a way to distract the
guard to sneak past him and gain access.""")
    roomThreePuzzle()
    input("Press Enter to Continue")
    roomFour()

# in this room, the puzzle is a riddle, if user inputs the correct answer they will be able to sneak
# past the guards, however there is no limit to answering this question, meaning it is inevitable
# amd you cannot skip this room until you guess correctly
def roomThreePuzzle():
    riddle = ""
    while riddle != "a shirt":
        riddle = input("""You find a note on the guard's desk that says: 
To distract the guard, you must solve this puzzle: 
What has a neck without a head, and two arms without hands?: """)
        if riddle != "a shirt":
            print("Incorrect. Try again")
    print("Correct! You have snuck past the guard!")
    return

# introduction to the fourth room, gives a brief overview and then brings you to roomFourPuzzle()
# after roomFourPuzzle() is finished, it will ask the user to proceed to the next room. 
def roomFour():
    print("You have made it to room 4! The Security Room...")
    print("""You manage to sneak past the guard and enter the facility,
but you find that the terrorists have rigged the building with
various traps. You need to gain access to the security room to
disable the bombs and prevent any damage.""")
    roomFourPuzzle()
    input("Press Enter to Continue")
    roomFive()

# in this room there are four levers, labeled A, B, C, and D, the user has to put it into correct order
# the correct order is ABDC, if the user doesn't correctly find the sequence, the bomb will explode and
# bring you back to the first room
def roomFourPuzzle():
    print("""You find a series of levers on the wall. There is a note on 
the wall that says: To disable the bombs, you must pull the levers 
in the correct order. If you pull the wrong lever, the bombs will 
detonate. There are four levers, labeled A, B, C, and D. You need 
to experiment with the levers to find the correct order. If you pull 
the wrong lever, the bombs will detonate and the game will end.""")
    print("You Have 5 Tries..")
    levers = "ABDC"
    tries = 0

    for i in range(5):
        userOrder = input("Enter the order of the levers: ")
        if userOrder == levers:
            print("Correct! The bombs have been disabled.")
            return
        else:
            tries += 1
            print("Incorrect. You used " + str(tries) + " tries.")


    print("Incorrect. The bombs have detonated.")
    print("You Died...")
    roomOne()

# introduction to the fifth room, gives a brief overview and then brings you to roomFivePuzzle()
# after roomFivePuzzle() is finished, it will ask the user to proceed to the next room. 
def roomFive():
    print("You have made it to room 5! The Mainframe Room...")
    print("""After successfully disabling the bombs,
you learn that the terrorists' leader is currently accessing
important files in the mainframe room. You need to stop the
leader and prevent them from stealing valuable information.""")
    roomFivePuzzle()
    input("Press Enter to Continue")
    roomSix()

# The user has a choice between 2 rooms, choice 1 gives multiple choices, the gun and laser
# lead to the next room, but the rest of the items lead to your death
# choice 2 leads ot their death and essentially bringing them back to room one
# if you give an invalid choice it will repeat the question again
def roomFivePuzzle():
  print("""You find a terminal in the mainframe room. There is a note on the terminal that says: 
"To stop the terrorists' leader, you must make a choice. You can either:
1. Try to hack into the mainframe and disable the security system. This is a difficult task, 
but if you succeed, you will be able to stop the terrorists' leader without risking any harm.
2. Confront the terrorists' leader directly. This is a dangerous option, but if you are successful, 
you will be able to stop the leader and prevent them from stealing valuable information.

Which option do you choose? 1 or 2?""")

  choice = input("Enter your choice: ")

  if choice == "1":
    user_choice = input("""You attempt to hack into the mainframe. The security system is complex, 
but you are able to disable it. The terrorists' leader catches you in the act and pulls out his knife,
you currently have: a laptop, gun, flashlight, guitar, chopsticks, laser, and a usb drive. Choose Object: """)
    if user_choice == "gun":
      print("You have succesfully shot the terrorist leader to death.")
      return
    elif user_choice == "laser":
      print("You burned the terrorist leader's eye to death")
      return
    elif user_choice == "guitar" or "flashlight" or "chopsticks" or "laptop":
      print("You were fatally stabbed to death...")
      roomOne()
    else:
      print("Invalid Choice")
      print("Try Again.")
      roomFivePuzzle()
     
  elif choice == "2":
    print("""You confront the terrorists' leader directly. The leader ends up stabbing you to death...""")
    roomOne()
  else:
    print("Invalid choice.")
    roomFivePuzzle()  

# introduction to the sixth room, gives a brief overview and then brings you to roomSixPuzzle()
# after roomSixPuzzle() is finished, it will ask the user to proceed to the next room. 
def roomSix():
    print("You have made it to room 6! The Helipad...")
    print("""After stopping the terrorists' attack,
you need to find an escape route. You arrive at the helipad and find a
helicopter parked. However, the helicopter's security system is activated,
and you must solve a puzzle to deactivate the system and escape.""")
    roomSixPuzzle()
    input("Press Enter to Continue")
    roomEnd()
    
# in this room, you are prompted with several numbers doubling each time, in order to solve it
# the answer would be 32 + 32, essentially the answer is 64
# if you incorrectly solve this question you will be prompted again until correctly answered
def roomSixPuzzle():
    print("You need to solve a puzzle to deactivate the helicopter's security system.")
    print("You see a sequence of numbers written on a panel: 2, 4, 8, 16, 32, __?.")
    
    missing_number = 64 

    user_input = int(input("Enter the missing number in the sequence: "))

    if user_input == missing_number:
        print("Correct! The security system is deactivated, and you can now board the helicopter.")
        return
    else:
        print("Incorrect. The security system remains active. Try again.")
        roomSixPuzzle()

# introduction to the last room, you finished!
def roomEnd():
    print("""You successfully complete your mission and escape with
valuable information. The government praises your bravery and awards
you for your success as a secret agent. You realize that your work
is never really done, as more missions await you in the future.""")
    input("Press Enter to Continue")
    print("You have made it to the end!")

roomStart()



