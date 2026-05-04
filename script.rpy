## script.rpy - THE SYSTEM BOOT SEQUENCE

# --- INITIAL STATE & VARIABLES ---
default inventory = Inventory(money=10)
default journal_entries = []
default game_start_time = ""

default death_count = 0
default last_room = None  # Used for resurrection

# ROUTE PROGRESS & FACILITY ACCESS FLAGS (for future expansion)
default route_dove_locked = False
default route_raven_locked = False
default route_swan_locked = False
default route_pigeon_locked = False
default current_route = None             # "dove", "raven", "swan", "pigeon"
default avm_facility_accessible = False  # Controls visibility/travel on map

# PIGEON Postgame Unlock Condition
default completion_dove = False
default completion_raven = False
default completion_swan = False
default pigeon_route_unlocked = False

# Centralize one-time spell/activation flags to avoid duplicate defaults
default seagull_healed = False
default secretary_healed = False
default ptarmigan_healed = False
default turkey_activated = False
default cabin_roots_deleted = False

# IMAGES
image bg = "images/ui/bg.png"
image player_menu_box = Frame("images/ui/text_player.png", 0, 0)
image aes_forest = "images/bgs/bg_forest.png"

# --- GAME START ---

label start:
    $ quick_menu = False

    python:
        import datetime
        game_start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        journal_entries = [JournalEntry("ROOT", "System Online", game_start_time, "OS stabilized. Cleric credentials verified. Blight investigation beginning in Sector 01.")]

    scene bg
    sys "AvisMortem OS 1.0 ... Initializing."

    menu:
        "How would you like to boot the system?"
        
        "[[ NORMAL MODE - Start Game ]]":
            jump opening_cutscene
        
        "[[ DEBUG MODE - All Unlocks Active ]]":
            jump start_debug

label start_normal:
    """Normal game start - all defaults as intended for release."""
    $ can_travel = True

    # Reset all flags to default/intended state


    
    # Route stages at 0

    d "Welcome, sister. The system is online."
    d "Your first assignment: investigate the Blight in Blushwood Court."
    
    $ current_room = "blushwood_1"
    jump overworld_loop

label start_debug:
    """Debug mode - all doors unlocked, all items/spells available."""
    $ can_travel = True

    # UNLOCK EVERYTHING
    $ dove_moved_to_sanctum = False  # Keep NPCs in starting positions for testing
    $ raven_moved_to_cafe = False
    $ ghost_cat_decrypted = True
    $ manor_unlocked = True
    $ cabin_unlocked = True
    $ arcade_machine_fixed = True
    
    # Unlock all doors
    $ sector_gate.locked = False
    $ mill_trap_door.locked = False
    $ restricted_magic.locked = False
    $ manor_door.locked = False
    $ cabin_door.locked = False
    
    # Route stages (optional - set to 1 or 2 to test mid-route content)
    $ dove_route_stage = 0
    $ raven_route_stage = 0
    $ swan_route_stage = 0
    
    # AVM Facility accessible for testing
    $ avm_facility_accessible = True
    
    # Give EVERYTHING
    python:
        inventory = Inventory(money=999)
        
        # Learn all spells
        inventory.learn_spell(ghost_speak_prog)
        inventory.learn_spell(animal_speak_prog)
        inventory.learn_spell(hack_prog)
        inventory.learn_spell(heal_blight_prog)
        
        # Add all items
        for item_key in item_db:
            inventory.add_item(item_db[item_key])
            inventory.add_item(item_db[item_key])  # Add twice for testing
    
    $ journal_entries = []
    $ journal_entries.append(JournalEntry("DEBUG", "Debug Mode Active", "2026-01-15", "All systems unlocked. Full access granted."))

    sys "DEBUG MODE ACTIVE"
    sys "All doors unlocked. All items granted. Fast travel enabled."
    sys "Where would you like to deploy?"
    
    menu:
        "Deploy to Blushwood (Gate)":
            $ current_room = "blushwood_1"
        "Deploy to Sundapple Square":
            $ current_room = "sundapple_1"
        "Deploy to Parlor District":
            $ current_room = "parlor_1"
        "Deploy to Hidden Bar":
            $ current_room = "hidden_bar"
        "Deploy to Cabin Exterior":
            $ current_room = "cabin_exterior"
        "Deploy to Manor Exterior":
            $ current_room = "manor_exterior"
        "Deploy to Manor Garden":
            $ current_room = "manor_garden"
        "Deploy to Underground":
            $ current_room = "manor_underground"
        "Deploy to Core":
            $ current_room = "manor_core"
    
    jump overworld_loop
label test_hub:
    menu:
        "Test inventory":
            jump inventory_test
        "Test spellcasting system":
            jump spell_test
        "Test inventory screen":
            jump inventorylist_test
        "Return to Start":
            jump start

label overworld_loop:
    # Run global triggers based on current room and flags.
    python:
        # Call the routing triggers function (defined in routing.rpy).
        if 'check_room_triggers' in globals():
            check_room_triggers()

    show screen game_tabs
    call screen world_interface
    jump overworld_loop

label death_sequence_poison:
    $ death_count += 1
    scene black
    "Your vision blurs as the data-corruption sweeps over your system..."
    "But the reset protocol triggers, rebooting your neural processes."
    jump post_death_generic

label post_death_generic:
    "You awaken where you left off. All systems operational."
    $ current_room = last_room if last_room is not None else "blushwood_1"
    jump overworld_loop