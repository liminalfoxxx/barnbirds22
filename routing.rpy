# Routing skeleton: centralized flags and one-shot triggers

init offset = -5

# Route stages (small integers are easy to reason about)
default dove_route_stage = 0        # 0 = gate talk only; 1 = saw cabin; 2 = post-roots; 3 = sanctum invite; 4 = LSD; 5 = post-trip
default raven_route_stage = 0       # 0 = library; 1 = invited to cafe; 2 = cafe; 3 = locked-in
default swan_route_stage = 0        # 0 = not seen; 1 = intro after delete roots; 2 = manor unlocked; 3 = locked-in

# One-shot triggers
default dove_saw_cabin = False      # flip when entering cabin_exterior for first time
default swan_intro_shown = False    # flip when showing Swan intro label

# Theme: "orange" (default, first half) vs "mac" (AVM Facility)
default ui_theme = "orange"

# Door unlock flags (used by overworld objects)
default manor_unlocked = False
default cabin_unlocked = False

# Call this once each loop to react to room and state changes.
init python:
    def check_room_triggers():
        # Dove: first time entering Cabin Exterior
        if store.current_room == "cabin_exterior" and not store.dove_saw_cabin:
            store.dove_saw_cabin = True
            store.dove_route_stage = max(store.dove_route_stage, 1)
            renpy.call_in_new_context("dove_cabin_hint")

        # Dove: after deleting roots, invite to sanctum and move her
        if getattr(store, "cabin_roots_deleted", False) and store.dove_route_stage < 2:
            store.dove_route_stage = 2
            renpy.call_in_new_context("dove_sanctum_invite")

        # Swan: intro after roots deleted (but only once)
        if getattr(store, "cabin_roots_deleted", False) and not store.swan_intro_shown:
            store.swan_intro_shown = True
            store.swan_route_stage = max(store.swan_route_stage, 1)
            renpy.call_in_new_context("swan_intro")

        # Cabin door unlock after roots deleted
        if getattr(store, "cabin_roots_deleted", False) and not getattr(store, "cabin_unlocked", False):
            store.cabin_unlocked = True
            try:
                store.cabin_door.locked = False
            except Exception:
                pass

        # Keep door lock states in sync (defensive in case doors are not yet defined)
        if getattr(store, "cabin_unlocked", False):
            try:
                store.cabin_door.locked = False
            except Exception:
                pass

        if getattr(store, "manor_unlocked", False):
            try:
                store.manor_door.locked = False
            except Exception:
                pass

# --- Labels used by triggers (stub text; replace with your writing) ---

label dove_cabin_hint:
    # Called when player enters Cabin Exterior for the first time.
    d "The path to the cabin... it's dangerous. If you need guidance, the Library may help."
    return

label dove_sanctum_invite:
    # Called after roots are deleted. Move Dove to the Inner Sanctum.
    $ dove_moved_to_sanctum = True
    $ dove_route_stage = 3
    d "Meet me at the Inner Sanctum in Sundapple Square. There's something I must show you."
    return

# Dove lock-in (LSD trip)
label dove_lock_in_choice:
    d "Will you stay with me through the trip?"
    menu:
        "Yes (lock in Dove route)":
            $ current_route = "dove"
            $ avm_facility_accessible = True
            $ dove_route_stage = 4
            jump dove_lsd_trip
        "Not yet":
            return

label dove_lsd_trip:
    # Introduce LSDEMON, visuals, etc. When done:
    $ dove_route_stage = 5
    jump dove_post_trip

label dove_post_trip:
    d "Thank you for watching over me. The AVM Facility node will accept your clearance now."
    return

# Raven skeleton

label raven_invite_cafe:
    # Call this after granting forbidden magic at the Library
    $ raven_route_stage = 1
    r "Meet me at the Cafe in the Parlor District. I have something for you."
    return

label raven_move_to_cafe:
    $ raven_moved_to_cafe = True
    $ raven_route_stage = 2
    return

label raven_lock_in_choice:
    r "Do you want to commit to my route?"
    menu:
        "Yes (lock in Raven route)":
            $ current_route = "raven"
            $ avm_facility_accessible = True
            $ raven_route_stage = 3
            return
        "Not yet":
            return

# Swan skeleton

label swan_intro:
    s "…"
    s "Out of my way."
    menu:
        "Who are you?":
            s "The reason you're still breathing."
            s "…"
            s "I'm going to the Manor. Find me there."
        "What are you?":
            s "A serial killer."
            s "I'm going to the Manor. Find me there."
        "What happened here?":
            s "Not here."
            s "The Manor. We can talk there."
        "(move out of his way)":
            s "…"
            s "Good instincts."
            s "Come find me at the Manor when you're ready. There are things I'd like to discuss with you."
    $ swan_route_stage = 2
    $ manor_unlocked = True
    $ manor_door.locked = False
    return

label swan_lock_in_choice:
    "SWAN" "Will you walk the rest of the way with me?"
    menu:
        "Yes (lock in Swan route)":
            $ current_route = "swan"
            $ avm_facility_accessible = True
            $ swan_route_stage = 3
            return
        "Not yet":
            return

# Optional: a stub for the 'ghost life story' mini-spell concept
label ghost_life_story_stub:
    # Swap to images/text sequence only; no overworld needed here.
    "SYSTEM" "Reconstructing past signal..."
    "..."
    return