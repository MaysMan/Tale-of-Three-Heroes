print("Welcome to the Quest of the Three Heroes!")
print("Use the corresponding numbers to make choices.")
print("Good luck!")
print('''                                                     o
                                                 _---|         _ _ _ _ _
                                              o   ---|     o   ]-I-I-I-[
                             _ _ _ _ _ _  _---|      | _---|    \ ` ' /
                             ]-I-I-I-I-[   ---|      |  ---|    |.   |
                              \ `   '_/       |     / \    |    | /^\|
                               [*]  __|       ^    / ^ \   ^    | |*||
                               |__   ,|      / \  /    `\ / \   | ===|
                            ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
                            I_I__I_I__I_I  (====(_________)___|_|____|____
                            \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_|
                             |[]      '|   | []  |`__  . [  \-\--|-|--/-/
                             |.   | |' |___|_____I___|___I___|---------|
                            / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] |
                           <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \
                           ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===>
                           ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [
                           <===>     ' ||||| |   |   | ||||.||  []   <===>
                            \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/
                             |      . _||||| |   |   | ||||.|| |     | |
                          ../|' v . | .|||||/____|____\|||| /|. . | . ./
                           |//\............/...........\........../../\\\)''')
print("You find yourself walking upon the great gates of the palace of Elmswood.")
print("the palace is surrounded by a moat and the only way to enter is through the drawbridge.")
print("You are faced with your first decision on this great quest.")
print("1. Do you turn around and leave?")
print("2. Do you try to enter the palace?")
if 1 == int(input()):
    print("You turn around and leave. The evil wizard Zoltar lays seige to the city and you are burned alongside its people.")
    exit()
else:
    print("You approach the drawbridge. The guards recognize you as a chosen hero and opent the gates.")
    print("You enter the palace and are greeted by the king.")
    print("The king tells you that the kingdom of Elmswood is in danger and that the princess has been taken.")
    print("You are tasked with rescuing the princess and defeating the evil wizard Zoltar.")
    print("The king asks what kind of hero you are.")
    print("1. A Palidin who fights for justice.")
    print("2. A rogue who uses stealth and cunning.")
    print("3. A mage who uses magic to defeat their foes.")
    #this is where the code breaks into different hero's paths
    hero = input("What kind of hero are you?")
    if hero == str(1):
        print('''     /'
     ||
     ||      ** *
     ||      __X_
     ||     ( ___\
     ||     |:  \\
    ><><  ___)..:/_#__,
    (X|) (|+(____)+\ _)
     o|_\/>> + + + << \
       |:\/|+ + + +| \_\<
       \./  XXXXXX.  (o_)_
           /+ + + |   \:|
          /+ +/+ +|  -/->>>----.
         /+ +|+ /XX /   _--,  _ \
        \+ + + /  |X   (,\- \/_ ,
        /\+ + /\  |X \    /,//_/
       +_+_+_( )o_)X  \  (( ///
        (_o(  /__/ X   \  \\//
         \_|  |_/  X    \ ///
         \_| >(_/        \,/
    ,////__o\ /__////,    V ''')
        print('''The king gives you a sword and shield and sends you on your way.
        You are now equiped with a holy sword and a shield of light.
        You are ready to face the evil wizard Zoltar.
        You leave the palace and head towards the dark forest where Zoltar is hiding.''')
        print("")
        print("You enter the forest. The sun is blocked out by the thick trees. Without sight, you are in danger of monster attacks.")
        print("1. Do you light a torch to see?")
        print("2. Do you continue without light?")
        print("3. Do you use your shield of light to guide you?")
        choice = input("What will you do?")
        if choice == str(1):
            print(" ")
            print("You light a torch and every monster in the proximity is alerted to your presence.")
            print("You are attacked by a group of goblins and are killed.")
            exit()
        if choice == str(2):
            print(" ")
            print("You continue without light and are attacked by a group of goblins.")
            print("You are killed.")
            exit()
        if choice == str(3):
            print(" ")
            print("You use your shield of light to guide you through the forest.")
            print("Your shield blasts away the darkness and all its viel creatures.")
            print("guided by holy light, you see a glistening red stone embedded in the ground.")
            print("1. Do you take the stone?")
            print("2. Do you leave it?")
            choice = input("What will you do?")
            if choice == str(1):
                print(" ")
                print("You take the stone and it begins to glow with a red light.")
                print("You are filled with a sense of power and strength.")
                print("You continue on your way to Zoltar's lair.")
                print("When you arrive at a bridge, you are faced with a troll.")
                print("The troll demands a toll to cross the bridge. Being a holy paladin, you never had much need for coin.")
                print("the troll attacks you and you are forced to fight.")
                print(" ")
                print("1. Do you use your sword to fight the troll?")
                print("2. Do you turn tail and run?")
                choice = input("What will you do?")
                if choice == str(1):
                    print(" ")
                    print("You fight the troll and are victorious due to the enhanced stats you recieved from the stone.")
                    print("You cross the bridge and continue on your way to Zoltar's lair.")
                    print("You arrive at Zoltar's lair. The door has been flung open and the remains of the other heroes have been left to rot.")
                    print("You enter the lair and are faced with Zoltar. Zolatar is a powerful wizard. You can feel his evil aura radiate through your armor.")
                    print("1. Do you charge Zoltar with your sword?")
                    print("2. Do you use your shield of light to protect yourself from his evil aura?")
                    choice = input("What will you do?")
                    if choice == str(1):
                        print(" ")
                        print("You charge Zoltar and are struck down by a bolt of lightning.")
                        print("Nothing remains of your body. Just a pile of ash and your once great shield.")
                        print("You have fail")
                        exit()
                    if choice == str(2):
                        print(" ")
                        print("You use your shield of light to protect yourself from Zoltar's evil aura.")
                        print("Zoltar is weakened by the shield and fails to cast his lightning spell. You strike Zoltar down with you mighty sword")
                        print("Zoltar is defeated and the princess is saved.")
                        print("You have completed your quest.")
                        exit()
                if choice == str(2):
                    print("You turn tail and run. The troll catches up to you and kills you.")
                    exit()
            if choice == str(2):
                print("You leave the stone and continue on your way to Zoltar's lair.")
                print("When you arrive at a bridge, you are faced with a troll.")
                print("The troll demands a toll to cross the bridge. Being a holy paladin, you never had much need for coin.")
                print("the troll attacks you and you are forced to fight.")
                print("1. Do you use your sword to fight the troll?")
                print("2. Do you turn tail and run?")
                choice = input("What will you do?")
                if choice == str(1):
                    print("You fight the troll. The troll rips off your arms and impales you with them")
                    print("You have died in a bloody mess.")
                    exit()
    if hero == str(2):
        print(" The king gives you a dagger and a cloak and sends you on your way.")
        print("You are now equiped with a snake venom dagger and a cloak of shadows.")
        print("You are ready to face the evil wizard Zoltar.")
        print("You leave the palace and head towards the dark forest where Zoltar is hiding.")
        print(" ")
        print("You enter the forest. The sun is blocked out by the thick trees. Without sight, you are in danger of monster attacks.")
        print("1. Do you light a torch to see?")
        print("2. Do you use your cloak of shadows to hide?")
        print("3. Do you continue without light?")
        choice = input("What will you do?")
        if choice == str(1):
            print(" ")
            print("You light a torch and every monster in the proximity is alerted to your presence.")
            print("You are attacked by a group of goblins and are killed.")
            exit()
        if choice == str(2):
            print(" ")
            print("You use your cloak of shadows to hide in the darkness.")
            print("You are able to sneak past the goblins and continue on your way to Zoltar's lair.")
            print("You arrive at a bridge, you are faced with a troll.")
            print("The troll demands a toll to cross the bridge. Being a rogue, you're as broke as broke can get.")
            print("The troll attacks you and you are forced to fight.")
            print(" ")
            print("1. Do you use your dagger to fight the troll?")
            print("2. Do you turn tail and run?")
            choice = input("What will you do?")
            if choice == str(1):
                print(" ")
                print("You fight the troll and are no match for his ferocius onslaught. He wails his club and tears you limb from limb.")
                print("You have died a bloody death.")
                exit()
            if choice == str(2):
                print("You turn tail and run. The troll has no hope of catching up with you. As a rogue, you are used to a chase.")
                print("You outrun the troll and continue on your way to Zoltar's lair.")
                print("You arrive at Zoltar's lair. The door has been flung open and the remains of the other heroes have been left to rot.")
                print("You enter the lair and are faced with Zoltar. Zolatar is a powerful wizard. You can feel his evil aura radiate through your cloak.")
                print("1. Do you charge Zoltar with your dagger?")
                print("2. Do you use your cloak of shadows to hide from Zoltar?")
                choice = input("What will you do?")
                if choice == str(1):
                    print(" ")
                    print("You charge Zoltar and are struck down by a bolt of lightning.")
                    print("Nothing remains of your body. Just a pile of ash and your once great cloak.")
                    print("You have failed")
                    exit()
                if choice == str(2):
                    print(" ")
                    print("You use your cloak of shadows to hide from Zoltar.")
                    print("Zoltar is unable to see you and you are able to sneak up behind him and stab him in the back.")
                    print("Zoltar fumbles around shooting lighting in every direction. Eventually his movements slow and Zoltar falls to the floor dead.")
                    print("Zoltar is defeated and the princess is saved.")
                    print("You have completed your quest.")
                    exit()
            if choice == str(3):
                print("You continue without light and trip over a red stone poking out of the ground.")
                print("You fall down a small hill and are impaled on a tree branch.")
                print("You have died")
                exit()
    if hero == str(3):
        print('''             _,._      
  .||,       /_ _\\     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-'\"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | >-'' _,\\ 
   ||'      ==\ ,-'  ,' 
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 
   ||       |     |    \
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/       
   ||''')
        print("The king gives you a magical tome and fire magic infused robes. Then he sends you on your way.")
        print("You are now equiped with a magical tome and a staff of the elements.")
        print("You are ready to face the evil wizard Zoltar.")
        print("You leave the palace and head towards the dark forest where Zoltar is hiding.")
        print(" ")
        print("You enter the forest. The sun is blocked out by the thick trees. Without sight, you are in danger of monster attacks.")
        print("1. Do you light a torch to see?")
        print("2. Do you burn down the forest?")
        print("3. Do you continue without light?")
        choice = input("What will you do?")
        if choice == str(1):
            print(" ")
            print("You light a torch and every monster in the proximity is alerted to your presence.")
            print("You are attacked by a group of goblins and are killed.")
            exit()
        if choice == str(2):
            print(" ")
            print("You burn down the forest and all the goblins within it.")
            print("However, you too were brought down in the blaze. Nothing remains but a pile of ash and the tools the king left you")
            print("You are dead")
            exit()
        if choice == str(3):
            print(" ")
            print("You continue without light and are attacked by a group of goblins.")
            print("The goblins strike but your robes defend you with fire magic")
            print("You are able to defeat the goblins and continue on your way to Zoltar's lair.")
            print(" ")
            print("  You arrive at a bridge, you are faced with a troll.")
            print("The troll demands a toll to cross the bridge. Being brought up in wealth you have plenty of coin to toss around.")
            print("The troll steps aside and lets you pass.")
            print("You cross the bridge and continue on your way to Zoltar's lair.")
            print("You arrive at Zoltar's lair. The door has been flung open and the remains of the other heroes have been left to rot.")
            print("You enter the lair and are faced with Zoltar. Zolatar is a powerful wizard. You can feel his evil aura radiate through your robes.")
            print(" ")
            print(" ")
            print("1. Do you cast elemental magic at Zoltar?")
            print("2. Do you allow your fire robes to defend you?")
            choice = input("What will you do?")
            if choice == str(1):
                print(" ")
                print("You cast elemental magic at Zoltar. Zoltar is a wizard of great power; however, he relies on his lightning magic too much.")
                print("You casted a hurricane of water and when Zoltar cast his lightning, you water spell was amplified.")
                print("Zoltar is struck down by his own magic.")
            if choice == str(2):
                print(" ")
                print("You allow your fire robes to defend you, but Zoltar's lightning spell his too strong.")
                print("You are struck down by a bolt of lightning.")
                print("You have died")
                exit()
                