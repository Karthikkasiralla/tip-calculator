import random
import time


def print_slow(text):

    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print("\n")


print('''
 ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')

print_slow("🌴 Welcome to the Treasure Island 🌴")
print_slow("Your mission is to find the legendary lost treasure. But beware! The island is full of danger...")

# Choice 1: Crossroad
choice1 = input('You arrive at a mysterious crossroad. Do you go "left" or "right"? choose only one.\n').lower()

if choice1 == "left":
    print_slow("You walk cautiously and hear strange whispers in the wind...")
    # Choice 2: Lake
    choice2 = input(
        'You reach a vast lake. An eerie fog rolls over the water. Do you "wait" for a boat or "swim" across?\n').lower()

    if choice2 == "wait":
        print_slow("A rusty boat arrives with no one inside. You step in and it carries you safely across.")

        # Choice 3: Doors
        print_slow("You arrive at a grand mansion with three doors: One **red**, one **yellow**, and one **blue**.")
        choice3 = input('Which door do you choose? ("red", "yellow", "blue")\n').lower()

        if choice3 == "red":
            print_slow("🔥 As soon as you enter, flames erupt around you! \n Game Over. 🔥")

        elif choice3 == "yellow":
            print_slow("✨ You push open the golden door and... behold! The legendary treasure is yours! \n🏆🎉 YOU WIN! ✨")

        elif choice3 == "blue":
            print_slow(
                "🐺 You enter a dark room. Suddenly, glowing eyes appear. It's a den of beasts! You don’t stand a chance. Game Over. 🐺")

        else:
            print_slow("You hesitate and step back. Suddenly, the floor crumbles beneath you! \nGame Over. 💀")

    else:
        print_slow(
            "🌊 You start swimming, but the water turns ice cold. Tentacles emerge and pull you down.\n Game Over. 🌊")

else:
    print_slow(
        "⚠️ Well You chose the wrong path, You fall into a pit of darkness.\nr Game Over. ⚠️")

