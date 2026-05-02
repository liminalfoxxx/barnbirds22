# --- STEP 1: Blueprints ---
init -10 python:
    class WorldObject:
        def __init__(self, name, description, img, sprite, x, y, can_talk=False, can_take=False, can_open=False, can_cast=False, locked=False, label=None):
            self.name = name
            self.description = description
            self.img = img
            self.sprite = sprite
            self.x = x
            self.y = y 
            self.can_talk = can_talk
            self.can_take = can_take
            self.can_open = can_open
            self.can_cast = can_cast
            self.locked = locked 
            self.label = label

    class Room:
        def __init__(self, name, art, north=None, south=None, east=None, west=None, contents=None):
            self.name = name
            self.art = art
            self.north = north
            self.south = south
            self.east = east
            self.west = west
            self._contents = contents or []

        @property
        def contents(self):
            """Dynamic content filtering for moving NPCs."""
            current_list = list(self._contents)
            
            # Dove Logic: Remove from Gate if moved to Sanctum
            if self.name == "GATE" and store.dove_moved_to_sanctum:
                current_list = [obj for obj in current_list if obj.name != "DOVE"]
            if self.name == "INNER_SANCTUM" and store.dove_moved_to_sanctum:
                current_list.append(store.forest_dove)

            # Raven Logic: Move from Library to Cafe
            if self.name == "LIBRARY_LOBBY" and store.raven_moved_to_cafe:
                current_list = [obj for obj in current_list if obj.name != "RAVEN"]
            if self.name == "CAFE" and store.raven_moved_to_cafe:
                current_list.append(store.npc_raven)

            # Optional: Swan presence in Manor Interior (stage-based)
            if self.name == "MANOR_INTERIOR" and getattr(store, "swan_route_stage", 0) >= 1:
                if store.npc_swan not in current_list:
                    current_list.append(store.npc_swan)

            # Seagull: Remove from Cider Mill Interior after healed
            if self.name == "CIDER_MILL_INTERIOR" and getattr(store, "seagull_healed", False):
                current_list = [obj for obj in current_list if obj.name != "SEAGULL"]

            # Secretary: Remove from Hedge Maze after healed
            if self.name == "HEDGE_MAZE" and getattr(store, "secretary_healed", False):
                current_list = [obj for obj in current_list if obj.name != "SECRETARY"]

            # Ptarmigan: Remove from current location after healed
            if getattr(store, "ptarmigan_healed", False):
                current_list = [obj for obj in current_list if obj.name != "PTARMIGAN"]

            return current_list

    def pick_up_item(target, inv, room_var_name):
        room_obj = getattr(store, room_var_name)
        item_key = target.name.lower().replace(" ", "_")

        if item_key == "money":
            inv.money += 5
            renpy.notify("RECEIVED: 5_UNITS")
        elif item_key in item_db:
            inv.add_item(item_db[item_key])
        else:
            inv.add_item(target)

        if target in room_obj._contents:
            room_obj._contents.remove(target)

        store.current_target = None
        renpy.notify("Item_Stored")

    def use_item_on_target(target, item):
        if target.name == "GATE" and item.name == "GATE_KEY":
            target.locked = False
            renpy.notify("SUCCESS: GATE_UNLOCKED")
            inventory.remove_by_name("GATE_KEY")
        elif target.name == "TRAP_DOOR":
            if item.name == "SILVER_KEY":
                target.locked = False
                renpy.notify("SUCCESS: DOOR_UNLOCKED")
                inventory.remove_by_name("SILVER_KEY")
        elif target.name == "RESTRICTED_MAGIC":
            if item.name == "Library Access Key":
                target.locked = False
                renpy.notify("RESTRICTED_ACCESS_GRANTED")
        else:
            renpy.notify("ERROR: INVALID_INTERFACE_TARGET")

    def use_pumpkin_pie():
        """Logic for eating the pie and getting a lantern."""
        if inventory.remove_by_name("Pumpkin Pie"):
            inventory.add_item(item_db["jack_o_lantern"])
            renpy.notify("CONVERSION_SUCCESSFUL: PIE -> LANTERN")
            store.selected_item = None 
        else:
            renpy.notify("ERROR: MODULE_NOT_FOUND")

    # --- NEW: Poison death mechanic for playtesting ---
    def use_poison():
        store.last_room = store.current_room
        renpy.jump('death_sequence_poison')

# --- STEP 2: The Manifest ---
define item_db = {
    "belladonna": Item("Belladonna", cost=0, description="A toxic perennial with bell shaped flowers and small berries. Legend has it these plants allow communication with the dead."),
    "mandrake": Item("Mandrake", cost=0, description="Highly disruptive root."),
    "catnip": Item("Catnip", cost=5, description="It's that good dank shit"),
    "cigarette": Item("Cigarette", cost=2, description="Something to take the edge off"),
    "bone": Item("Bone", cost=0, description="A bleached fragment"),
    "apple": Item("Apple", cost=0, description="Bright and flavorful"),
    "cherries": Item("Cherries", cost=2, description="Sweet fruit found in the mill."),
    "rusted_key": Item("Rusted Key", cost=0, description="Smells like cider."),
    "GATE_KEY": Item("GATE_KEY", cost=0, description="Access to Blushwood Court Gate"),
    "library_access_key": Item("Library Access Key", cost=0, description="A magnetic card for restricted areas."),
    "candle": Item("Candle", cost=0, description="An essential to any spell or ritual"),
    "cassette": Item("Cassette", cost=0, description="Recordable tape."),
    "soda": Item("Orange Soda", cost=4, description="A citrusy, bubbly delight. Made with real orange juice."),
    "pumpkin_pie": Item("Pumpkin Pie", cost=5, description="A warm dessert with the scent of Hallow's Eve", use_func=use_pumpkin_pie),
    "jack_o_lantern": Item("Jack o Lantern", cost=0, description="A carved pumpkin emitting a warm glow."),
    "poison": Item("Poison", cost=0, description="This will kill you.", use_func=use_poison),
    "Destruction_Scroll": Item("Destruction_Scroll", cost=0, description="A forbidden spell scroll capable of deleting world geometry."),
    "placeholder_a": Item("Placeholder_A", cost=0, description="A placeholder spell component. TBD."),
    "placeholder_b": Item("Placeholder_B", cost=0, description="A placeholder spell component. TBD."),
    "placeholder_c": Item("Placeholder_C", cost=0, description="A placeholder spell component. TBD."),
}

# --- STEP 3: World Creation ---

# --- BLUSHWOOD OBJECTS ---
default sector_gate = WorldObject(name = "GATE", description = "The door to an impossibly large castle.", img = Solid("#111", xsize=300, ysize=300), sprite = Solid("#333", xsize=100, ysize=200), x=450, y=50, locked=True)
default forest_dove = WorldObject("DOVE", "A nun standing in a ritual circle, praying.", Solid("#e15a00", xsize=300, ysize=300), Solid("#ffffff", xsize=50, ysize=50), x=500, y=300, can_talk=True, can_cast=True, label="talk_dove_blushwood")
default ghost_dealer = WorldObject("SCARLET_WRAITH", "An elegant red spectre drifts along the castle walls, watching you from a distance", Solid("#444", xsize=300, ysize=300), Solid("#fff", xsize=50, ysize=50), x=400, y=250, can_talk=False, can_cast=True, label="scarlet_gate")
default herb_belladonna = WorldObject(name = "Belladonna", description = "A toxic perennial with bell shaped flowers and small berries. Legend has it these plants allow communication with the dead.", img = Solid("#005500", xsize=300, ysize=300), sprite = Solid("#00ff00", xsize=40, ysize=40), x=700, y=450, can_take=True)
default crossroads_sign = WorldObject(
    name = "Automaton Guide",
    description = "A Turkey automaton. It seems to be broken and non-responsive.",
    img = Solid("#422", xsize=300, ysize=300),
    sprite = Solid("#543", xsize=40, ysize=60),
    x=480, y=300,
    can_talk=True,
    can_cast=True,
    label="talk_turkey"
)
default arcade_machine_fixed = False
default arcade_machine = WorldObject(
    name="ARCADE_MACHINE",
    description="A vintage arcade cabinet. The screen flickers with corrupted data.",
    img=Solid("#300", xsize=300, ysize=400),
    sprite=Solid("#411", xsize=50, ysize=90),
    x=700, y=250,
    can_talk=False,  # Can't talk until fixed
    can_cast=True,   # Can cast HACK on it
    label="talk_arcade_machine"
)
default herb_mandrake = WorldObject(name = "Mandrake", description = "Mimics the human form.", img = Solid("#321", xsize=300, ysize=300), sprite = Solid("#544", xsize=30, ysize=30), x=200, y=500, can_take=True)
default patch_cat = WorldObject(name="PATCH_CAT", description="A black cat.", img=Solid("#000", xsize=200, ysize=200), sprite=Solid("#111", xsize=30, ysize=30), x=300, y=400, can_talk=True, can_cast=True, label="talk_cat")
default maze_crow = WorldObject(name="CROW", description="A raven with a pixelated sheen.", img=Solid("#000", xsize=200, ysize=200), sprite=Solid("#000", xsize=30, ysize=30), x=200, y=200, can_talk=True, can_cast=True, label="talk_crow")
default item_bone = WorldObject(name="Bone", description="A bleached fragment.", img=Solid("#eee", xsize=200, ysize=200), sprite=Solid("#fff", xsize=20, ysize=20), x=150, y=520, can_take=True)
default item_bar_key = WorldObject(name="SILVER_KEY", description="A key to a trap door found inside a fountain.", img=Solid("#444", xsize=200, ysize=200), sprite=Solid("#333", xsize=20, ysize=20), x=180, y=550, can_take=True)
default jack_o_lantern = WorldObject(name="Jack o Lantern", description="A carved pumpkin emitting a warm, digital glow.", img=Solid("#f90", xsize=250, ysize=250), sprite=Solid("#d80", xsize=40, ysize=40), x=600, y=450, can_take=True)
default slot_machine = WorldObject(
    name="SLOT_MACHINE", 
    description="A vintage slot machine with glowing reels.", 
    img=Solid("#f00", xsize=300, ysize=400), 
    sprite=Solid("#f11", xsize=50, ysize=90), 
    x=500, y=300, 
    can_talk=True, 
    label="minigame_slots"
)
default mill_door = WorldObject(name="MILL_DOOR", description="The heavy oak door.", img=Solid("#321", xsize=300, ysize=300), sprite=Solid("#432", xsize=60, ysize=80), x=450, y=200, can_open=True, label="enter_mill")
default mill_dog = WorldObject(name="STRAY_DOG", description="A scruffy dog napping in the shade.", img=Solid("#642", xsize=250, ysize=200), sprite=Solid("#531", xsize=40, ysize=30), x=200, y=400, can_talk=True, can_cast=True, label="talk_dog")
default vending_machine = WorldObject(name="VENDING_MACHINE", description="A rusted 'GULP_CORP' machine.", img=Solid("#800", xsize=300, ysize=400), sprite=Solid("#911", xsize=50, ysize=90), x=700, y=250, can_talk=True, label="vending_machine_ui")
default npc_seagull = WorldObject(name="SEAGULL", description="A Seagull sits slumped against the wall. The gun by his hand hasn't moved in a while. Neither has he.", img=Solid("#003", xsize=300, ysize=400), sprite=Solid("#005", xsize=60, ysize=100), x=600, y=250, can_talk=True, can_cast=True, label="talk_seagull")
default item_apple = WorldObject(name="Apple", description="Organic data container.", img=Solid("#f00", xsize=200, ysize=200), sprite=Solid("#d00", xsize=25, ysize=25), x=200, y=450, can_take=True)
default mill_trap_door = WorldObject(name="TRAP_DOOR", description="A wooden door in the floor.", img=Solid("#210", xsize=300, ysize=200), sprite=Solid("#321", xsize=100, ysize=60), x=450, y=500, can_open=True, locked=True, label="enter_hidden_bar")
default npc_toucan = WorldObject("TOUCAN", "A bright bird offering a game of chance.", Solid("#f0f", xsize=300), Solid("#f0f", xsize=60), 300, 250, can_talk=True, label="talk_toucan")
default npc_hummingbird = WorldObject("Hummingbird", "A small woman sits at a broken Aerospace Invaders machine, lost in thought", Solid("#f0f", xsize=300), Solid("#f0f", xsize=60), 600, 350, can_talk=True, label="talk_hummingbird")
default vending_machine_mill = WorldObject("VENDING_MILL", "Unique mill dispenser.", Solid("#800", xsize=300), Solid("#911", xsize=50), 700, 250, can_talk=True, label="vending_machine_mill")
default npc_ptarmigan = WorldObject(name="PTARMIGAN", description="Woman by the riverbank.", img=Solid("#555", xsize=300, ysize=400), sprite=Solid("#666", xsize=60, ysize=100), x=400, y=300, can_talk=True, label="talk_ptarmigan")
default item_river_herb = WorldObject(name="River_Herb", description="A strange plant.", img=Solid("#055", xsize=200, ysize=200), sprite=Solid("#088", xsize=40, ysize=40), x=700, y=500, can_take=True)
default cabin_roots = WorldObject(name="MAGICAL_ROOTS", description="Giant, blocking roots.", img=Solid("#220", xsize=500, ysize=500), sprite=Solid("#331", xsize=200, ysize=300), x=400, y=100, can_cast=True, label="cabin_blocked")
# NEW: Cabin door (unlocks after roots deleted)
default cabin_door = WorldObject(name="CABIN_DOOR", description="A weathered cabin door.", img=Solid("#310", xsize=200, ysize=300), sprite=Solid("#421", xsize=60, ysize=90), x=500, y=220, can_open=True, locked=True, label="enter_cabin")

# Secretary (in Hedge Maze)
default npc_secretary = WorldObject(
    name="SECRETARY",
    description="A woman pacing in erratic circles, muttering about evidence and enemies.",
    img=Solid("#0fa", xsize=300, ysize=400),
    sprite=Solid("#0fa", xsize=60, ysize=100),
    x=300, y=350,
    can_talk=True,
    can_cast=True,
    label="talk_secretary"
)

# Falcon ghost (in Cabin Interior) - requires Ghost_Speak
default npc_falcon = WorldObject(
    name="FALCON",
    description="The spectral outline of a government field agent.",
    img=Solid("#0fa", xsize=300, ysize=400),
    sprite=Solid("#0fa", xsize=60, ysize=100),
    x=200, y=200,
    can_talk=False,
    can_cast=True,
    label="talk_falcon"
)

# Shrike ghost (in Core) - requires Ghost_Speak
default npc_shrike = WorldObject(
    name="SHRIKE",
    description="A spectral architect surrounded by shimmering lattice fragments.",
    img=Solid("#0fa", xsize=300, ysize=400),
    sprite=Solid("#0fa", xsize=60, ysize=100),
    x=500, y=300,
    can_talk=False,
    can_cast=True,
    label="talk_shrike"
)

# --- SUNDAPPLE OBJECTS ---
default npc_magpie = WorldObject("MAGIE", "Curious bird watching the crowd.", Solid("#000", xsize=300), Solid("#222", xsize=60), 100, 300, can_talk=True, label="talk_magpie")
default npc_goose = WorldObject("GOOSE", "Main merchant of the square.", Solid("#fff", xsize=300), Solid("#eee", xsize=60), 400, 200, can_talk=True, label="shop_goose")
default npc_ostrich = WorldObject("OSTRICH", "A tall bird selling niche wares.", Solid("#333", xsize=300), Solid("#444", xsize=60), 700, 150, can_talk=True, label="shop_ostrich")
default item_money = WorldObject("Money", "Lost currency units.", Solid("#0f0", xsize=100), Solid("#0f0", xsize=20), 500, 500, can_take=True)
default sundapple_vending = WorldObject("VENDING_SQUARE", "Dispensing city-grade modules.", Solid("#800", xsize=300), Solid("#911", xsize=50), 850, 250, can_talk=True, label="vending_sundapple")
default npc_raven = WorldObject("RAVEN", "The local archivist.", Solid("#111", xsize=300), Solid("#000", xsize=60), 200, 300, can_talk=True, label="talk_raven")
default library_pc = WorldObject("PC_TERMINAL", "OS_DATA_INDEX. Accessing files...", Solid("#0ff", xsize=300), Solid("#0ff", xsize=80), 500, 200, can_talk=True, can_cast=True, label="talk_library_pc")
default library_bin = WorldObject("NEWSPAPER_BIN", "Old headlines about the Manor.", Solid("#aaa", xsize=200), Solid("#aaa", xsize=50), 800, 450, can_talk=True, label="talk_library_bin")
default npc_pigeon = WorldObject("PIGEON", "Shelving books at a fast pace.", Solid("#888", xsize=300), Solid("#999", xsize=60), 150, 350, can_talk=True, label="talk_pigeon")
default shelf_1 = WorldObject("SHELF_HISTORY", "Records of the Sector.", Solid("#422", xsize=200), Solid("#422", xsize=40), 400, 200, can_talk=True, label="talk_shelf_history")
default shelf_2 = WorldObject("SHELF_CLERIC", "Ancient Cleric logs.", Solid("#422", xsize=200), Solid("#422", xsize=40), 600, 200, can_talk=True, label="talk_shelf_cleric")
default restricted_magic = WorldObject("RESTRICTED_MAGIC", "A glowing locked chest.", Solid("#f0f", xsize=300), Solid("#f0f", xsize=60), 500, 500, can_open=True, locked=True, label="label_restricted_magic")
default npc_pheasant = WorldObject("PHEASANT", "A diner regular.", Solid("#844", xsize=300), Solid("#844", xsize=60), 200, 300, can_talk=True, label="talk_pheasant")
default npc_cassowary = WorldObject("CASSOWARY", "A ghostly presence in a booth.", Solid("#444", xsize=300), Solid("#444", xsize=60), 500, 300, can_talk=False, can_cast=True, label="talk_cassowary")
default npc_heron = WorldObject("HERON", "A Heron taps his coffee cup as he reads a newspaper. He looks like he hasn't slept in weeks.", Solid("#f00", xsize=300), Solid("#f00", xsize=50), 800, 250, can_talk=True, label="talk_heron")
default npc_hen = WorldObject("HEN", "Kneeling in prayer.", Solid("#fff", xsize=300), Solid("#fff", xsize=60), 300, 400, can_talk=True, label="talk_hen")
default suncatcher = WorldObject("SUNCATCHER", "A device refracting solar data.", Solid("#0ff", xsize=400), Solid("#0ff", xsize=100), 500, 100)

# --- PARLOR OBJECTS ---
default npc_spider = WorldObject("SPIDER", "A small arachnid with a tiny headset.", Solid("#000", xsize=100), Solid("#000", xsize=20), 100, 100, can_talk=True, can_cast=True, label="talk_spider")
default npc_vampire_bat = WorldObject("VAMPIRE_BAT", "A bat hanging upside down.", Solid("#222", xsize=250), Solid("#222", xsize=50), 700, 100, can_talk=True, label="talk_vampire_bat")
default parlor_vending = WorldObject("VENDING_PARLOR", "Unique parlor dispenser.", Solid("#800", xsize=300), Solid("#911", xsize=50), 800, 250, can_talk=True, label="vending_machine_parlor")
default npc_vulture = WorldObject("VULTURE", "Runs the Parlor Cafe.", Solid("#333", xsize=300), Solid("#333", xsize=60), 400, 250, can_talk=True, label="shop_vulture")
default npc_flying_fox = WorldObject("FLYING_FOX", "Runs the Record Store.", Solid("#333", xsize=300), Solid("#333", xsize=60), 400, 250, can_talk=True, label="shop_flying_fox")
default npc_ghost_cat = WorldObject("GHOST_CAT", "Flickering behind the records.", Solid("#444", xsize=200), Solid("#444", xsize=30), 700, 400, can_talk=False, can_cast=True, label="talk_ghost_cat")
default item_cassette = WorldObject("Cassette", "Analog data.", Solid("#444"), Solid("#222"), 400, 400, can_take=True)

# --- NEW: Manor door (locked until Swan intro unlocks) and Swan NPC ---
default manor_door = WorldObject(name="MANOR_DOOR", description="An ornate gate leading into the manor.", img=Solid("#333", xsize=220, ysize=300), sprite=Solid("#555", xsize=70, ysize=100), x=500, y=250, can_open=True, locked=True, label="enter_manor")
default npc_swan = WorldObject("SWAN", "A spectral presence within the manor.", img=Solid("#ddd", xsize=300, ysize=300), sprite=Solid("#eee", xsize=60, ysize=90), x=520, y=240, can_talk=True, label="talk_swan_manor")

# --- 2. DEFINE ROOMS AT THE END ---

# --- SECTOR 01: BLUSHWOOD COURT ---
default blushwood_1 = Room("GATE", Solid("#1a1a1a"), north="blushwood_2", 
    contents=[forest_dove, ghost_dealer, herb_belladonna, sector_gate])

default blushwood_2 = Room("PLAZA", Solid("#2a2a2a"), south="blushwood_1", 
    north="manor_exterior", west="carousel", east="cider_mill", 
    contents=[crossroads_sign, herb_mandrake])

default manor_exterior = Room("MANOR_GATE", Solid("#050505"), south="blushwood_2", 
    contents=[manor_door])

default carousel = Room("CAROUSEL", Solid("#331100"), east="blushwood_2", 
    west="hedge_maze", contents=[patch_cat, jack_o_lantern])

default hedge_maze = Room("HEDGE_MAZE", Solid("#111100"), east="carousel", 
    contents=[maze_crow, item_bone, item_bar_key, npc_secretary])

default cider_mill = Room("CIDER_MILL", Solid("#112211"), west="blushwood_2", 
    north="river_bank", contents=[mill_door, mill_dog, vending_machine_mill])

default cider_mill_interior = Room("CIDER_MILL_INTERIOR", Solid("#050505"), south="cider_mill", 
    contents=[npc_seagull, item_apple, mill_trap_door])

default hidden_bar = Room("HIDDEN_BAR", Solid("#200"), south="cider_mill_interior",
    contents=[npc_toucan, npc_hummingbird, slot_machine, arcade_machine])

default river_bank = Room("RIVER", Solid("#001a1a"), south="cider_mill", 
    north="cabin_exterior", contents=[npc_ptarmigan, item_river_herb])

default cabin_exterior = Room("CABIN_EXTERIOR", Solid("#1a0000"), south="river_bank", 
    contents=[cabin_roots, cabin_door])

# NEW: Cabin interior and Manor interior rooms
default cabin_interior = Room("CABIN_INTERIOR", Solid("#2a0000"), south="cabin_exterior",
    contents=[npc_falcon])
default manor_interior = Room("MANOR_INTERIOR", Solid("#0a0a0a"), south="manor_exterior",
    north="manor_garden",
    contents=[])

# Manor mini-dungeon rooms
default manor_garden = Room(
    name="GARDEN",
    art=Solid("#040", xsize=1000, ysize=600),
    south="manor_interior",
    north="manor_underground"
)

default manor_underground = Room(
    name="UNDERGROUND",
    art=Solid("#111", xsize=1000, ysize=600),
    south="manor_garden",
    north="manor_core"
)

default manor_core = Room(
    name="CORE",
    art=Solid("#202", xsize=1000, ysize=600),
    south="manor_underground",
    contents=[npc_shrike]
)

# SUNDAPPLE SQUARE 
default sundapple_1 = Room("MALL", Solid("#ffcc00"), north="sd_church", 
    east="sd_library", west="sd_diner", 
    contents=[npc_magpie, npc_goose, npc_ostrich, item_money, sundapple_vending])

default sd_library = Room("LIBRARY_LOBBY", Solid("#422"), west="sundapple_1", 
    north="sd_shelves", contents=[npc_raven, library_pc, library_bin])

default sd_shelves = Room("LIBRARY_SHELVES", Solid("#311"), south="sd_library", 
    contents=[npc_pigeon, shelf_1, shelf_2, restricted_magic])

default sd_diner = Room("DINER", Solid("#600"), east="sundapple_1", 
    contents=[npc_pheasant, npc_cassowary, npc_heron])

default sd_church = Room("WORSHIP", Solid("#fff"), south="sundapple_1", 
    north="sd_sanctum", contents=[npc_hen])

default sd_sanctum = Room("INNER_SANCTUM", Solid("#0ff"), south="sd_church", 
    contents=[suncatcher])

# PARLOR DISTRICT 
default parlor_1 = Room("CAVE_ENTRANCE", Solid("#404"), east="p_cafe", 
    west="p_records", contents=[npc_spider, npc_vampire_bat, item_money, parlor_vending])

default p_cafe = Room("CAFE", Solid("#303"), west="parlor_1", contents=[npc_vulture])

default p_records = Room("RECORD_STORE", Solid("#202"), east="parlor_1", 
    contents=[npc_flying_fox, npc_ghost_cat, item_cassette])

default cave_depths = Room("CAVE_DEPTHS", Solid("#000"), south="parlor_1")

# --- INITIAL STATE ---
default dove_moved_to_sanctum = False
default raven_moved_to_cafe = False
default interaction_mode = "main" 
default current_room = "blushwood_1" 
default current_target = None
default can_speak_with_animals = False



