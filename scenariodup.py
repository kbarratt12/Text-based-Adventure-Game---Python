#Steven Dang - sdang4@student.gsu.edu
#Rachit Kowatra - rkowatra1@student.gsu.edu
#Malachi Barratt - mbarratt2@student.gsu.edu
import commands

roll=0
karma=0
#intro (character creation)
print("In the kingdom of Pythor, you are a descendant next in line to the throne. Today your father, the King, is taking your family along on his voyage to visit an allied nation for a friendly meeting. After you’ve set sailed, the winds felt a little off this specific day. Suddenly, across the horizon you see 3 ships appear with flags of your allied nation. It seems they are here to escort your entourage, but suddenly as they approached closer a different flag was hoistered, the Jolly-Roger. The pirates rammed and boarded your ship. In the ensuing chaos, your family, including the King, was mercilessly slaughtered, leaving you as the lone survivor. Desperate to escape, you leaped overboard, clutching a piece of wreckage as the pirates continued their brutal assault. Washed ashore on an unknown location, battered and mourning the loss of your entire direct family, you now find yourself alone, seeking answers in the aftermath of the treacherous attack that shattered the your once tranquil life...")
print("As you step on to the beach, shell shocked, you stare into the vast ocean recollected the pain and anguish that you experienced so quickly. After a while you resolve to get revenge on the pirates who murdered your family. But only could you remember who you are...")
character = commands.create_character()
#stats = commands.class_attributes(character['class'])
#print(stats)
h = character["Health"]
a = character["Attack"]
print(f"Health is {h} and Attack is {a}")
commands.create_weaponname(character['class'])
print("With your memory intact and your gear secured, you begin your trek and can only think of one thing...REVENGE!")
#commands.class_attributes
#character_class = character['class']
#health = commands.class_attributes(character_class)
#attack = commands.class_attributes(character_class)
#scenario 1
print("Scenario 1: As you leave the landing sight, you set off to explore your surroundings. You decide to climb a nearby mountain to get a better vantage point. Once you arrived on top you see a city in the distance. You decide to head there to determine where you are currently located. As you tread through the woods in the direction of the town, you sense a presence tailing you from close by. Suddenly, a silver wolf pounces it at you. It seems thin, suffering from immense hunger. Its blood red eyes stare at you, there is no escape...only one of yall will come out of this alive!")
#Define enemy attributes
#regular_pirate_health = commands.generate_pirate_health("Wolf")
choice = int(input("Press 1 to begin fight: "))
import commands
if choice == 1:
    character_alive = 1
    initial_player_health = h
    player_health = initial_player_health
    #initial_attack = a
    #attack = initial_attack
    initial_attack = (character['Attack'])
    attack = initial_attack


    enemy_health = 25
    enemy_attack = 5
    print(f"Enemy health is: {enemy_health}")
    print(f"Your health is: {player_health}")
    while True:
        print("\nYour turn!")
        player_roll = commands.roll_dice()
        print("You rolled:", player_roll)
        # Calculate player's damage
        #player_damage = attack #commands.player_damage(character['class'], character['Attack'])

        # Inflict damage to enemy
        enemy_health -= attack
        print(f"You dealt {attack} damage to the enemy.")
        print(f"Enemy health is: {enemy_health}")

        if enemy_health <= 0:
            print("You defeated the enemy!")
            #karma += 5
            break

        print("\nEnemy's turn!")
        enemy_roll = commands.roll_dice()
        print("Enemy rolled:", enemy_roll)

        # Calculate enemy's damage
        enemy_damage = enemy_attack #commands.enemy_damage("Regular", character['Attack'])

        # Inflict damage to player
        player_health -= enemy_damage
        print(f"Enemy dealt {enemy_damage} damage to you.")


        if player_health <= 0:
            character_alive = 0
            print("You were defeated by the enemy...")

    print(f"After the fight, your health is: {player_health}")
    character, karma = commands.perform_action(character, karma) #commands.perform_action(character, karma)
    if character_alive == 1:
        karma += 5


    #scenario 2
choice = int(input("Enter 2 to continue: "))
if choice == 2:
    print("Scenario 2: After defeating the wolf, You continue your trek into town. As you approach you see it nestled between ancient, moss-covered trees and enchanted by the soft glow of ethereal orbs. The town is a whimsical fantasy town where cobblestone streets wind through bustling markets filled with magical trinkets and aromatic potions. Towering spires adorned with shimmering crystals pierce the skyline, casting a kaleidoscope of colors upon the vibrant tapestry of this mystical haven where merchants, townfolk, and curious adventurers coexist in harmony. As you head towards the town center, 2 hooded men approached you and offered to take you to a good place that has good deals on wares and souvenirs. You are warry of them but before you could react, they dragged you down a dark alleyway. Once their, they whipped out a pair of daggers each and order you to take off all your valuables or face the consequences. You refuse and prepare for battle.")
    choice = int(input("Enter 3 to begin fight: "))
    if choice == 3:
            #regular_pirate_health = commands.generate_pirate_health("Regular")
            character_alive = 1
            initial_player_health = character['Health']
            player_health = initial_player_health
            initial_attack = character['Attack']
            attack = initial_attack
            enemy_health = 50 #commands.generate_pirate_health("Regular")
            enemy_attack = 5
            print(f"Enemy health is: {enemy_health}")
            print(f"Your health is: {player_health}")
            while True:
                print("\nYour turn!")
                player_roll = commands.roll_dice()
                print("You rolled:", player_roll)
                #player_damage = attack


                enemy_health -= attack #commands.player_damage(character['class'], character['Attack'])
                print("You dealt", attack, "damage to the enemy.")

                if enemy_health <= 0:
                    print("You defeated the enemy!")
                    #karma += 5
                    break

                print("\nEnemy's turn!")
                enemy_roll = commands.roll_dice()
                print("Enemy rolled:", enemy_roll)

                enemy_damage = enemy_attack #commands.enemy_damage("Regular", character['Attack'])

                # Inflict damage to player based on enemy's attack
                player_health -= enemy_damage
                print("Enemy dealt", enemy_damage, "damage to you.")
                print(f"Your health is:{player_health}")

                if player_health <= 0:
                    character_alive = 0
                    print("You were defeated by the enemy...")
                    break
            print("After defeating the hooded men, you sift through their gear for anything of importance. As you take off their hooded robes, you notice a familiar symbol on their arms, a tatted jolly roger. You continue to dig through their wears and find a crumpled up note. On it, it writes ""Meet behind the moonlight tavern on the night of the newmoon, the boss wants a meeting")
            print(f"After the fight, your health is: {player_health}")
            character, karma = commands.perform_action(character, karma) #commands.perform_action(character, karma)
            if character_alive == 1:
                karma += 5

#scenario 3
choice = int(input("Enter 4 to continue: "))
if choice == 4:
    print("Scenario #3: You make your way for the so called, moonlight tavern. Tucked away in the shadows of the city's outskirts, The Moonlight Tavern caters to a crowd of weathered souls, its dimly lit ambiance casting a veil of secrecy over the room. Gruff patrons huddle in worn leather booths, nursing their drinks as the low hum of conversations about gritty adventures and shadowy dealings fills the air, making it a haven for those who thrive in the edgier corners of the realm. On the way there, you check the town board to see what day it was, suprisingly, tonight is the night of the new moon. As it was still daytime, you decide to go into the Tavern itself to kill sometime. Once inside, you take a seat and wait to be servered. As the tavern door swings open with a creak, a menacing figure strides in, clad in tattered leather and sporting a twisted grin. The air tightens as the ruffian locks eyes with you, a challenge simmering in the dangerous glint of their gaze, foreshadowing an imminent clash in the dimly lit confines of The Moonlight Tavern. He walks up and states ""That is my seat you're sitting in there, you must be new here, everyone knows not to touch old me's reserved seat."" You attempt to apologize as to not make a scene but he reveals himself to be the first mate of the Pirate gang. He claimes you tarnished his authority and challenges you to a duel to the death. The tavern falls silent as the patrons watch with bated breath. You stand your ground, ready to face this formidable opponent.")
    character_alive = 1
    initial_player_health = character['Health']
    player_health = initial_player_health
    initial_attack = character['Attack']
    attack = initial_attack

    enemy_health = 100
    enemy_attack = 10
    print(f"Enemy health is: {enemy_health}")
    print(f"Your health is: {player_health}")
    while True:
        print("\nYour turn!")
        player_roll = commands.roll_dice()
        print("You rolled:", player_roll)
        #player_damage = attack


        enemy_health -= attack
        print("You dealt", attack, "damage to the enemy.")

        if enemy_health <= 0:
            print("You defeated the enemy!")
            #karma += 5
            break

        print("\nEnemy's turn!")
        enemy_roll = commands.roll_dice()
        print("Enemy rolled:", enemy_roll)

        # Inflict damage to player based on enemy's attack
        enemy_damage = enemy_attack #commands.enemy_damage("Regular", character['Attack'])

        # Inflict damage to player based on enemy's attack
        player_health -= enemy_damage
        print("Enemy dealt", enemy_damage, "damage to you.")

    if player_health <= 0:
        character_alive = 0
        print("You were defeated by the enemy...")
    else:


        print(f"After the fight, your health is: {player_health}")
        print("After a fierce battle, you emerge victorious over the first mate. The patrons, impressed by your skills, offer you a round of drinks and share tales of their own adventures. You learn more about the town, its inhabitants, and the challenges they face. In the midst of the revelry, you find a drawing of yourself on the first mate's body.")
         #commands.perform_action(character, karma)
        if character_alive == 1:
            karma += 5
            character, karma = commands.perform_action(character, karma)

                        #scenario 4
choice = int(input("Enter 5 to continue: "))
if choice == 5:
    print("Scenario 4: You track down the pirate captain to the dockyards.")
    initial_player_health = character['Health']
    player_health = initial_player_health
    initial_attack = character['Attack']
    attack = initial_attack
    enemy_health = 75
    enemy_attack = 5
    print(f"Enemy health is: {enemy_health}")
    print(f"Your health is: {player_health}")
    while True:
        print("\nYour turn!")
        player_roll = commands.roll_dice()
        print("You rolled:", player_roll)
        #player_damage = attack

        enemy_health -= attack #commands.player_damage(character['class'], character['Attack'])
        print("You dealt", attack, "damage to the enemy.")

        if enemy_health <= 0:
            print("You defeated the enemy!")
            #karma += 5
            break

        print("\nEnemy's turn!")
        enemy_roll = commands.roll_dice()
        print("Enemy rolled:", enemy_roll)

        # Inflict damage to player based on enemy's attack
        enemy_damage = enemy_attack #commands.enemy_damage("Regular", character['Attack'])

        # Inflict damage to player based on enemy's attack
        player_health -= enemy_damage
        print("Enemy dealt", enemy_damage, "damage to you.")

    if player_health <= 0:
        print("You were defeated by the enemy...")
        character_alive = 0
    else:
        print(f"After the fight, your health is: {player_health}")
        print("After a fierce battle, you stand victorious against the pirate captain.")
        if character_alive == 1:
            karma += 5



#scenario 5 (end)

if karma <=6 and character_alive == 1:
    print(f"Your karma was {karma}, scumbag...")
    print("Bad ending: Within your adventure, you were too focused on yourself and failed to see how the citizenry view you as a person.")
    print("They only saw you going about killing and, in doing so, saw that you have no compassion at all.")
    print("They do not wish for you to be their ruler, and upon finding out that you want to go and kill your uncle, the townsfolk ganged up on you and forced you into exile.")
#run bad ending (will define)
elif 6 <= karma <=29 and character_alive == 1:
    print(f"Your karma was {karma}, you weren't such a bad person")
    print(
        "Normal ending: Fueled by the revelation that your uncle, once trusted and familial, had orchestrated a treacherous plot to hire pirates to assassinate your father, the reigning king, a surge of determination courses through your veins.")
    print(
        "Determined to settle the score and avenge your father's death, you look around and spot a dark mare. You mount it and ride off in a hurry with tears and rage flowing out of you.")
    print(
        "You ride all night long to arrive in the Royal Capital. Your palms were sweaty, knees weak, arms were heavy, you were nervous, but on the surface, you were armed and ready.")
    print(
        "As the sun rises, you confront your uncle in the courtyard of the castle. The air is thick with tension as the glow of torches flickers, and the sun casting elongated shadows on the cold stone walls.")
    print(
        "With the weight of betrayal and the crown's destiny on your shoulders, you draw your weapon, prepared for the final, tumultuous clash that will decide the fate of both the kingdom and your family.")#run ok ending (will define later)
elif karma >=30 and character_alive == 1:
    print(f"Your karma was {karma}, you were a true hero")
    print(
        "Best ending: Throughout your adventure, you have gained the hearts of the people. You have spent time in the town, getting to know everyone, learning of their daily struggles, and truly understanding them.")
    print(
        "They have seen your efforts and upon finding out about your origins, banded together and marched alongside you to overthrow your treacherous uncle, crowning you,",
        character['name'], "as the true ruler of Pythor.")
elif character_alive == 0:
    print("GAME OVER, PLEASE RERUN GAME TO START ANOTHER PLAYTHROUGH!")


