# --- PARLOR DISTRICT DIALOGUE & EVENTS ---

# --- CAVE ENTRANCE (Landing Zone) ---

label talk_spider:
    if not can_speak_with_animals:
        "The spider remains motionless, staring at you with all its eyes."
        jump overworld_loop

    "SPIDER" "Sector 03 is quiet today. Too quiet. Even the web-traffic is down to a crawl."
    "SPIDER" "Watch out for the Vampire Bat. He'll drink anyone's blood. I've seen it."
    jump overworld_loop

label talk_vampire_bat:
    "VAMPIRE_BAT" "Greetings, Cleric. Looking for someone? Or just lurking in the shadows like the rest of us?"
    "VAMPIRE_BAT" "Don't go North into the Depths. That area is under a permanent kernel lock."
    jump overworld_loop

label vending_machine_parlor:
    "SYSTEM: PARLOR_DISTRICT_HUB. Local currency recognized."
    menu:
        "INSERT 10 UNITS: ENCRYPTED_DATA_PACK":
            if inventory.has_money(10):
                $ inventory.money -= 10
                "Clunk. A glowing purple drive slides into the tray."
            else:
                "INSUFFICIENT FUNDS."
        "LEAVE":
            jump overworld_loop
    jump overworld_loop

# --- THE CAFE ---

label shop_vulture:
    "VULTURE" "Welcome to the Parlor Cafe. We serve the finest data-brews in the district."
    "VULTURE" "Looking to trade some units for hardware?"

    label .vulture_menu:
    menu:
        "BUY: Cassette (5 Units)":
            if inventory.buy(item_db["cassette"]):
                "VULTURE" "A classic choice. Very analog."
            else:
                "VULTURE" "You're short on units, friend."
            jump .vulture_menu

        "Talk to Vulture":
            "VULTURE" "The Parlor used to be full of life. Now, it's just a graveyard for wealthy algorithms."
            jump .vulture_menu

        "[[ X ]] EXIT":
            "VULTURE" "Fly safe."
            jump overworld_loop

# --- RAVEN'S SECOND LOCATION (CAFE) ---
label talk_raven_cafe:
    # This event can later set route flags / AVM access when ready.
    r "Hey! Thanks for meeting me here. Do you want anything to drink?"
    menu:
        "Sure":
            r "Cool! Just tell Vulture to put it on my tab."
        "No thanks":
            r "Sure. Yeah, I'm not a huge fan of alcohol either tbh."
        "Are you hitting on me?":
            r "Oh! Sorry, I didn't mean to give you that impression. I just.... uhhm..."

    r "Sorry if I seem a bit nervous, or if I say something stupid. I'm not very good at this social interaction thing."
    r "..."
    r "You're a Death Cleric. I saw it on your ID."
    menu:
        "Yeah... and?":
            pass
        "You seemed very calm about handing over a Destruction spell to me.":
            r "Is it that obvious, that I've stopped caring about everything?"

    r "From what I've read, Death Clerics don't really die all the way. You keep regenerating to the way you were before it happened."
    r "I was just curious to talk to you because... well, I don't entirely know what it is, but I might also have an allergic reaction to dying."
    r "Have you heard about the Plagues? Spontaneous Electrocution? I'm pretty sure it got me, and if it did..."
    r "... then as far as I know, I'm the only one who has survived it."
    jump overworld_loop

# --- THE RECORD STORE ---

label talk_flying_fox:
    "FLYING_FOX" "You look like you appreciate the old frequencies. We've got recordings here that date back to the first OS."
    jump overworld_loop

label talk_ghost_cat:
    if not can_speak_with_animals:
        "A translucent feline flickers in and out of existence among the vinyl racks."
        jump overworld_loop

    "SYSTEM: DUAL_ENCRYPTION_DETECTED. Target is both ANIMAL and SPECTRAL."
    "The cat's meows are distorted by a phantom echo. You need to decrypt its spectral frequency as well."

    if can_speak_with_animals and ghost_cat_decrypted:
        "GHOST_CAT" "The music here... it repeats forever. Do you like the loop, Cleric?"

    jump overworld_loop

# --- THE DEPTHS ---

label cave_depths_blocked:
    "The way is barred by a heavy iron gate with a digital keypad."
    "SYSTEM: FORBIDDEN_ZONE. Clearance level 'OBSIDIAN' required."
    jump overworld_loop