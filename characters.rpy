# characters.rpy

define d = Character(
    "Dove",
    color="#e1c400",
    window_background=None,
    image="dove",
    what_color="#e1c400",
)
define r = Character(
    "Raven",
    color="#4700d1",
    window_background=None,
    image="raven",
    what_color="#7755ee",
)
define s = Character(
    "Swan",
    color="#ffffff",
    window_background=None,
    image="swan",
    what_color="#ffffff",
)
define seagull = Character(
    "Seagull",
    color="#8899cc",
    window_background=None,
    image="seagull",
    what_color="#8899cc",
)
define sca = Character(
    "Scarlet Tanager",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define turk = Character(
    "AUTOMATON GUIDE",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define cat = Character(
    "Cat",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define crow = Character(
    "Crow",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define tou = Character(
    "Toucan",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define hum = Character(
    "Hummingbird",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define pta = Character(
    "Ptarmigan",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define mag = Character(
    "Magpie",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define ost = Character(
    "Ostrich",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define dog = Character(
    "Dog",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define phe = Character(
    "Pheasant",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define cas = Character(
    "Cassowary",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define heron = Character(
    "Heron",
    color="#0fa",
    window_background=None,
    what_italic=False,
)
define hen = Character(
    "Hen",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define sec = Character(
    "Secretary",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define fal = Character(
    "Falcon",
    color="#0fa",
    window_background=None,
    what_italic=True,
)

define shrike = Character(
    "Shrike",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define robin = Character(
    "Robin",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define can = Character(
    "Canary",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define peacock = Character(
    "Peacock",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define p = Character(
    "Pigeon",
    color="#0fa",
    window_background=None,
    what_italic=False,
)
define sys = Character(
    "System",
    color="#e15a00",
    window_background=None,
    what_prefix="SYSTEM: ",
    what_italic=False,
)
# Additional speakers used in scripts
define goose = Character("Goose", color="#0fa", window_background=None, what_italic=True)
define vulture = Character("Vulture", color="#0fa", window_background=None, what_italic=True)
define flying_fox = Character("Flying Fox", color="#0fa", window_background=None, what_italic=True)
define rooster = Character("Rooster", color="#0fa", window_background=None, what_italic=True)
define ghost_cat = Character("Ghost Cat", color="#0fa", window_background=None, what_italic=True)
define spider = Character("Spider", color="#0fa", window_background=None, what_italic=True)
define vampire_bat = Character("Vampire Bat", color="#0fa", window_background=None, what_italic=True)
define ghost = Character("THE GHOST", color="#0fa", window_background=None, what_italic=True)

# Optional programmatic lookup
default character_db = {
    "dove": d,
    "raven": r,
    "swan": s,
    "seagull": seagull,
    "pigeon": p,
    "ptarmigan": pta,
    "system": sys,
    "turkey": turk,
    "scarlet": sca,
    "cat": cat,
    "dog": dog,
    "crow": crow,
    "toucan": tou,
    "magpie": mag,
    "ostrich": ost,
    "pheasant": phe,
    "cassowary": cas,
    "hen": hen,
    "goose": goose,
    "vulture": vulture,
    "flying_fox": flying_fox,
    "rooster": rooster,
    "ghost_cat": ghost_cat,
    "spider": spider,
    "vampire_bat": vampire_bat,
    "ghost": ghost,
    "hummingbird": hum,
    "shrike": shrike,
    "secretary": sec,
    "falcon": fal,
    "robin": robin,
    "canary": can,
    "peacock": peacock,
}