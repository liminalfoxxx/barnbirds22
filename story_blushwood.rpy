# Dove flags
default dove_soda_received = False
default dove_soda_thanked = False
default dove_asked_who = False
default dove_asked_doing = False
default dove_asked_blight = False
default dove_asked_soda = False
default dove_asked_organic = False
default dove_asked_chorus = False
default dove_starlight = False
default dove_asked_kingsnake = False
default dove_asked_death = False
default dove_asked_11 = False
default dove_talked_scarlet = False
default dove_asked_scarlet = False
default dove_asked_dc = False

# Seagull flags
default seagull_asked_here = False
default seagull_asked_blight = False
default seagull_asked_dying = False
default seagull_asked_dead = False
default seagull_asked_her = False
default seagull_asked_infected = False
default seagull_asked_toucan = False

# Scarlet flags
default scarlet_still_alive = False
default scarlet_asked_dead = False
default scarlet_asked_aware = False
default scarlet_asked_blight = False
default scarlet_asked_cleric = False

# Crow conversation flags
default crow_asked_who = False
default crow_asked_bird = False
default crow_asked_blight = False
default crow_asked_blushwood = False
default crow_asked_glamor = False
default crow_asked_kingsnakes = False

# Toucan conversation flags
default toucan_first = False
default toucan_asked_who = False
default toucan_asked_dying = False
default toucan_asked_scarlet = False
default toucan_asked_hummingbird = False
default toucan_asked_kingsnake = False
default toucan_asked_blight = False

# Hummingbird flags
default hum_asked_arcade = False
default hum_asked_aerospace = False
default hum_asked_blight = False
default hum_asked_blushwood = False
default hum_asked_fae = False
default hum_hacked = False
default arcade_hacked = False

# Secretary flags
default sec_asked_enemy = False
default sec_asked_name = False
default sec_asked_who = False
default sec_asked_blight = False
default sec_asked_federal = False
default heron_sec = False

# Ptarmigan flags
default pta_asked_who = False
default pta_asked_blight = False
default pta_asked_cabin = False
default pta_asked_what = False
default pta_asked_help = False

# Swan flags
default swan_asked_who = False
default swan_asked_bloodmage = False
default swan_asked_bloodlearn = False
default swan_asked_falcon = False
default swan_asked_location = False
default swan_asked_mind = False
default swan_killed = False
default pigeon_told_human = False

# Falcon flags
default fal_first_time = True
default fal_420_success = False
default fal_asked_who = False
default fal_asked_what = False
default fal_asked_why = False
default fal_asked_cleric = False
default fal_asked_blight = False
default fal_asked_killed = False
default fal_asked_living = False
default fal_asked_before = False
default fal_asked_worm = False
default fal_asked_gov = False
default fal_angy = False

# Shrike flags
default shrike_asked_who = False
default shrike_asked_creation = False
default shrike_asked_bad = False
default shrike_asked_disco = False
default shrike_asked_blight = False
default shrike_asked_die = False
default shrike_asked_ghost = False
default shrike_asked_off = False
default shrike_asked_gov = False

# --- D O V E ---

label talk_dove_blushwood:
    $ quick_menu = False
    $ can_travel = False

    d "Good evening, sister. Tread carefully, there is a terrible curse beyond these gates."
    $ dove_starlight = True

    label .dove_menu:
    menu:
        "Who are you?" if not dove_asked_who:
            d "I am a ☀︎Life Cleric☀︎"
            d "Rejoice, nocturnal sister, for the Moon's light is the Sun’s love, finding you in the dark."
            $ dove_asked_who = True
            jump .dove_menu

        "What are you doing?" if not dove_asked_doing:
            d "Casting a protection spell. I’m keeping the Blight from spreading to the rest of the forest."
            d "Blushwood Court is already lost, I think. I grieve that. But I can at least try to keep it contained."
            d "I don’t love quarantine work... it feels wrong in all sorts of ways."
            d "But sometimes a boundary is an act of love."
            d "..."
            d "The sun is setting for today. I will be resting soon... then back to casting after the Dawn Chorus."
            $ dove_asked_doing = True
            jump .dove_menu

        "What is the Dawn Chorus?" if dove_asked_doing and not dove_asked_chorus:
            d "You're unfamiliar with the Dawn Chorus? It’s an old Helionic tradition, and one of my favorites."
            d "I start every day by singing to the sun."
            d "It isn’t really my song, though. I just… lend it my voice."
            d "It’s the sound the air makes when the light comes back. When God returns, and the world remembers She exists."
            d "We sing the shape of the world back into form before the first light spills over the edge of everything."
            d "It’s how we say that we are still here. We still see you. ☀︎"
            d "..."
            d "Between the two of us… I wonder if the Chorus is why the Blight hasn’t found its way to me yet."
            d "When you name the morning out loud, the Void has less room to argue."
            $ dove_asked_chorus = True
            jump .dove_menu

        "Did you know there’s a ghost next to the gate?" if dove_talked_scarlet and not dove_asked_scarlet:

            d "Ah, so you’ve met Scarlet Tananger. It breaks my heart, what happened to her…"
            d "I’ve spoken with her. She’s still here, still herself, still bright."
            d "She doesn’t know much more about the Blight than I do, I’m afraid. But her perspective may be worth seeking out."
            d "As a Death Cleric… you’ll be able to hear her in ways that I simply cannot."
            $ dove_asked_scarlet = True
            jump .dove_menu

        "What is a Death Cleric?" if dove_asked_kingsnake and not dove_asked_death:
            d "A rare and beautiful thing to be. Many people think Death is scary, but it’s a necessary transformation."
            d "You’re more attuned to it than most. That space between the end and the beginning."
            $ dove_asked_death = True
            jump .dove_menu

        "I'm here to investigate the Blight" if not dove_asked_kingsnake:
            d "Oh, yes, you must be the Cleric they sent for. Yes, Kingsnake mentioned you would be coming."
            d "Death always follows closely behind Life. That’s not a sad thing, it’s just the shape of it (^_^)☀︎"
            d "Here. A key to the Gate. Please be careful in there."
            $ inventory.add_item(item_db["GATE_KEY"])
            $ sector_gate.locked = False
            $ dove_asked_kingsnake = True
            jump .dove_menu

        "Ask about Blight" if not dove_asked_blight:
            d "From what I've seen… it feels like Void magic, and more of it than I've ever encountered in one place."
            d "I’ve been out here casting for 11 days now, and I still don’t fully understand what I’m pushing back against."
            d "Darkness itself isn’t something to fear. Everything living casts a shadow, that’s just the shape of being real."
            d "Usually, all darkness needs is to be loved. Met with light, gently, and it softens."
            d "But this... there's nothing but emptiness here."
            $ dove_asked_blight = True
            jump .dove_menu

        "You've been casting a spell for 11 days?" if dove_asked_blight and not dove_asked_11:
            d "Yes, and I've never felt better ☀︎"
            $ dove_asked_11 = True
            jump .dove_menu
 

        "Who do you mean, 'Her'?" if dove_starlight:
            d "Oh! Forgive me, nearly two weeks alone out here and I forgot not everyone lives in my head."
            d "Though you're a Cleric, too, so perhaps you'll understand."
            d "Most of the Church speaks of the Sun as He. And yes, scripture says the same."
            d "But in my own faith, in the private, quiet part of it that belongs only to me…"
            d "The Sun is a woman. She has always been a woman."
            d "It just feels true. The way some things feel true before you have the words for them."
            jump .dove_menu

            
        "(exit conversation)":
            if dove_moved_to_sanctum:
                d "I'll be heading to my Inner Sanctum at the Church in Sundapple Square. I hope to see you there, sister."
            else:
                d "Take care, sister of the Moon."
            $ can_travel = True
            jump overworld_loop

            

# --- THE CIDER MILL INTERIOR ---

label talk_seagull:
    seagull "You here to put me down? Go ahead. The gun's empty."
    label .seagull_menu:
    menu:
        "What happened here?" if not seagull_asked_here:
            seagull "I did the job. I killed an innocent dame for no good reason."
            seagull "And then, society collapsed. We live in a new world now, one where money, time, and God all mean nothing."
            seagull "Nothing. I killed her for absolutely nothing."
            $ seagull_asked_here = True
            jump .seagull_menu

        "Do you know anything about the Blight?" if not seagull_asked_blight:
            seagull "The trees? It turns people into trees. At least... I think they're trees."
            seagull "There's some around here. Dark, twisting branches with no leaves, and strange flickering colors. Reminds me of TV static."
            seagull "You might find pieces of viscera on and around them. It's the only thing left of the person that they used to be. As far as I can tell."
            seagull "..."
            seagull "I guess it doesn't kill you. It convinces you to stay until you're a place no one visits anymore."
            seagull "Came up here to try to get infected on purpose. I think it's working."
            $ seagull_asked_blight = True
            jump .seagull_menu

        "Are you infected with the Blight?" if seagull_asked_blight and not seagull_asked_infected:
            seagull "Yeah. I deserve whatever's coming to me."
            seagull "So I'm just sitting here, waiting to die."
            seagull "Toucan might still be alive. Might even still have some booze. I left a key out by the Hedge Maze. Take it... I don't need it anymore."
            $ seagull_asked_infected = True
            jump .seagull_menu

        "Who is Toucan?" if seagull_asked_infected and not seagull_asked_toucan:
            seagull "An old associate. He runs the bar downstairs. Might ask you to play cards with him."
            seagull "I think he likes to pretend that money still means something in this world."
            $ seagull_asked_toucan = True
            jump .seagull_menu

        "You look like you're close to dying..." if not seagull_asked_dying:
            seagull "Good. I owe the world at least that much."
            $ seagull_asked_dying = True
            jump .seagull_menu

        "Why do you think I'm here to kill you?" if seagull_asked_dying and not seagull_asked_dead:
            seagull "That's usually how this goes..."
            $ seagull_asked_dead = True
            jump .seagull_menu

        "Who did you kill?" if seagull_asked_here and not seagull_asked_her:
            seagull "Scarlet Tanager. Her bodyguard and I used to be besties, before I started killing for money."
            seagull "I killed some people here, too... if they could still be called 'people'. They're trees."
            $ scarlet_still_alive = True
            $ seagull_asked_her = True
            jump .seagull_menu

        "(exit conversation)":
            $ can_travel = True
            jump overworld_loop

label heal_seagull:
    seagull "..."
    seagull "You shouldn't have wasted that on me."
    menu:
        "You'll just have to find a way to live with it.":
            seagull "..."
            seagull "..."
            seagull "Yeah."
            jump overworld_loop
        "Scarlet's ghost is nearby..." if scarlet_still_alive:
            seagull "..."
            seagull "I know."
            jump overworld_loop
    $ can_travel = True
    jump overworld_loop

# Vending machine
label vending_machine_mill:
    "RECREATIONAL CONSUMABLES UNIT SYS:FILTER"
    menu:
        "Insert 2 units: CIGARETTE":
            if inventory.has_money(2):
                $ inventory.money -= 2
                $ inventory.add_item(item_db["cigarette"])
                "A single cigarette dispenses from the tray."
            else:
                "INSUFFICIENT FUNDS."
        "Insert 5 units: CATNIP":
            if inventory.has_money(5):
                $ inventory.money -= 5
                $ inventory.add_item(item_db["catnip"])
                "A pre-rolled catnip joint dispenses from the tray."
            else:
                "INSUFFICIENT FUNDS."
        "LEAVE":
            jump overworld_loop
    jump overworld_loop

# --- OTHER BLUSHWOOD LABELS ---

label scarlet_gate:
    sca "Well, well. Another Cleric. It is nice being able to talk to the living."
    $ dove_talked_scarlet = True
    label .scarlet_menu:
    menu:
        "I'm a Cleric?" if not scarlet_asked_cleric:
            sca "You carry the death mark. I can see it."
            sca "There aren't many of you left."
            $ scarlet_asked_cleric = True
            jump .scarlet_menu

        "What do you know about the Blight?" if not scarlet_asked_blight:
            sca "The world grew sick of maintaining the illusion. Everything's breaking."
            sca "I watched it happen from here. The trees first, then the people."
            sca "It is a kind of grief, I think. The world grieving itself."
            $ scarlet_asked_blight = True
            jump .scarlet_menu

        "Are you aware that you're dead?" if not scarlet_asked_aware:
            sca "Probably. If that's what you need to call it."
            sca "The brand outlives the girl."
            sca "There is no more Hollywood, no more record labels, no more media industry. No television, no phones, no print."
            sca "..."
            sca "I've never felt more free in my life."
            $ scarlet_asked_aware = True
            jump .scarlet_menu

        "Why is your ghost here?" if scarlet_asked_aware and not scarlet_asked_dead:
            sca "Where else would I go?"
            sca "This is the last place I was alive. The last place anyone knew the name Scarlet Tanagner."
            sca "Fame is a strange haunting. It keeps you tethered."
            $ scarlet_asked_dead = True
            jump .scarlet_menu

        "Did you know the man who killed you is still alive?" if scarlet_still_alive:
            sca "Of course he is. For men like him and women like me, survival is all we know how to do."
            sca "The Harbor Mafia doesn't waste assets. Even old ones."
            jump .scarlet_menu

        "I read that you died in the newspaper. Look, it says right here":
            sca "..."
            sca "They'll print anything that people want to hear."
            sca "Same as it's always been."
            jump .scarlet_menu

        "(exit conversation)":
            jump overworld_loop

label talk_turkey:
    $ quick_menu = False
    $ can_travel = False
    
    turk "Attention all guests"
    turk "In observance of THE END TIMES, all facilities are currently closed."
    turk "We hope you have enjoyed your visit to the Blushwood Court :^)"
    
    $ quick_menu = True
    $ can_travel = True
    jump overworld_loop

label surge_turkey:
    turk "..."
    turk "HELLO OPERATOR, how may I be of service?"
    turk "..."
    $ can_travel = True
    jump overworld_loop

label enter_mill:
    $ current_room = "cider_mill_interior"
    $ current_target = None
    "The heavy oak door groans. You enter the dark interior of the Cider Mill."
    jump overworld_loop

label talk_cat:
    if not can_speak_with_animals:
        "The black cat sits perched on a candy pumpkin, watching you curiously."
        jump overworld_loop

    cat "Good evening, Cleric."
    cat "I see you've been making good use of your spellbook. Keep it up :3"
    label .cat_menu:
        menu:
            "Who are you?":
                cat "I'm a Familiar, here to guide you in magic :3"
                cat "I can teach you a spell, if you'd like! :3"
                jump .cat_menu

            "What do you know about the Blight?":
                cat "Oh, I cannot tell you that. I can only guide you in magic :3"
                jump .cat_menu

            "I'd like to learn a new spell":
                cat "What spell would you like to learn? :3"
                menu:
                    "Power Surge":
                        # TODO: teaching logic will go here
                        jump .cat_menu
                    "Death Sight":
                        # TODO: teaching logic will go here
                        jump .cat_menu

            "(pet the cat)":
                cat "purrr, purrrrr..."
                jump .cat_menu

            "(exit conversation)":
                cat "Don't forget that I love you forever, Human :3"
                jump overworld_loop

label talk_dog:
    if not can_speak_with_animals:
        "The dog barks playfully, wagging its tail."
        jump overworld_loop

    dog "Death Cleric have dead things? Cleric give dead things to me? :3"
    # TODO: if give bone
    dog "DEAD THINGS!!! YAYAYAYAYAYYY I LOVE YOU, CLERIC :3"

    label .dog_menu:
        dog "Arf arf! :3"
        menu:
            "Who are you?":
                dog "I'm doggy. And doggy tummy full of dead things :3"
                jump .dog_menu

            "Where's your owner?":
                dog "Owner?"
                dog "There is no more 'owner'. No more hierarchy. No more law. No more safe place."
                dog "We are all wild beasts :3"
                jump .dog_menu

            "What do you know about the Blight?":
                dog "Bad sound waves everywhere. Sound waves inside human minds."
                dog "Many sad humans. Many dead humans."
                dog "But we don't have to be sad! Doggy know secret :3"
                dog "Was never really humans to begin with :3"
                jump .dog_menu

            "(pet the dog)":
                # TODO: optional pet feedback
                jump .dog_menu

            "(exit conversation)":
                "I love you always, Human!! ^w^"
                jump overworld_loop

label talk_crow:
    if not can_speak_with_animals:
        "The crow perches on a lamp post, eyeing you curiously."
        jump overworld_loop

    crow "What's on your mind, Cleric?"
    label .crow_menu:
        menu:
            "Who are you?" if not crow_asked_who:
                crow "I'm a crow."
                $ crow_asked_who = True
                jump .crow_menu

            "So... you're a bird, and I'm also a bird...thing? How does that work?" if not crow_asked_bird:
                crow "Haa haa haa... the world is an impossible thing, Cleric."
                crow "You may find some interesting documents scattered around. Whether or not they have any connection to eachother or to the grand scheme of things..."
                crow "Well. It's a Human's role to decide what has meaning."
                crow "Being something that exists is weird, isn't it?"
                $ crow_asked_bird = True
                jump .crow_menu

            "What do you know about the Blight?" if not crow_asked_blight:
                crow "I know that it is too late to save anyone."
                $ crow_asked_blight = True
                jump .crow_menu

            "What do you know about Blushwood Court?" if not crow_asked_blushwood:
                crow "Blushwood Court is not a real place. Everything here was constructed on the Glamour Lattice."
                crow "It turns out, playing God over a tightly bound tapestry of emotions and beliefs doesn't turn out very well for anyone."
                $ crow_asked_blushwood = True
                jump .crow_menu

            "What is a Glamour Lattice?" if crow_asked_blushwood and not crow_asked_glamor:
                crow "A structure built from Fae Magic. Illusions mapping themselves to whatever is percieving them. It's a network, a grid, a map, a mental link shared with anyone who steps through the gates."
                crow "Through the Glamour Lattice, the architect can fine tune every detail of the world within it. It is a contained, shared, curated illusion."
                crow "Your brain and body can believe that you've stepped into an enchanting, saccharine vacation resort."
                crow "Have you noticed that there is no rotten food here, despite it all sitting out in the open for several days? No flies or ants swarming the sugar frosted rooftops?"
                crow "That only me and two other animals here are real?"
                crow "Experiential life inside the Glamor Lattice can be curated and shaped into any desired form."
                crow "And just as easily, it can all unravel into chaos."
                $ crow_asked_glamor = True
                jump .crow_menu

            "Do you know where Kingsnake is?" if not crow_asked_kingsnakes:
                crow "Far away from here. Off the map entirely. Waiting for this mess to be cleaned up by someone else... he could be waiting a very long time. Haa haa haa"
                $ crow_asked_kingsnakes = True
                jump .crow_menu

            "(pet the crow)":
                crow "..."
                crow "I find this acceptable."
                jump .crow_menu

            "(exit conversation)":
                jump overworld_loop

label enter_hidden_bar:
    $ current_room = "hidden_bar"
    $ current_target = None
    "You descend into the neon lit basement, the air thick with the scent of alcohol and cigarettes."
    jump overworld_loop

label talk_toucan:
    if not toucan_first:
        tou "HEY! Goddamn, girl, you walked down here so quietly. Nearly gave me a heart attack."
        tou "You lost, or brave? Either way, you found my floor."
        $ toucan_first = True
    else:
        tou "Pull up a chair, doc."
        $ toucan_first = True

    tou "Can I get you a drink, or you here to play a round of cards?"
    label .toucan_menu:
        menu:
            "Who are you?" if not toucan_asked_who:
                tou "Name's Toucan, and this here's my hidden bar, away from the eye of the law."
                tou "Under normal circumstances, you would've been met with a lot more suspicion and pointed firearms when you walked through that door."
                tou "But, as I'm sure you noticed from outside, these are not normal circumstances."
                tou "So, welcome!"
                $ toucan_asked_who = True
                jump .toucan_menu

            "There's a man dying upstairs..." if not toucan_asked_dying:
                tou "He's still alive, then?"
                tou "That's Seagull. He's an old friend... got himself mixed up in a lot of bad business with a lot of bad people."
                tou "Wish there was something I could do to help him. He's so haunted by the past, I don't think he sees any possibility of a future."
                tou "Got the kinds of demons in his head that can't be drowned out with booze."
                tou "I keep hoping I'll hear him coming down those stairs one of these days, coming to say he's changed his mind and decided to give life another chance."
                tou "..."
                tou "But I've seen this enough times to know how it ends."
                $ toucan_asked_dying = True
                jump .toucan_menu

            "Did you know he murdered Scarlet Tanager?" if seagull_asked_her and toucan_asked_dying and not toucan_asked_scarlet:
                tou "Did he tell you?"
                tou "Not much point in hiding anything anymore..."
                tou "That's just the kind of mess that tends to happen in the underbelly of Blushwood. And I'm no saint, either."
                tou "Can't run an illegal gambling den without getting your hands dirty every now and then."
                tou "But I gotta say... I'm still surprised he actually did it. Killing an innocent woman like that."
                tou "Maybe it really is the end of the world."
                $ toucan_asked_scarlet = True
                jump .toucan_menu

            "Is Hummingbird... alright?" if not toucan_asked_hummingbird:
                tou "Hahahaha, are any of us alright??"
                tou "But, no, I feel you. I'm worried about her too. Wish I could get that Airspace Invaders machine up and running again."
                tou "She's been playing that thing non-stop. Part of me was kind of concerned with how much it consumed her attention."
                tou "Given the circumstances of the world right now though... I think she can play all the damn videogames she wants."
                $ toucan_asked_hummingbird = True
                jump .toucan_menu

            "Do you know Kingsnake?" if not toucan_asked_kingsnake:
                tou "Know him? He's basically my landlord!"
                tou "That's right, the big man who runs this whole resort knows all about this little den of sin."
                tou "Wonder if the Blight got to him. Can't say I'd have much sympathy if it did."
                tou "This whole resort is nothing but an act. Something that looks eco-friendly, a way to distract the public from where the Kingsnake fortune really comes from."
                tou "Kingsnake is an oil tycoon, through and through."
                $ toucan_asked_kingsnake = True
                jump .toucan_menu

            "What do you know about the Blight?" if not toucan_asked_blight:
                tou "Is that what they're calling it?"
                tou "Haven't heard anything from the outside world- TV lost signal on the first day."
                tou "Honestly? This might sound weird, but I'm just thankful it's not a zombie apocalypse scenario."
                tou "Now, I haven't ruled zombies out as a possibility. But, I feel like I would've had to fight off at least one person trying to eat my brains by now."
                tou "From what I've seen, it does look like some type of infection that makes people sad and lethargic until they turn into a tree."
                tou "But not like a real tree. Real trees in nature are beautiful."
                tou "These... well, it's more like, some type of negative malevolent energy compressed into the shape of a tree."
                tou "Which sounds dumb as hell. But I don't know any other way to describe it."
                $ toucan_asked_blight = True
                jump .toucan_menu

            "I'd like to buy a drink":
                # TODO: hook up a drinks submenu when ready
                jump .toucan_menu

            "Let's play some cards":
                jump minigame_toucan

            "(exit conversation)":
                tou "Careful out there, kid."
                tou "And don't be a stranger!"
                $ can_travel = True
                jump overworld_loop

label heal_toucan:
    tou "..."
    tou "Oh my god. How long have I been down here?!"
    tou "I need to get out of here, I need to go home..."
    tou "..."
    tou "Thanks for opening my eyes, doc. You're a good person."
    $ can_travel = True
    jump overworld_loop

label talk_hummingbird:
    hum "..."
    label .hummingbird_menu:
    menu:
        "Are you okay?" if not hum_asked_arcade:
            hum "..."
            hum "I'm waiting for the machine to come back on."
            $ hum_asked_arcade = True
            jump .hummingbird_menu

        "What game is this?" if hum_asked_arcade and not hum_asked_aerospace:
            hum "Aerospace Invaders."
            hum "It's the only thing keeping me sane right now."
            $ hum_asked_aerospace = True
            jump .hummingbird_menu

        "Do you know anything about the Blight?" if not hum_asked_blight:
            hum "..."
            hum "It's not a disease. It's a feeling."
            hum "And some people can't stop feeling it."
            $ hum_asked_blight = True
            jump .hummingbird_menu

        "What do you know about Blushwood Court?" if not hum_asked_blushwood:
            hum "It's not real."
            hum "None of it was ever real."
            $ hum_asked_blushwood = True
            jump .hummingbird_menu

        "What do you know about Fae magic?" if not hum_asked_fae:
            hum "..."
            hum "I know that once it's in you, you can't get it out."
            $ hum_asked_fae = True
            jump .hummingbird_menu

        "(exit conversation)":
            $ can_travel = True
            jump overworld_loop

label talk_arcade_machine:
    $ quick_menu = False
    $ can_travel = False

    if not arcade_machine_fixed:
        sys "ERROR: SYSTEM_CORRUPTED. UNABLE_TO_BOOT."
        $ quick_menu = True
        $ can_travel = True
        jump overworld_loop

    # After it's fixed:
    sys "ARCADE_MACHINE.EXE online."
    sys "AEROSPACE_INVADERS version 2.1 loaded."
    


    $ can_travel = True
    jump overworld_loop

label talk_ptarmigan:
    pta "..."
    pta "is someone there?"
    pta "[PROCESSING]"
    pta "..."
    pta "It's like I'm falling apart."
    label .ptarmigan_menu:
    menu:
        "Who are you?" if not pta_asked_who:
            pta "[ALWAYS KNOWN THAT]"
            pta "..."
            pta "I think my name is... I think..."
            pta "..."
            $ pta_asked_who = True
            jump .ptarmigan_menu

        "What is the Blight?" if not pta_asked_blight:
            pta "[THE EMPTY DEATH]"
            pta "..."
            $ pta_asked_blight = True
            jump .ptarmigan_menu

        "Do you know where we are?" if not pta_asked_cabin:
            pta "..."
            pta "The river. I came to the river."
            pta "I was looking for something."
            $ pta_asked_cabin = True
            jump .ptarmigan_menu

        "What were you looking for?" if pta_asked_cabin and not pta_asked_what:
            pta "..."
            $ pta_asked_what = True
            jump .ptarmigan_menu

        "Can I help you?" if not pta_asked_help:
            pta "..."
            pta "..."
            pta "I don't know."
            $ pta_asked_help = True
            jump .ptarmigan_menu

        "(exit conversation)":
            $ can_travel = True
            jump overworld_loop

label heal_ptarmigan:
    "Your power washes over Ptarmigan, banishing the Blight from her eyes."
    pta "I feel... lighter."
    pta "..."
    pta "Thank you, Cleric."
    $ can_travel = True
    jump overworld_loop

label cabin_blocked:
    if getattr(store, "cabin_roots_deleted", False):
        "The remains of enormous, withered roots litter the path. The cabin door stands open."
        jump after_prune_roots
    else:
        "The roots hum with a deadly magical frequency. Access Denied."
        jump overworld_loop

label after_prune_roots:
    $ cabin_roots_deleted = True
    # Unlock the cabin door once roots are pruned
    $ cabin_unlocked = True
    $ cabin_door.locked = False
    "As you cast PRUNE.EXE, the MAGICAL_ROOTS wither and crumble away, leaving the path to the cabin unblocked."
    "A presence waits by the threshold - an elegant, spectral figure of a SWAN. (Placeholder: Swan introductory event goes here.)"
    jump overworld_loop


# --- S E C R E T A R Y ---

label talk_secretary:
    $ quick_menu = False
    $ can_travel = False
    sec "█████ ████ ███"
    sec "Have you seen him? My enemy?"
    label .secretary_menu:
    menu:
        "Who is your enemy?" if not sec_asked_enemy:
            sec "█████"
            sec "He's here. He's always here."
            sec "He took my evidence. He took my case. He took everything."
            $ sec_asked_enemy = True
            jump .secretary_menu

        "What is your enemy's name?" if sec_asked_enemy and not sec_asked_name:
            sec "████████"
            sec "I know his face. I know his voice."
            sec "I just can't... I can't say it."
            $ sec_asked_name = True
            jump .secretary_menu

        "Who are you?" if not sec_asked_who:
            sec "I'm a federal investigator."
            sec "Or I was."
            sec "█████ ████"
            $ sec_asked_who = True
            jump .secretary_menu

        "Do you know anything about the Blight?" if not sec_asked_blight:
            sec "The Blight is him."
            sec "He made it. He manufactured it. I have the documents."
            sec "I have the documents, I have the documents, I have the—"
            sec "..."
            $ sec_asked_blight = True
            jump .secretary_menu

        "Are you a federal investigator?" if sec_asked_who and not sec_asked_federal:
            sec "I was assigned to Blushwood Court by Kingsnake himself."
            sec "I found something I wasn't supposed to find."
            sec "And then I found myself here."
            $ sec_asked_federal = True
            jump .secretary_menu

        "(exit conversation)":
            $ can_travel = True
            jump overworld_loop

label heal_secretary:
    "The Blight lifts from the Secretary's eyes. For a moment, she is completely still."
    sec "..."
    sec "Oh."
    sec "Oh, I remember now."
    sec "My name is... my name is Secretary."
    sec "I was investigating a facility. The AVM facility. Kingsnake's project."
    sec "There's a diner in Sundapple Square. Meet me there when you're ready."
    sec "I have a lot to tell you."
    $ secretary_healed = True
    $ can_travel = True
    jump overworld_loop


# --- F A L C O N ---

label talk_falcon:
    $ quick_menu = False
    $ can_travel = False
    if fal_first_time:
        fal "Identify yourself. Agent ID number."
        $ fal_first_time = False
        menu:
            "420":
                $ fal_420_success = True
                fal "..."
                fal "Clearance confirmed."
                fal "I'm ready to give my post-mortem report."
                jump .falcon_report_menu
            "I don't have an ID number.":
                $ fal_angy = True
                fal "Then I can't speak with you."
                fal "This is a classified operation."
                jump .falcon_civilian_menu
            "1776":
                $ fal_angy = True
                fal "Wrong."
                jump .falcon_civilian_menu
            "0000":
                $ fal_angy = True
                fal "Wrong."
                jump .falcon_civilian_menu
    else:
        if fal_420_success:
            jump .falcon_report_menu
        else:
            jump .falcon_civilian_menu

    label .falcon_report_menu:
    menu:
        "Who are you?" if not fal_asked_who:
            fal "Special Agent Falcon. Government field division."
            fal "I was assigned to the Blushwood Court investigation."
            $ fal_asked_who = True
            jump .falcon_report_menu

        "What was your assignment?" if not fal_asked_what:
            fal "Third iteraction of the Grief Seed experiment."
            fal "Observe. Document. Report."
            fal "I did not complete my report."
            $ fal_asked_what = True
            jump .falcon_report_menu

        "What is the Grief Seed experiment?" if fal_asked_what and not fal_asked_why:
            fal "A controlled study in manufactured emotional collapse."
            fal "The Blight is not a disease. It is a program."
            fal "Someone wrote it. Someone deployed it."
            $ fal_asked_why = True
            jump .falcon_report_menu

        "Are you infected with the Blight?" if not fal_asked_blight:
            fal "Negative. I'm dead."
            fal "The Blight doesn't affect the dead."
            fal "That's the only advantage."
            $ fal_asked_blight = True
            jump .falcon_report_menu

        "What killed you?" if not fal_asked_killed:
            fal "..."
            fal "The person I was protecting."
            $ fal_asked_killed = True
            jump .falcon_report_menu

        "Who wrote the Blight program?" if fal_asked_why and not fal_asked_gov:
            fal "That is classified."
            fal "..."
            fal "But you're a Cleric, and Clerics outrank my clearance level."
            fal "Look for the worm."
            $ fal_asked_gov = True
            jump .falcon_report_menu

        "What is the worm?" if fal_asked_gov and not fal_asked_worm:
            fal "The core of the program. The self-replicating emotional vector."
            fal "If you can find the worm, you can find the source."
            $ fal_asked_worm = True
            jump .falcon_report_menu

        "(exit conversation)":
            $ can_travel = True
            jump overworld_loop

    label .falcon_civilian_menu:
    menu:
        "I'm a Cleric, investigating the Blight." if not fal_asked_cleric:
            fal "..."
            fal "A Cleric."
            fal "Then you already know more than I do."
            $ fal_asked_cleric = True
            jump .falcon_civilian_menu

        "What do you know about this place?" if not fal_asked_before:
            fal "I was stationed here."
            fal "Before."
            $ fal_asked_before = True
            jump .falcon_civilian_menu

        "Are you still alive?" if not fal_asked_living:
            fal "No."
            $ fal_asked_living = True
            jump .falcon_civilian_menu

        "(exit conversation)":
            $ can_travel = True
            jump overworld_loop


# --- S H R I K E ---

label talk_shrike:
    $ quick_menu = False
    $ can_travel = False
    shrike "..."
    shrike "So. You found the Core."
    label .shrike_menu:
    menu:
        "Who are you?" if not shrike_asked_who:
            shrike "I built this place."
            shrike "Every inch of it. Every tree, every cobblestone, every face."
            shrike "My name is Shrike."
            $ shrike_asked_who = True
            jump .shrike_menu

        "What is the Glamour Lattice?" if shrike_asked_who and not shrike_asked_creation:
            shrike "A structure of living memory."
            shrike "I designed it to hold the shape of a world that people actually wanted to live in."
            shrike "It worked, for a while."
            $ shrike_asked_creation = True
            jump .shrike_menu

        "What went wrong?" if shrike_asked_creation and not shrike_asked_bad:
            shrike "Nothing went wrong."
            shrike "Everything went exactly as it was designed to."
            shrike "That was the problem."
            $ shrike_asked_bad = True
            jump .shrike_menu

        "What do you know about the Blight?" if not shrike_asked_blight:
            shrike "The Blight is the Lattice turning inward."
            shrike "When the illusion can no longer sustain itself, it starts consuming the things inside it."
            shrike "The people first. Then the architecture."
            shrike "Then the Core."
            $ shrike_asked_blight = True
            jump .shrike_menu

        "Are you dead?" if not shrike_asked_die:
            shrike "Yes."
            shrike "I chose it."
            shrike "Someone had to stay in the Core and keep it stable. And I couldn't ask anyone else to do that."
            $ shrike_asked_die = True
            jump .shrike_menu

        "Why are you still here?" if shrike_asked_die and not shrike_asked_ghost:
            shrike "The Core is the anchor point of the Lattice."
            shrike "As long as the Lattice exists, so do I."
            $ shrike_asked_ghost = True
            jump .shrike_menu

        "Can I turn the Glamour Lattice off?" if shrike_asked_ghost and not shrike_asked_off:
            shrike "You could."
            shrike "But everything inside it would dissolve."
            shrike "Everyone in Blushwood Court would..."
            shrike "..."
            shrike "There might be another way. But I don't know it yet."
            $ shrike_asked_off = True
            jump .shrike_menu

        "Who built this place originally?" if shrike_asked_creation and not shrike_asked_disco:
            shrike "The government commissioned it."
            shrike "A controlled environment for social research."
            shrike "They wanted to see what people do when everything is provided for them."
            $ shrike_asked_disco = True
            jump .shrike_menu

        "Who authorized the Grief Seed experiment?" if shrike_asked_disco and not shrike_asked_gov:
            shrike "..."
            shrike "I don't know that name."
            shrike "But someone with very high clearance modified the Lattice parameters after I died."
            shrike "I couldn't stop it."
            $ shrike_asked_gov = True
            jump .shrike_menu

        "(exit conversation)":
            $ can_travel = True
            jump overworld_loop


# --- S W A N  M A N O R ---

label talk_swan_manor:
    $ quick_menu = False
    $ can_travel = False
    s "You made it."
    label .swan_manor_menu:
    menu:
        "Who are you?" if not swan_asked_who:
            s "Swan."
            s "I'm a Blood Mage. Among other things."
            $ swan_asked_who = True
            jump .swan_manor_menu

        "What is a Blood Mage?" if swan_asked_who and not swan_asked_bloodmage:
            s "Someone who uses their own life force as a power source."
            s "It's not a career path I'd recommend."
            $ swan_asked_bloodmage = True
            jump .swan_manor_menu

        "How are you not infected?" if not swan_asked_location:
            menu:
                "You seem immune to the Blight.":
                    s "Blood Magic is a complete internal system. The Blight has nothing to interface with."
                    jump .swan_manor_menu
                "Is it because you're a Blood Mage?":
                    s "That's part of it."
                    s "The rest is... complicated."
                    jump .swan_manor_menu
                "Did Pigeon tell you about me?" if pigeon_told_human:
                    s "..."
                    s "Yes."
                    s "That's why I'm talking to you."
                    jump .swan_manor_menu
                "(say nothing)":
                    s "..."
                    jump .swan_manor_menu
            $ swan_asked_location = True

        "What happened at the Cabin?" if not swan_asked_falcon:
            s "..."
            s "That's a long conversation."
            s "The short version: I was protecting someone. Someone died protecting me instead."
            s "I've been dealing with the aftermath ever since."
            $ swan_asked_falcon = True
            jump .swan_manor_menu

        "What do you know about Kingsnake?" if not swan_asked_mind:
            s "He's my stepfather."
            s "..."
            s "Yes. I know."
            $ swan_asked_mind = True
            jump .swan_manor_menu

        "Can you teach me Blood Magic?" if swan_asked_bloodmage and not swan_asked_bloodlearn:
            s "No."
            s "Not because I don't want to. Because it would kill you."
            s "You'd need to be... differently constructed."
            $ swan_asked_bloodlearn = True
            jump .swan_manor_menu

        "(exit conversation)":
            $ can_travel = True
            jump overworld_loop

label swan_avm_confirm:
    s "The AVM facility is northeast of the map."
    s "You'll need clearance to get in."
    s "I can get you that clearance."
    s "But once you go in... things will change."
    menu:
        "I'm ready.":
            $ avm_facility_accessible = True
            s "Then go."
            jump overworld_loop
        "Not yet.":
            s "..."
            s "Come back when you are."
            jump overworld_loop



label hack_pc_terminal:
    sys "ACCESS_GRANTED. Scanning local index..."
    sys "// TODO: PC Terminal hack content goes here."
    $ can_travel = True
    jump overworld_loop

label hack_vending_machine:
    sys "HACK.EXE interfacing with [hack_target.name]..."
    sys "// TODO: Vending machine hack content goes here."
    $ can_travel = True
    jump overworld_loop

label hack_slot_machine:
    sys "HACK.EXE interfacing with SLOT_MACHINE..."
    sys "// TODO: Slot machine hack content goes here."
    $ can_travel = True
    jump overworld_loop

label hack_atm_machine:
    sys "HACK.EXE interfacing with ATM_MACHINE..."
    sys "// TODO: ATM hack content goes here."
    $ can_travel = True
    jump overworld_loop
