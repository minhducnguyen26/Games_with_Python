# Game Information
'''
    Author: Minh Nguyen
    Title: The Tail of Brigade and The Brave Hero
    Game Description: Saving the world of Brigade by collecting 5 natural elements to defeat the Lord of Darkness.
'''

# Record Definitions
'''
Records:
    World:
        status (str): Whether or not the game is "playing", "won",
                      "quit", or "lost". Initially "playing".
        map (dict[str: Location]): The lookup dictionary matching 
                                   location names to their
                                   information.
        player (Player): The player character's information.
      
    Player:
        location (str): The name of the player's current location.
        inventory (list[str]): The player's collection of items.
                               Initially empty.
 
    Location:
        about (str): A sentence that describes what the current 
                     location looks like.
        neighbors (list[str]): A list of the names of other places 
                               that the player can reach from the 
                               current location.
        stuff (list[str]): A collection of things available at 
                           the current location.
'''

# Core Game Functions
def render_introduction():
    '''
    Create the message to be displayed at the beginning of the game.
    
    Returns:
        str: The introductory text of the game to be displayed.
    '''
    name = input("Welcome player, what is your name? ")
    instruction = "\n" \
               "Welcome, " + name + ", you are on a quest to save Brigade, a wonderful world of peace, beauty, and happiness. \n" \
               "\n" \
               "It all started 5 months ago ...\n" \
               "\n" \
               "Brigade was long known as a perfect world where people lived with each other in harmony. \n"\
               "However, happiness did not last very long. \n" \
               "One day, the world was threatened by Dominato, the Lord of Darkness. \n" \
               "Dominato was a powerful being, and he planned to destroy Brigade. \n"\
               "Many brave knights and soldiers from all around the world had come and challenged him, yet, none had succeeded. \n" \
               "In order to stop the Lord of Darkness, there is only one way: \n"\
               "'One must collect 5 natural elements: Fire, Water, Earth, Wood, and Metal. \n"\
               "The power from those 5 elements would summon the mighty Humblo – Lord of the Light.' \n" \
               "The legend told that only light could defeat darkness, and only Humblo could stop the ambition of Dominato. \n" \
               "\n" \
               "You, " + name + ", are the chosen one to collect the 5 natural elements and defeat the Lord of Darkness. \n" \
               "Will the world be saved, or will it be destroyed? It all depends on you. \n" \
               "Good luck, brave hero! \n"       
    
    return instruction

def create_world():
    '''
    Creates a new version of the world in its initial state.
    
    Returns:
        World: The initial state of the world
    '''

    world = {"status" : "playing",
            
            "player"  : {"location" : "village",
                       "inventory" : []},
            
            "map"     : [

                {"location" : "village",
                "about" : "You find yourself in a small village named Barbell of Brigade. \n" \
                          "Your mission is to collect all 5 natural elements.",
                "neighbors" : ["volcano","ocean","plain","forest","castle","battlefield"],
                "stuff" : []},

                {"location" : "volcano",
                "about" : "You have arrived to the powerful volcano called Sudo. \n"\
                          "You will find the FIRE element here, but be careful \n" \
                          "for no normal person could stand the heat of this place." ,
                "neighbors" : ["volcano","ocean","","","","","village"],
                "stuff" : ["GET THE FIRE ELEMENT"]},

                {"location" : "ocean",
                "about" : "You have arrived to the deepest and most mysterious ocean in the world, Incorel. \n" \
                          "Here, you will find the WATER element, but remember, the ocean is not friendly \n" \
                          "to those who come with a greedy heart. Only take what you need!",
                "neighbors" : ["volcano","ocean","plain","","","",""],
                "stuff" : ["GET THE WATER ELEMENT","GET THE OCEAN KING'S TRIDENT"]},

                {"location" : "plain",
                "about" : "You continue on your adventure, and you see in front of your eyes an immense and lively plain named Vidia. \n" \
                          "This is the most peaceful and beautiful place in Brigade for it is protected by the Spirit of Life and Cultivation. \n"\
                          "Here, you will find the EARTH element, as well as delicious foods, and a one of a kind scenery.",
                "neighbors" : ["","ocean","plain","forest","","",""],
                "stuff" : ["GET THE EARTH ELEMENT"]},

                {"location" : "forest",
                "about" : "You have successfully found the way to Jupbelus, the forest of the truth. \n" \
                          "You need to get the WOOD element, but be cautious, only those who seek the element \n" \
                          "for the sake of everybody but themselves are worthy to lay their hands on it.",
                "neighbors" : ["","","plain","forest","","","village"],
                "stuff" : ["GET THE WOOD ELEMENT"]},

                {"location" : "castle",
                "about" : "You have arrived to Ovolen, the haunted castle. \n" \
                          "The former owner of this castle stole the METAL element and used it to turn his army into monsters. \n" \
                          "However, he could not stand the power of the METAL element, and he vanished, leaving behind his army. \n"\
                          "The METAL element is guarded by the monsters.",   
                "neighbors" : ["","","","","castle","","village"],
                "stuff" : ["RUN AWAY","FIGHT THE MONSTERS"]},

                {"location" : "battlefield",
                "about" : "You are at Xeneelk, also known as the Valley of the End, where the biggest battle of your life will take place. \n" \
                          "Dominato, the Lord of Darkness, is here and he is ready to put an end to Brigade. \n" \
                          "Will the world be safe, or will it be destroyed? Only you can decide.",
                "neighbors" : ["","","","","","battlefield","village"],
                "stuff" : ["SUMMON HUMBLO"]},
                    
                    ]
            }

    return world

def render(world):
    '''
    Consumes a world and produces a string that describe the current state of the world.
    
    Args:
        world (World): The current world to describe.
    
    Returns:
        str: A textual description of the world.
    '''
    
    loc = world["player"]["location"]
    for xdict in world["map"]:
        if xdict["location"] == loc:
            about = "===================================== \n" + xdict["about"]+"\n"
            for item in xdict["stuff"]:
                if item not in world["player"]["inventory"]:
                    about = about
            about = about + "====================================="
            return about
    return "error"

def get_options(world):
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.
    
    Args:
        world (World): The current world to get options for.
    
    Returns:
        list[str]: The list of commands that the user can choose from.
    '''

    loc = world["player"]["location"]
    options = []
            
    if loc == "village":
        options.append("GO TO THE VOLCANO")
        options.append("GO TO THE BATTLEFIELD")
        options.append("GO TO THE FOREST")
        options.append("GO TO THE CASTLE")
        
    if loc == "volcano":
        options.append("GO TO THE OCEAN")
        options.append("GO TO THE VILLAGE")
        
    if loc == "ocean":
        options.append("GO TO THE PLAIN")
        options.append("GO TO THE VOLCANO")
        
    if loc == "plain":
        options.append("GO TO THE FOREST")
        options.append("GO TO THE OCEAN")
        options.append("TREAT MYSELF WITH SOME FOOD")
        
    if loc == "forest":
        options.append("GO TO THE VILLAGE")
        options.append("GO TO THE PLAIN")
        
    if loc == "castle":
        options.append("GO TO THE VILLAGE")
        
    if loc == "battlefield":
        options.append("GO TO THE VILLAGE")   
        
    for xdict in world["map"]:
        for item in xdict["stuff"]:
            if xdict["location"] == loc and item not in world["player"]["inventory"]:
                options.append(item)
    options.append("QUIT")
    return options

def update(world, command):
    '''
    Consumes a world and a command and updates the world according to the
    command, also producing a message about the update that occurred.
    This function modify the world given, not producing a new one.
    
    Args:
        world (World): The current world to modify.
    
    Returns:
        str: A message describing the change that occurred in the world.
    '''
    
    loc = world["player"]["location"]
    
    if command == "QUIT":
        world["status"] = "quiting"
        return("\nAt least you had a choice, unlike the poor people of Brigade.")
    
    # Command to go to different places
    elif command == "GO TO THE VOLCANO":
        for xdict in world["map"]:
            if xdict["location"] == loc:
                world["player"]["location"] = xdict["neighbors"][0]
    elif command == "GO TO THE OCEAN":
        for xdict in world["map"]:
            if xdict["location"]  == loc:
                world["player"]["location"] = xdict["neighbors"][1]
    elif command == "GO TO THE PLAIN":
        for xdict in world["map"]:
            if xdict["location"]  == loc:
                world["player"]["location"] = xdict["neighbors"][2]
    elif command == "GO TO THE FOREST":
        for xdict in world["map"]:
            if xdict["location"]  == loc:
                world["player"]["location"] = xdict["neighbors"][3]
    elif command == "GO TO THE CASTLE":
        for xdict in world["map"]:
            if xdict["location"]  == loc:
                world["player"]["location"] = xdict["neighbors"][4]
    elif command == "GO TO THE BATTLEFIELD":
        for xdict in world["map"]:
            if xdict["location"]  == loc:
                world["player"]["location"] = xdict["neighbors"][5]
    elif command == "GO TO THE VILLAGE":
        for xdict in world["map"]:
            if xdict["location"] == loc:
                world["player"]["location"] = xdict["neighbors"][6]
    
    # Command of actions - WIN path
    elif command == "GET THE FIRE ELEMENT":
        world["player"]["inventory"].append("GET THE FIRE ELEMENT")
        return("\nThe FIRE element is added to your inventory. \n")
    elif command == "GET THE WATER ELEMENT":
        world["player"]["inventory"].append("GET THE WATER ELEMENT")
        return("\nThe WATER element is added to your inventory. \n")
    elif command == "GET THE EARTH ELEMENT":
        world["player"]["inventory"].append("GET THE EARTH ELEMENT")
        return("\nThe EARTH element is added to your inventory. \n")
    elif command == "GET THE WOOD ELEMENT":
        world["player"]["inventory"].append("GET THE WOOD ELEMENT")
        return("\nThe WOOD element is added to your inventory. \n")
    elif command == "FIGHT THE MONSTERS":
        world["player"]["inventory"].append("FIGHT THE MONSTERS")
        world["player"]["inventory"].append("RUN AWAY")
        return("\nYou have proven your bravery and defeated the army of monsters. The METAL element comes to you. \n")
    elif command == "SUMMON HUMBLO":
        if "GET THE FIRE ELEMENT" and "GET THE WATER ELEMENT" and "GET THE EARTH ELEMENT" and "GET THE WOOD ELEMENT" and "FIGHT THE MONSTERS" not in world["player"]["inventory"]:
            world["status"] = "lose"
            return("\nYou do not have all 5 natural elements. Without them, you are not ready to face Dominato. \nYou return to Barbell, but too bad, he saw you.")
        else:
            world["status"] = "win"
            
    # Command of actions - LOSE path
    elif command == "GET THE OCEAN KING'S TRIDENT":
        world["status"] = "lose"
        return("\nYou have taken what does not belong to you. The ocean shows its wrath, and that is the last time people see you.")
    elif command == "RUN AWAY":
        world["status"] = "lose"
        return("\nToo bad, the monsters did not let you leave that easily.")
    
    # Additional command (does not affect the storyline)
    elif command == "TREAT MYSELF WITH SOME FOOD":
        world["player"]["inventory"].append("TREAT MYSELF WITH SOME FOOD")
        return("\nThe food is indeed delicious. \n")
    return ""

def render_ending(world):
    '''
    Create the message to be displayed at the end of the game.
    
    Args:
        world (World): The final world state to use in describing the ending.
    
    Returns:
        str: The ending text of the game to be displayed.
    '''

    if world["status"] == "win":
        return("With all 5 natural elements, you summon Humblo. \nThe power of the Lord of the Light destroys Dominato. \nCongratualtions, you have saved Brigade, and once again, the beautiful world remains beautiful. \nYOU WON")
    if world["status"] == "lose":
        return("GAME OVER \n")
    else:
        return("From that day, the beautiful land of Brigade is destroyed by Dominato.\nGAME OVER")

def choose(options):
    '''
    Consumes a list of commands, prints them for the user, takes in user input
    for the command that the user wants (prompting repeatedly until a valid
    command is chosen), and then returns the command that was chosen.
    
    Args:
        options (list[str]): The potential commands to select from.
    
    Returns:
        str: The command that was selected by the user.
    '''

    print("Your current options are:")
    for i in range(len(options)):
        print("     " + options[i])
    while True:
        command = input("What do you want to do? ")
        command = command.upper()
        if command in options:
            break
        else:
            print("That does no seem to be an option at this point.")

    return command

def main():
    '''
    Run the game using the Text Adventure console engine.
    Consumes and produces nothing, but prints and indirectly takes user input.
    '''
    print(render_introduction())
    world = create_world()
    while world['status'] == 'playing':
        print(render(world))
        options = get_options(world)
        command = choose(options)
        print(update(world, command))
    print(render_ending(world))
    print("")
    
    while input('Type "PLAY" to play again, or press ENTER to quit. ').upper() == "PLAY":
        print(render_introduction())
        world = create_world()
        while world['status'] == 'playing':
            print(render(world))
            options = get_options(world)
            command = choose(options)
            print(update(world, command))
        print(render_ending(world))
    
if __name__ == '__main__':
    main()