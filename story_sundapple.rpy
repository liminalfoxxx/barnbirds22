# --- SECTOR 02: SUNDAPPLE SQUARE DIALOGUE & EVENTS ---

# --- THE MALL (Center Hub) ---

label talk_magpie:
    mag "Oh! Hi, sorry, I thought you worked here for a second."
    mag "They keep changing the uniforms, don't they?"
    mag "I'm Magpie, it's nice to meet you~!"
    mag "You're back! That's good. I was starting to think they'd stopped letting people in."
    label .menu_magpie:
    menu:
        "What is this place?":
            mag "Sundapple Square~!"
            mag "It's a lot quieter lately, though. And some of the stores are temporarily closed."
            mag "I guess people just don't know where to go anymore."
            jump .menu_magpie
        "What do you know about the Plagues?":
            mag "All of my friends died from sponteneous electrocution."
            mag "..."
            mag "They would've loved the new trinket store that just opened up."
            jump .menu_magpie
        "What do you know about the Blight?":
            mag "The Blight? Oh, yeah, I heard that's why Blushwood Court is temporarily closed."
            mag "..."
            mag "I'm sure it's only temporary, though!"
            jump .menu_magpie
        "(exit conversation)":
            mag "I remember when you couldn't hear yourself think in here."
            jump overworld_loop

label shop_goose:
    "GOOSE" "HONK! Welcome to the Square Market. Looking to trade memory units for physical hardware?"
    label .goose_menu:
    menu:
        "BUY: Candle (2 Units)":
            if inventory.buy(item_db["candle"]):
                "GOOSE" "A wise investment. The shadows in the library can be... hungry."
            else:
                "GOOSE" "Insufficient units. Check the floor for spare change."
            jump .goose_menu
        "BUY: Soda (4 Units)":
            if inventory.buy(item_db["soda"]):
                "GOOSE" "Tastes like pure orange data. Enjoy the kick."
            else:
                "GOOSE" "You're short on funds, Cleric."
            jump .goose_menu
        "[[ X ]] EXIT":
            "GOOSE" "Honk! Fly safe."
            jump overworld_loop

label shop_ostrich:
    ost "Evening, ma'am."
    label .ostrich_menu:
    menu:
        "BUY: Cassette (5 Units)":
            if inventory.buy(item_db["cassette"]):
                ost "Rare analog storage. Don't let the tape tangle."
            else:
                ost "Memory error: Insufficient currency."
            jump .ostrich_menu
        "[[ X ]] EXIT":
            jump overworld_loop

label cornucopia_dogs:
    "Welcome to Cornucopia Dogs!"
    menu:
        "Ice Cream Sundae: (5) units":
            pass
        "Orange Soda: (3) units":
            pass
        "(leave)":
            jump overworld_loop
    jump overworld_loop

label vending_sundapple:
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

# --- THE LIBRARY ---

label talk_raven:
    r "Welcome to the Library. Let me know if you need help with anything."
    label .raven_library_menu:
    menu:
        "I'd like to check out a book.":
            r "We’re still digitizing the catalog, but feel free to browse the shelves."
            jump .raven_library_menu
        "I would like to request access to the Forbidden Magic.":
            r ".... sure, okay. Let me check."
            r "Hmm. Yeah, your Cleric ID checks out."
            r "You have access to one of the scrolls. Use it wisely."
            # TODO: grant restricted magic access key and/or Destruction Scroll
            jump .raven_library_menu
        "(exit conversation)":
            jump overworld_loop

label talk_library_pc:
    "SYSTEM: data_index_terminal"
    label .pc_menu:
    menu:
        "History":
            "Ancient Draconic Law"
            "Gryphons"
            "Industrial Revolution- Electricity"
            jump .pc_menu
        "RESTRICTED ACCESS: OS Specs":
            "AvisMortem OS 1.0. Priority 1: Prevent total data collapse."
            jump .pc_menu
        "[[ X ]] DISCONNECT":
            jump overworld_loop

label talk_library_bin:
    "A pile of pixelated newspapers. The ink is still wet with code."
    label .bin_menu:
    menu:
        "READ: 'Blushwood Court Grand Opening'":
            "The Kingsnakes open their private garden residence to the public- book now!"
            jump .bin_menu
        "READ: 'Cider Mill Shutdown'":
            "Penguin confirms machinery is no longer accepting organic fruit input."
            jump .bin_menu
        "[[ X ]] LEAVE":
            jump overworld_loop

label talk_pigeon:
    "PIGEON" "Sort, stack, shelf. Sort, stack, shelf. The cycle never terminates."
    jump overworld_loop

label talk_shelf_history:
    #add text here, we can format it later
    "Death Goddess Prayer Card"
    "To shadows that lurk between the trees, untouched by the sun, not disconnected."
    "She is everything, the roots, the leaves, the sky, the storm, the fire."
    "We are all dancing within her cycle just as she dances through ours."
    "She is life."
    "This strange miracle, this strange accident."
    "From her we are formed, a thousand miracles in motion, a million accidents woven together."
    "And to her, we return-"
    jump overworld_loop

label label_restricted_magic:
    if restricted_magic.locked:
        "A glowing locked chest. It requires a Library Access Key."
        jump overworld_loop
    
    "The chest opens with a chime. You feel a surge of magical potential."
    # TODO: Here you may want to give the Destruction_Scroll or "DELETE" spell to player, e.g.
    # $ inventory.add_item(item_db["Destruction_Scroll"])
    # $ inventory.learn_spell(delete_prog)
    jump overworld_loop

# --- THE DINER & CHURCH ---

label talk_pheasant:
    phe "Need something, sugar?"
    jump overworld_loop

label talk_heron:
    heron "Hmm? What is it?"
    jump overworld_loop

label talk_cassowary:
    cas "Aye. Don't start nothing. I'm watching you."
    jump overworld_loop

label talk_hen:
    hen "Praise the sun, sister."
    jump overworld_loop

label talk_rooster:
    # Requires Ghost Speak
    "ROOSTER" "Do you feel the solar winds, sister? The Suncatcher knows what time it is."
    jump overworld_loop

# DOVE'S SECOND LOCATION
label talk_dove_sanctum:
    if not dove_moved_to_sanctum:
        "The Inner Sanctum is silent. Solar data refracts through the suncatcher."
        jump overworld_loop
    
    d "The light is so much clearer here, sister. I can see the structure of the world from this height."
    d "The Blight isn't a disease. It's an uninstaller."
    jump overworld_loop