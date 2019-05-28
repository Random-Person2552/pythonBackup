import time
import random

'''Text Adventure project created by Jared Smith and Oleg Bychenkov'''

played_before = False
weaponChoice = None
characterChoice = None

# ------------------------- WEAPON CREATION ------------------------------------     

class weapon:
    def __init__(self, name, kill_boss, kill_second):
        self.name = name
        self.kill_boss = kill_boss
        self.kill_second = kill_second

longsword = weapon("Longsword", 'YES', 'YES')
dagger = weapon("Dagger", 'NO', 'NO')
battleAxe = weapon("Battle Axe", 'YES', 'NO')
hammer = weapon("Hammer", 'NO', 'NO')
shortsword = weapon("Shortsword", 'NO', 'NO')
bow = weapon("Bow and Arrow", 'YES', 'YES')
fists = weapon("Fists", 'NO', 'NO')
mace = weapon("Mace", 'YES', 'YES')
    
# ----------------------- CHARACTER CREATION -----------------------------------    
    
class player:
    def __init__(self, name, description, abilities):
        self.name = name
        self.description = description
        self. abilities = abilities    
    
witch = player("Myrna", """Myrna was just a child when she found that she had
magical powers, ranging from being able to summon those that had been lost in 
battle to protecting herself when she was in danger.""", 
"Protected from curses and other harmful objects, can summon warriors")    

knight = player("Artus", """Despite being born in a poor family, Artus mastered 
the mace just as his peers learned to walk. He quickly rose up in ranks and soon 
enough was announced one of the greatest warriors in Fruystin.""", 
"Easy mode, can kill any boss with his mace")

archer = player("Nightmare", """Her real name is unknown, since none of her 
victims survived long enough to tell the story. Her motives are unknown, but 
her skill with the bow is envied by all. You can be considered lucky if you get
to see the arrow before your inevitable demise.""", """Can kill
anything with a bow""")

rogue = player("Crow", """His nickname is enough to describe his personality.
An outcast, a scavenger, someone who believes that one day, he will get lucky. 
The short, hooded figure is easy to underestimate, and you will only realise 
your mistake after he swiftly finds the crack in your armour with his dagger."""
, "Can kill anything with a dagger")

philosopher = player("Scitus", """Scitus always preferred brain over brawn. In
times of need he would pick up a weapon, but always preferred to resolve 
conflicts peacefully. His logic his sword, his discipline his shield, Scitus 
seeks to find the answers to life's deepest questions.""", 
"Able to talk his way out of some situations")

jester = player("Delirus", """Delirus means crazy in Latin. Seems like even his 
parents knew he was worthless. Throughout his life he did not bother to master
a weapon or learn magic, which is why he turned to the life of a jester. One day
he decided to leave his home town to find his destiny, equipped only with his
determination and crazy ideas in mind.""", 
"Hard difficulty character, cannot kill anything")


# ------------------------------ PLAY AGAIN ------------------------------------   
    
def play_again():
    time.sleep(1)
    print "Would you like to play again?"
    playAgain = raw_input("Y or N ")
    playAgain = playAgain.upper()
    if playAgain == "Y":
        characterChange = raw_input("""Would you like to change you character? 
        Y or N. """)
        characterChange = characterChange.upper()
        if characterChange == "Y":
            change_character()
            game_start()
        elif characterChange == "N":
            game_start()
        else:
            play_again()
    elif playAgain == "N":
        print """Thank you for playing our game!"""
    else:
        play_again()
    
def change_character():
    time.sleep(1)
    global characterChoice
    print "Characters:"
    print "Name:"
    print witch.name
    print "Description:"
    print witch.description
    print "Abilities:"
    print witch.abilities
    print ""
    print "Name:"
    print knight.name
    print "Description:"
    print knight.description
    print "Abilities:"
    print knight.abilities
    print ""
    print "Name:"
    print archer.name
    print "Description:"
    print archer.description
    print "Abilities:"
    print archer.abilities
    print ""
    print "Name:"
    print rogue.name
    print "Description:"
    print rogue.description
    print "Abilities:"
    print rogue.abilities
    print ""
    print "Name:"
    print philosopher.name
    print "Description:"
    print philosopher.description
    print "Abilities:"
    print philosopher.abilities
    print ""
    print "Name:"
    print jester.name
    print "Description:"
    print jester.description
    print "Abilities:"
    print jester.abilities
    print ""
    character = raw_input("Select your character! ")
    character = character.upper()
    if character == "MYRNA":
        characterChoice = witch
    elif character == "ARTUS":
        characterChoice = knight
    elif character == "NIGHTMARE":
        characterChoice = archer
    elif character == "CROW":
        characterChoice == rogue
    elif character == "SCITUS":
        characterChoice == philosopher
    elif character == "DELIRUS":
        characterChoice = jester
    else:
        change_character()
    
# ------------------------------- ENDINGS --------------------------------------   
    
def ending_one():
    '''Turn left in the very first room'''
    time.sleep(1)
    print """Before you are able to react, the floor opens up below you and the
    last thing you remember is falling into a pool of lava."""
    play_again()
    
def ending_two():
    '''Fail to beat boss'''
    time.sleep(1)
    print """The Kitidae quickly takes you out. You fall without knowing what
    he was doing in the room or what he was guarding. """
    play_again()
    
def ending_three():
    '''Take cursed treasure'''
    time.sleep(1)
    print """As you greedily stuff treasure into your pockets, you start to 
    feel weird. The next moment you have doubts but it is too late, the curse 
    of greed is already in you and you spend the rest of your days rolling in 
    gold until your inevitable death."""
    play_again()

def ending_four():
    '''Same as ending eight but in a different place, escape without treasure'''
    time.sleep(1)
    print """You sigh out loud, but your will to live is too high and you don't 
    want to risk wasting time or running into a trap. You keep going and find
    an old staircase. It does not seem too stable but with enough caution soon 
    enough you feel a slight breeze on your face. In a couple minutes you walk
    outside and feel the sunlight. You ended up on the side of a mountain. You
    have no idea where you are, or where you should go, but freedom is freedom.
    After months of walking around, you find a village filled with people. You 
    settle there and live a long, but not too prosperous life, and eventually
    death finally comes peacefully to you."""
    play_again()
    
def ending_five():
    '''Join Mr. Brown, create a text adventure'''
    time.sleep(1)
    print """It has been 4 months since you first learned how to program. 
        Now Mr. Brown is asking you to create a Text Adventure Game. You decide
        to create one about a person waking up in a dungeon."""
    play_again()

def ending_six():
    print """You don't feel so good as you completely disappear from reality."""
    play_again()
    
def ending_seven():
    '''Fail to answer troll's riddle'''
    time.sleep(1)
    print """The troll laughs 'I am finally free of this curse!'. The meaning of 
    his words gets to you too late, as you find yourself stuck and unable to 
    leave your post beside the bridge as the troll strolls away to freedom. When
    anyone tries to cross the bridge you ask them the riddle in hopes of 
    escaping the curse, but yet they always answer right. Why do you always get
    the smart ones..."""
    play_again()

def ending_eight():
    '''Escape without taking the treasure'''
    time.sleep(1)
    print """You sigh out loud, but your will to live is too high and you don't 
    want to risk wasting time or running into a trap. You keep going and find
    an old staircase. It does not seem too stable but wish enough caution soon 
    enough you feel a slight breeze on your face. In a couple minutes you walk
    outside and feel the sunlight. You ended up on the side of a mountain. You
    have no idea where you are, or where you should go, but freedom is freedom.
    After months of walking around, you find a village filled with people. You 
    settle there and live a long, but not too prosperous life, and eventually
    death finally comes to you."""
    play_again()
    
def ending_nine():
    time.sleep(1)
    '''Occurs if you escape after taking the treasure'''
    print """You stuff enough treasure to sustain you for the rest of your life,
    if you are to get out alive. Fortune seems to smile upon you as you quickly 
    find stairs that lead you outside. As you feel the sunlight on your skin you
    realise that you are on the side of the mountain, but nevertheless free.
    After months of wandering around, you find a village filled with people. 
    The amount of pure gold you possess allows you to quickly rise up, and soon
    enough the small village became popular and rich enough to be considered
    a city, with you as the founder. You lead a long life full of luxury and 
    success. When you die you still live in the minds of the people for
    centuries, as they raise monuments of you and write about your deeds in
    history books."""
    play_again()
    
def ending_ten():
    '''Travel to the future, become movie star'''
    time.sleep(1)
    print """You feel sudden tiredness, you decide to stay in the room and let
    fate take the wheel. As your vision blurrs momentarily, you find yourself in
    a place with high towers of glass, and people swarming around like ants.
    A person approaches you, his accent is strange, but you understand his 
    words. After a short talk, you find out that the person makes something
    he calls 'movies', which as far as you understand, are plays but shoved
    inside a box for people to see. You decide to go with him and do a couple
    movies. A couple months later the same person comes back and hands you some 
    papers. He calls them 'money', and apprently in this new world you can buy
    anything with them. Since the portal has closed, there's no way back, but 
    you don't complain. People call you a natural at your roles in fantasy 
    movies, and you quickly become popular in this new, unknown world."""
    play_again()
    
def ending_eleven():
    '''Fail to make the underground villagers join you, get lost'''
    time.sleep(1)
    print """As you wander back, trying to find your way to the boss, you
    realise that you have completely lost track of where you are. You scream
    and yell but nobody comes to help you. You spend the rest of your days
    wandering the caves until your death."""
    play_again()
    
# --------------------------------- ROOMS --------------------------------------   
    
def first_room():
    '''Start room, determines the whole following story'''
    print """You wake up in an unknown room, wondering where you are. Looking 
    around, the walls are stone grey and as smooth as can be. The room is lit 
    by a single torch in the middle of the room. Grabbing it and examining the 
    walls, you notice three passages, one ahead of you, one to the left, and 
    one to the right."""
    choice = raw_input("Go FORWARD, LEFT, or RIGHT? ")
    choice = choice.upper()
    if choice == "FORWARD":
        room_one() #find other room, must go forward
    elif choice == "LEFT":
        ending_one()
    elif choice == "RIGHT":
        room_nine() #Find room with two options 
    else:
        first_room()
        
def room_one():
    '''Occurs after walking forward in first room'''
    time.sleep(1)
    print """You walk forward for a while and find yourself in another room, the 
    only thing left to do is keep going forward."""
    room_two()

def room_two():
    '''Result of room one, also major decision as to which events occur'''
    time.sleep(1)
    print """You find yourself in a room eerily similar to the first, but there
    are only two passages now."""
    choice = raw_input("Go FORWARD or RIGHT? ")
    choice = choice.upper()
    if choice == "FORWARD":
        room_three()
    elif choice == "RIGHT":
        room_six()
    else:
        room_two()

def room_three():
    '''Important chice, pick a weapon that will be used later'''
    time.sleep(1)
    print """You walk into a room filled with weapons. You see a longsword, a 
    dagger, a battle axe, a shortsword, a hammer, and a bow."""
    pick_up_weapon = raw_input("Would you like to choose a weapon? Yes or No. ")
    pick_up_weapon = pick_up_weapon.upper()
    global weaponChoice
    if characterChoice == knight:
        print """You already have a weapon, so you continue moving forward."""
        weaponChoice = mace
        room_four()
    if pick_up_weapon == "YES":
        weaponChoice1 = raw_input("What weapon would you like to choose? ")
        weaponChoice1 = weaponChoice1.upper()
        if weaponChoice1 == "LONGSWORD":
            weaponChoice = longsword
            room_four()
        elif weaponChoice1 == "DAGGER":
            weaponChoice = dagger
            room_four()
        elif weaponChoice1 == "BATTLE AXE":
            weaponChoice = battleAxe
            room_four()
        elif weaponChoice1 == "SHORTSWORD":
            weaponChoice = shortsword
            room_four()
        elif weaponChoice1 == "HAMMER":
            weaponChoice = hammer
            room_four()
        elif weaponChoice1 == "BOW":
            weaponChoice = bow
            room_four()
        else:
            room_three()
    elif pick_up_weapon == 'NO':
        weaponChoice = fists 
        room_four()
    else:
        room_three()
    
    
def room_four():
    '''Room that leads to boss fight'''
    time.sleep(1)
    print """As you stumble into the next room you find a Kitidae 
    grinning at you"""
    choice = raw_input("FIGHT the Kitidae or RUN? ")
    choice = choice.upper()
    if choice == "FIGHT":
        fightChoice = "FIGHT"
        Kitidae_fight(fightChoice)
    elif choice == "RUN":
        fightChoice = "RUN"
        print """The Kitidae seemed lazy, but as you try to escape he reaches 
        you in a moment, the fight is inevitable"""
        Kitidae_fight(fightChoice)  #Need a sleep here, prints 4 paragraphs instantly without pausing
    else:
        room_four()
        
def room_five():
    '''Treasure room, leads to 2 different endings'''
    time.sleep(1)
    print """As you enter the door, you find a room full of treasure. You can 
    easily grab some in your pockets and keep moving without any risk.""" 
    choice = raw_input("GRAB the treasure or don't risk it and MOVE on? ")
    choice = choice.upper()
    if choice == "GRAB":
        if characterChoice == witch:
            ending_nine()
        else:
            ending_three()
    elif choice == "MOVE":
        ending_four()
    else:
        room_five()
        
def room_six():
    '''Same as room three but in a different location'''
    time.sleep(1)
    print """You walk into a room filled with weapons. You see a longsword, a 
    dagger, a battle axe, a shortsword, a hammer, and a bow."""
    pick_up_weapon = raw_input("Would you like to choose a weapon? YES or NO. ")
    pick_up_weapon = pick_up_weapon.upper()
    global weaponChoice
    if characterChoice == knight:
        print """You already have a weapon, so you continue moving forward."""
        weaponChoice = mace
        room_seven()
    elif pick_up_weapon == "YES":
        weaponChoice1 = raw_input("What weapon would you like to choose? ")
        weaponChoice1 = weaponChoice1.upper()
        if weaponChoice1 == "LONGSWORD":
            weaponChoice = longsword
            room_seven()
        elif weaponChoice1 == "DAGGER":
            weaponChoice = dagger
            room_seven()
        elif weaponChoice1 == "BATTLE AXE":
            weaponChoice = battleAxe
            room_seven()
        elif weaponChoice1 == "SHORTSWORD":
            weaponChoice = shortsword
            room_seven()
        elif weaponChoice1 == "HAMMER":
            weaponChoice = hammer
            room_seven()
        elif weaponChoice1 == "BOW":
            weaponChoice = bow
            room_seven()
        else:
            room_three()
    elif pick_up_weapon == 'NO':
        weaponChoice = fists 
        room_seven()
    else:
        room_six()
        
def room_seven():
    '''Find Mr.Brown, choose if you want to join or fight'''
    time.sleep(1)
    print """After walking for a few hundred meters, the room suddenly increases
    in size dramaticaly. This is the first room that has been lit by sources 
    other than your torch. In the center of the room sits a throne as high as a 
    house. Thinking about this, you wonder how you even know what a house is. 
    While you are pondering this, a figure multiple times larger than you walks 
    out of the shadows. The torches along the walls throw light on his face. It 
    seems to be Mr. Brown! You don't even know who that is or how you know them, 
    but he is wearing the infinity gauntlet along his left hand."""
    time.sleep(1)
    print """Hello child. It seems you have found my throne room. You have 
    survived longer than I thought you would. For your bravery, I will offer you 
    a choice. Join me in my mission to teach everyone how to program."""
    choice = raw_input("JOIN Mr. Brown in his mission, or try to FIGHT? ")
    choice = choice.upper()
    if choice == "JOIN":
        print """You join Mr. Brown on his mission. That was the right choice. 
        With a wave of his fingers, you are transported to a building that looks
        like a classroom. Here you will learn how to program, along with the 
        other disciples."""
        time.sleep(1)
        ending_five()
    elif choice == "FIGHT":
        brown_fight()
        
def room_nine():
    '''Another room that determines future decisions'''
    time.sleep(1)
    print """After walking for what seems to be eternity, you find yourself in 
    another room. This room is almost identical to the room you woke up in, 
    but when you use the torch to light it up, you see that there are only two 
    passages in this room. You can continue forward, or you can go to the 
    right."""
    choice = raw_input("Continue FORWARD, or go to the RIGHT? ")
    choice = choice.upper()
    if choice == "FORWARD":
       room_ten()
    elif choice == "RIGHT":
        room_seven()
    else:
        room_nine()
        
def room_ten(): 
    '''Troll's riddle, leads to treasure room or a bad ending'''
    time.sleep(1)
    print """This time, you decide to go forward. Soon enough you find a river 
    too fast for you to even attempt to swim over. You look to the side and see 
    a working bridge. The creature guarding it also notices you though. You
    recognize that it is a troll. He doesn't seem aggressive though. He offers
    you to answer his riddle, if you answer it right you will be able to
    pass untouched."""
    choice = raw_input("""What is faster to catch the faster you run? """)
    choice = choice.upper()
    if choice == "BREATH":
        print """The troll sighs with disappointment. 'Why do I always get the 
        smart ones...'. You waste no time to ponder upon his words and quickly
        cross the bridge before he makes up his mind"""
        room_eleven()
    elif characterChoice == witch:
        print """You feel something poking at your aura, but through your 
        knowledge of curses you quickly negate it. The troll seems shocked and
        you use this to your advantage to cross the bridge before the troll 
        can react."""
        room_eleven()
    elif characterChoice == philosopher:
        print """out smart troll cuz nerd"""
        room_eleven()
    else:
        ending_seven()

def room_eleven():
    '''Same as room five but this time there is no cursed ending'''
    time.sleep(1)
    print """As you enter the door, you find a room full of treasure. You can 
    easily grab some in your pockets and keep moving without any risk.""" 
    choice = raw_input("GRAB the treasure or don't risk it and MOVE on? ")
    choice = choice.upper()
    if choice == "GRAB":
        ending_nine()
    elif choice == "MOVE":
        ending_four()
    else:
        room_eleven()

def room_twelve():
    '''Fight, no decisions but different story based on character'''
    time.sleep(1)
    print """After walking through the room, you notice there are weird demon 
    like creatures huddled throughout the room. Trying not to make any noise, 
    you silently observe them, waiting for your time to strike."""
    if characterChoice == knight:
        print """You leap out of the shadows, and start flinging your mace 
        around. You manage to take down almost half of the minions before they 
        know what is happening. Standing your ground, you kill the rest of the 
        minions in no time. There is only one way out of this room, and that is 
        to keep pressing forward."""
        room_thirteen()
        
    elif characterChoice == witch:
        print """Slowly chanting to yourself, the room starts to quake. The 
        ground splits apart, and from the cracks rise up the bodies of those 
        that died in wars past. They overwhelm the demons, swallowing them in 
        their swords and shields. You continue to press forward towards the door
        at the end of the room."""
        room_thirteen()
        
    elif characterChoice == archer:
        print """Popping out of the shadows, you quickly fire your arrows 2 at a 
        time, each one finding their target precisely. Sprinting into the middle
        so as to make sure none survive, you see the entrance to another room, 
        and decide to walk through it."""
        room_thirteen()
        
    elif characterChoice == rogue:
        print """Leaping from the rock you were hidden behind, you dash behind 
        the first of your prey, quickly silencing it before it can alert the 
        others. As it falls the others realize you are there, but you quickly 
        dispatch two more before they can do anything. Finishing the rest, you 
        find a door at the end of the room and enter it."""
        room_thirteen()
    elif characterChoice == philosopher:
        print """Striding into the center of the room, you begin to spout 
        political nonsense. Enthralled, the beasts turn to face you, and form 
        the conclusion that you must be a god. Worshipping you, they step aside
        to reveal the door to the next room, and as you step forward, so do 
        they. It seems you have gained some followers!"""
        room_thirteen()
        
def room_thirteen():
    '''Room after minions, contains a Kitidae that is harder to kill than the rest.'''
    time.sleep(1)
    print """Stepping into the room, an even larger Kitidae appears. He seems to be 
    wearing some type of crude armor, but you think that it will not stop you from
    killing him."""
    fightBossChoice = raw_input("FIGHT the Kitidae or RUN? ")
    fightBossChoice = fightBossChoice.upper()
    if fightBossChoice == 'FIGHT':
        final_boss(fightBossChoice, 2)
    elif fightBossChoice == "RUN":
        room_fifteen(fightBossChoice)
    else:
        room_thirteen()
        
        
def room_fourteen(fightBossChoice):
    '''Time travel machine room when you can stay to go to the future or leave'''
    time.sleep(1)
    print """As the Kitidae falls, the room suddenly transforms. The door starts
    closing behind you as you see something sparking a foot away from you"""
    choice = raw_input("RUN out while you have a chance or STAY? ")
    choice = choice.upper()
    if choice == "RUN":
        room_fifteen(fightBossChoice)
    elif choice == "STAY":
        ending_ten()
    
def room_fifteen(fightBossChoice):
    '''Underground village system ask for help to fight boss'''
    time.sleep(1)
    print """While you are walking away, the cave system you are walking through 
    suddenly increases in size, and houses made out of stone begin to come into 
    focus. """
    if fightBossChoice == "RUN":
        print """You decide to ask the locals for help killing the Kitidae that 
        you saw with the armor."""
        getHelp = random.randint(1, 2)
        if getHelp == 1:
            print """Either your persuasion, or the villagers' curiousness did 
            it's job. They quickly grab their pitchforks and get ready to face
            the Kitidae."""
            final_boss(fightBossChoice, getHelp)
        else:
            print """The villagers look upon you in doubt. You don't look
            convincing enough. One of them grabs his pitchfork and threatens
            you. Not looking for conflict, and clearly understanding that you
            won't be able to get their help, you decide to head back alone."""
            ending_eleven()
# ---------------------------------- BOSSES ------------------------------------

def Kitidae_fight(fightChoice):
    '''Boss fight function, determines if the character you chose has any special abilites,
    if the weapon you chose can kill the Kitidae, or if you chose to fight the Kitidae or run,
    before determining what the next part of the story is.'''
    time.sleep(1)
    if fightChoice == "FIGHT":
        if characterChoice == knight:
            print """You swing your mace at the Kitidae before it can reach you, instantly killing it. 
            looking past, you find the door to the room that he must have been guarding."""
            room_five()
        elif characterChoice == witch:
            if weaponChoice == fists:
                print """You spin a curse with your magic, killing the Kitidae where it stands 
                before it even knew what hit it. As it falls, you see the door to the 
                room it must have been keeping safe."""
                room_five()
            else:
                print "Reaching for the", weaponChoice.name, """that you chose, you 
                stumble, and the Kitidae is able to reach you first."""
                ending_two()
        elif characterChoice == archer:
            if weaponChoice == bow:
                print """You kill the Kitidae with your bow before it can turn around
                to face you. As it falls, the door behind it appears. """
                room_five()
            else:
                print """You should have picked up that bow when you had the chance.
                reaching for your""", weaponChoice.name, """it feels unfamiliar and
                you do not know how to wield it. The Kitidae quickly overwhelms you, killing
                you instantly."""
        elif characterChoice == rogue:
            if weaponChoice == dagger:
                print """Due to your mastery of the dagger, you are able to quickly
                dash behind the Kitidae and find his weak points, then drop behind to dodge
                his attacks from how mobile your training made you. You quickly defeat
                the Kitidae without even so much as a scratch."""
            else:
                print """Maybe you should have picked the dagger, or focused on another
                weapon when you were training."""
                ending_two()
        elif characterChoice == philosopher:
            if weaponChoice.kill_boss == "YES":
                print """Your wiseness led you to pick the right weapon. Even though 
                you never trained in a weapon, the knowledge of how to use it 
                seems to flow through you. You are able to drop the Kitidae without a 
                second thought."""
                room_five()
            else:
                print """Maybe you aren't as wise as you thought you are. The 
                puny weapon you chose does nothing against the Kitidae."""
        elif characterChoice == jester:
            print """What did you expect?"""
            ending_two()
            
    else:
        if characterChoice == knight:
            print """You swing your mace at the Kitidae before it can reach you, 
            instantly killing it. looking past, you find the door to the room 
            that he must have been guarding."""
            room_twelve()
        elif characterChoice == witch:
            if weaponChoice == fists:
                print """You spin a curse with your magic, killing the Kitidae 
                where it stands before it even knew what hit it. As it falls, 
                you see the door to the room it must have been keeping safe."""
                room_twelve()
            else:
                print "Reaching for the", weaponChoice.name, """that you chose, you 
                stumble, and the Kitidae is able to reach you first."""
                ending_two()
        elif characterChoice == archer:
            if weaponChoice == bow:
                print """You kill the Kitidae with your bow before it can turn around
                to face you. As it falls, the door behind it appears. """
                room_twelve()
            else:
                print """You should have picked up that bow when you had the chance.
                reaching for your""", weaponChoice.name, """it feels unfamiliar and
                you do not know how to wield it. The Kitidae quickly overwhelms you, killing
                you instantly."""
        elif characterChoice == rogue:
            if weaponChoice == dagger:
                print """Due to your mastery of the dagger, you are able to quickly
                dash behind the Kitidae and find his weak points, then drop 
                behind to dodge his attacks from how mobile your training made you. 
                You quickly defeat the Kitidae without even so much as a scratch."""
            else:
                print """Maybe you should have picked the dagger, or focused on another
                weapon."""
                ending_two()
        elif characterChoice == philosopher:
            if weaponChoice.kill_boss == "YES":
                print """Your wiseness led you to pick the right weapon. Even though 
                you never trained in a weapon, the knowledge of how to use it 
                seems to flow through you. You are able to drop the Kitidae without a 
                second thought."""
                room_twelve()
            else:
                print """Maybe you aren't as wise as you thought you are. The 
                puny weapon you chose does nothing against the Kitidae."""
        elif characterChoice == jester:
            print """What did you expect?"""
            ending_two()

def final_boss(fightBossChoice, getHelp):
    '''Final Kitidae fight, Kitidae is harder than the first one'''
    time.sleep(1)
    if characterChoice == knight:
        print """You were right in your assumptions. Your mace quickly breaks 
        through the weak armor of the Kitidae."""
        room_fourteen(fightBossChoice)
    if fightBossChoice == "FIGHT":
        if weaponChoice.kill_second == 'YES':
            print """Looks like you chose well! The""", weaponChoice.name, """
            is able to kill the Kitidae before it can turn to face you. That armor 
            that is was wearing does nothing to stop your""", weaponChoice.name, """
            from piercing it."""
            room_fourteen(fightBossChoice)
        elif weaponChoice.kill_second == 'NO':
            ending_two()
    elif getHelp == 1:
        print """With the help of the villagers you quickly overwhelm it and
        through sheer numbers the fight is over in minutes.."""
    else: 
        room_fifteen(fightBossChoice)


def brown_fight():
    '''Fighting Mr. Brown with the infinity gauntlet'''
    time.sleep(1)
    print """You become distracted by the infinity gauntlet resting on Mr. Brown's
    left hand. Wanting it for your own, you decide to attack him. As you ready 
    your""", weaponChoice.name, """you must decide where you want to attack 
    Mr. Brown."""
    attackChoice = raw_input("Attack the HEAD, or the BODY? ")
    attackChoice = attackChoice.upper()
    if attackChoice == "HEAD":
        print """That was the wrong choice, child. Mr. Brown snaps."""
    elif attackChoice == "BODY":
        print """You should have aimed for the head. Mr. Brown snaps."""
    ending_six()

# -------------------------- GAME START ----------------------------------------       
        
def game_start():
    '''Runs instantly when the file is ran, starts the game and initiated 
    first room. Uses the played_before to only ask to change the character the 
    first time it is played.'''
    global played_before
    if played_before == False:
        change_character()
        played_before = True
        first_room()
    elif played_before == True:
        first_room()
        
game_start()