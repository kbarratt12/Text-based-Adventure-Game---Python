# Steven Dang - sdang4@student.gsu.edu
# Rachit Kowatra - rkowatra1@student.gsu.edu
# Malachi Barratt - mbarratt2@student.gsu.edu
import random

def roll_dice():
    return random.randint(1, 6)

def player_damage(attack):
    dice_roll = roll_dice()
    #damage = 0

    if dice_roll in range(1, 3):
        damage = round(0.2 * attack,2)
    elif dice_roll in range(3, 5):
        damage = round(0.5 * attack,2)
    elif dice_roll == 6:
        damage = attack
        attack = damage
        return float(damage)

def enemy_damage(enemy_type, enemy_attack):
    dice_roll = roll_dice()
    damage = 0

    if dice_roll in range(1, 3):
        damage = 0.1 * enemy_attack
    elif dice_roll in range(3, 5):
        damage = 0.3 * enemy_attack
    else:
        damage = enemy_attack
    return damage
    #dice_roll = roll_dice()
    #damage = 0

    #if dice_roll in range(1, 3):
        #damage = 0.1 * attack
    #elif dice_roll in range(3, 5):
        #damage = 0.3 * attack
    #else:
        #damage = attack

    #return damage


def generate_pirate_health(pirate_type):
    if pirate_type == "Regular":
        return random.randint(30, 50)
    elif pirate_type == "Wolf":
        return random.randint(20,30)
    elif pirate_type == "Captain":
        return random.randint(50, 80)
    elif pirate_type == "Boss":
        return random.randint(80, 120)
    else:
        return 50  # Default health if pirate type is unknown or unspecified


def create_character():
    name = input("Enter your character's name: ")
    class_name = pick_class()
    attributes = class_attributes(class_name)
    return {"name": name, "class": class_name, "Health": attributes["Health"], "Attack": attributes["Attack"]}




def pick_class():
    classes = ["Warrior", "Clown", "Knight", "Rogue"]
    class_name = input("Choose your class (Warrior, Clown, Knight, Rogue): ")
    while class_name not in classes:
        print("Invalid class. Please choose again.")
        class_name = input("Choose your class (Warrior, Clown, Knight, Rogue): ")
    return class_name


def create_weaponname(class_name):
    weaponname = ""
    if class_name == "Warrior":
        weaponname = input(
            "After deciding to go down the path of the sword, you scower about the ship wreck to find a suitable weapon. Within a few minutes of searching you stumble upon a glistening blade forged from an amalgamation of metal alloys. It seems to not have a name, "
            "you decided to name it...:")
        print(f"You've named your weapon '{weaponname}'")
    elif class_name == "Knight":
        weaponname = input(
            "Upon contemplation, you have decided to be a protector of the lands and went upon the path of a knight. You prowl about the wreckage looking for a suitable shield to protect you and your future companions. After a worthwhile search you stumble upon a grand shield cladded in obsidian and metal spikes. "
            "You've decided to name it...")
        print(f"You've named your weapon '{weaponname}'")
    elif class_name == "Clown":
        weaponname = input(
            "You've decided to go down the path of silliness, tom-foolery, and comedic combat. As an ex-member of a royal family, you were always chained to your family's prestige and reputation, but now that they are gone you can be what you always wanted to be deep down: A Clown. You have decided to develop a form of combat with "
            "your magical ""bag of tricks"" known as...:")
        print(f"You've named your weapon '{weaponname}'")
    elif class_name == "Rogue":
        weaponname = input(
            "You are in a deep state of shock after watching your entire family die right before your eyes as you helplessly watch. After several weeks in a deep depression, you finally think about what shall be done next. After much contemplation and deliberation, you decide to become like a shadow, a cold and mysterious killer, who haunts your enemies. To assist you in doing so, you will need a fine blade. You scour the wreckage in the hopes of finding a suitable edge to become your most trusted companion. After days of searching, you find a sharp, jagged blade with an inscription in an ancient language you don't recognize. "
            "You decide to name it...:")
        print(f"You've named your weapon '{weaponname}'")

def class_attributes(class_name):
    attributes = {"Health": 0, "Attack": 0}
    if class_name == "Warrior":
        attributes["Health"] = 100
        attributes["Attack"] = 20
    elif class_name == "Clown":
        attributes["Health"] = random.randint(1, 200)
        attributes["Attack"] = random.randint(1, 70)
    elif class_name == "Knight":
        attributes["Health"] = 150
        attributes["Attack"] = 10
    elif class_name == "Rogue":
        attributes["Health"] = 75
        attributes["Attack"] = 40
    return attributes







def actions_menu():
    print("Actions Menu:")
    print("1. Heal yourself to full health")
    print("2. Help the townsfolk")
    print("3. Training grounds")
    print("4. Go to the tavern to gamble")
    choice = input("Choose an action (1-4): ")
    return choice


def perform_action(character, karma):
    choice = actions_menu()

    if choice == "1":
        print("You heal yourself to full health.")
        character["Health"] = class_attributes(character['class'])["Health"]
    elif choice == "2":
        print(
            "You decide to help the townsfolk by doing jobs around the town. They are so grateful")
        karma += 10
    elif choice == "3":
        print("You train and learn new skills in the wilderness of Pythor, increasing your attack by 5.")
        character["Attack"] += 5
    elif choice == "4":
        gamble_result = random.choice(["blackout", "tavern_brawl", "regenerate_health", "make_friends"])

        if gamble_result == "blackout":
            print("You get blackout drunk, go clean yourself up")
            karma -= 5
        elif gamble_result == "tavern_brawl":
            print("You get into a tavern brawl with a pirate gang, increasing your Attack by 5.")
            character["Attack"] += 5
        elif gamble_result == "regenerate_health":
            print("The ale is so tasty that you fully regenerate your health.")
            character["Health"] = class_attributes(character['class'])["Health"]
        elif gamble_result == "make_friends":
            print("You make friends with the townspeople in the tavern, what a charismatic person you are.")
            karma += 5
        elif gamble_result == "Instadeath":
            print("GAME OVER: Stop gambling you addict")
            character_alive = 0

    return character, karma


