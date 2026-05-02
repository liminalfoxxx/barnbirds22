# Define all possible spells in the game here

# These are "templates" that you can award to the player later with:
#   $ inventory.learn_spell(<spell_var>)
# The player currently starts with Ghost_Speak.exe and Speak with Animals from script.rpy.
default ghost_speak_prog = Spell("Ghost_Speak", {"Belladonna": 1, "Candle": 1, "Cassette": 1})
default animal_speak_prog = Spell("Animal_Speak", {"Catnip": 1, "Bone": 1, "Candle": 1})

# DELETE (Destruction) – uses the Destruction Scroll
default delete_prog = Spell("Delete", {"Destruction_Scroll": 1}, "Deletes obstacles in your way. 'WARNING: HIGHLY UNSTABLE CODE.'")

# HEAL_BLIGHT – heals infected living targets (Seagull, Secretary, Ptarmigan)
default heal_blight_prog = Spell("Heal_Blight", {"Placeholder_A": 1, "Placeholder_B": 1, "Placeholder_C": 1}, "Cleanses a living system of the Blight. Can only be cast on the infected.")

# HACK – previously Power_Surge, opens special device dialogues
# Requires the item names exactly as in your item_db: "Orange Soda" and "Cassette".
default hack_prog = Spell("Hack", {"Orange Soda": 1, "Cassette": 1}, "Interfaces with devices and automation systems to unlock dialogues.")


init python:
    def execute_cast_sequence(program, target, inv):
        """
        Central router for resolving a spell cast on the current_target.

        program: a Spell instance from inventory.known_spells
        target:  a WorldObject currently selected (current_target)
        inv:     the player's Inventory
        """
        if not target or not program:
            return

        # 1) Normalize names for matching
        program_id = program.name.upper().replace(" ", "_").replace(".EXE", "")
        target_id = target.name.upper().replace(" ", "_")

        # Debug helper in Shift+O
        print(f"CLEAN_ID: Program({program_id}) Target({target_id})")

        # 2) Dispatch by program_id

        # --- GHOST SPEAK LOGIC ---
        if program_id == "GHOST_SPEAK":
            # Valid spectral targets
            valid_targets = {"SCARLET_TANAGER", "FALCON", "SHRIKE", "LOST_SOUL", "CASSOWARY", "ROOSTER", "GHOST_CAT"}
            if target_id in valid_targets:
                # If the ghost hasn't been "decrypted" to can_talk, pay the recipe and enable
                if not target.can_talk:
                    if inv.execute_program(program):
                        target.can_talk = True
                        target.description = "Link Established. Spectral data decrypted."
                        renpy.notify("COMPILATION_SUCCESSFUL")
                        renpy.jump(target.label)
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")
                else:
                    # Already decrypted - just talk
                    renpy.jump(target.label)
            else:
                renpy.notify("INCOMPATIBLE_SUBJECT_TYPE")
                renpy.jump("overworld_loop")

        # --- ANIMAL SPEAK LOGIC ---
        elif program_id in {"ANIMAL_SPEAK", "SPEAK_WITH_ANIMALS"}:
            valid_targets = {"PATCH_CAT", "STRAY_DOG", "CROW", "SPIDER"}
            if target_id in valid_targets:
                if not store.can_speak_with_animals:
                    if inv.execute_program(program):
                        store.can_speak_with_animals = True
                        renpy.notify("ANIMAL_TRANSLATOR.EXE_ACTIVE")
                        renpy.jump(target.label)
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")
                else:
                    # Translator already active - just talk
                    renpy.jump(target.label)
            else:
                renpy.notify("INCOMPATIBLE_SUBJECT_TYPE")
                renpy.jump("overworld_loop")

        # --- DELETE / DESTRUCTION LOGIC ---
        elif program_id == "DELETE":
            # Currently only used for the MAGICAL_ROOTS
            if target_id == "MAGICAL_ROOTS":
                if inv.execute_program(program):
                    renpy.notify("PROGRAM DELETE SUCCESSFUL. Roots eradicated.")
                    store.cabin_roots_deleted = True
                    renpy.jump("after_delete_roots")
                else:
                    renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                    renpy.jump("overworld_loop")
            else:
                renpy.notify("ERROR: THIS PROGRAM'S CODE WILL NOT WORK HERE.")
                renpy.jump("overworld_loop")

        # --- HEAL_BLIGHT LOGIC ---
        elif program_id == "HEAL_BLIGHT":
            # One-time cures with simple flags
            if target_id == "SEAGULL" and not getattr(store, "seagull_healed", False):
                if inv.execute_program(program):
                    setattr(store, "seagull_healed", True)
                    renpy.jump("heal_seagull")
                else:
                    renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                    renpy.jump("overworld_loop")

            elif target_id == "SECRETARY" and not getattr(store, "secretary_healed", False):
                if inv.execute_program(program):
                    setattr(store, "secretary_healed", True)
                    renpy.jump("heal_secretary")
                else:
                    renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                    renpy.jump("overworld_loop")

            elif target_id == "PTARMIGAN" and not getattr(store, "ptarmigan_healed", False):
                if inv.execute_program(program):
                    setattr(store, "ptarmigan_healed", True)
                    renpy.jump("heal_ptarmigan")
                else:
                    renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                    renpy.jump("overworld_loop")

            else:
                renpy.notify("This spell will not work on this target... or they've already been healed.")
                renpy.jump("overworld_loop")

        # --- HACK LOGIC ---
        elif program_id == "HACK":
            valid_targets = {"AUTOMATON_GUIDE", "PC_TERMINAL", "ARCADE_MACHINE"}
            if target_id in valid_targets:
                # Automaton Guide one-shot activation
                if target_id == "AUTOMATON_GUIDE" and not getattr(store, "turkey_activated", False):
                    if inv.execute_program(program):
                        setattr(store, "turkey_activated", True)
                        renpy.jump("surge_turkey")
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")
                
                # PC Terminal dialog
                elif target_id == "PC_TERMINAL":
                    if inv.execute_program(program):
                        renpy.jump("hack_terminal")
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")
                
                # NEW: Arcade Machine fix
                elif target_id == "ARCADE_MACHINE" and not getattr(store, "arcade_machine_fixed", False):
                    if inv.execute_program(program):
                        setattr(store, "arcade_machine_fixed", True)
                        target.can_talk = True
                        target.description = "The screen flickers to life! The game is operational."
                        renpy.notify("ARCADE_MACHINE SUCCESSFULLY REPAIRED")
                        renpy.jump(target.label)
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")
                
                else:
                    renpy.notify("Nothing to hack here! Or this device is already functioning.")
                    renpy.jump("overworld_loop")
            else:
                renpy.notify("INCOMPATIBLE_SUBJECT_TYPE")
                renpy.jump("overworld_loop")

        # System Reboot / default
        elif program_id == "SYSTEM_REBOOT":
            renpy.notify("REBOOT_SEQUENCE_INITIALIZED")
            renpy.jump("overworld_loop")

        else:
            renpy.notify(f"UNKNOWN_PROGRAM: {program_id}")
            renpy.jump("overworld_loop")


# --- SCREENS ---

default selected_program = None

screen spellbook_screen():
    modal True
    zorder 100
    add Solid("#0d0d0d")

    frame:
        background None
        padding (50, 50)
        xfill True
        yfill True

        hbox:
            spacing 40

            # --- LEFT COLUMN: Known Programs ---
            vbox:
                xsize 450
                frame:
                    background Solid("#e15a00")
                    padding (2, 2)
                    yfill True
                    frame:
                        background Solid("#0d0d0d")
                        padding (10, 10)
                        xfill True
                        yfill True
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                spacing 5
                                if not inventory.known_spells:
                                    text "NO PROGRAMS INSTALLED" color "#444" size 24 xpos 10
                                else:
                                    for s in inventory.known_spells:
                                        button:
                                            action SetVariable("selected_program", s)
                                            xfill True
                                            ysize 50
                                            background (Solid("#e15a00") if selected_program == s else None)
                                            text "> [s.name]":
                                                xpos 15
                                                yalign 0.5
                                                color ("#0d0d0d" if selected_program == s else "#e15a00")
                                                size 26

            # --- RIGHT COLUMN: Analysis & Execution ---
            vbox:
                xfill True
                spacing 20

                hbox:
                    xfill True
                    label "PROGRAM_MANIFEST.EXE" text_size 45 text_color "#e15a00"
                    textbutton " [[ X ]] ":
                        action [Hide("spellbook_screen"), SetVariable("selected_program", None)]
                        xalign 1.0
                        text_idle_color "#e15a00"
                        text_hover_color "#f00"

                frame:
                    background Solid("#e15a00")
                    padding (2, 2)
                    xfill True
                    yfill True
                    frame:
                        background Solid("#0d0d0d")
                        padding (30, 30)
                        xfill True
                        yfill True

                        if selected_program:
                            vbox:
                                spacing 20

                                # Optional program image
                                if renpy.loadable("gui/programs/" + selected_program.name + ".png"):
                                    add "gui/programs/[selected_program.name].png" xalign 0.5
                                else:
                                    add Solid("#222", xsize=300, ysize=200) xalign 0.5

                                text "[selected_program.name]" size 40 color "#ff8000"
                                text "[selected_program.description]" size 24 color "#ccc"

                                null height 20
                                label "HARDWARE_REQUIREMENTS:" text_color "#e15a00"

                                # Ingredients list with counts
                                hbox:
                                    spacing 50
                                    for ingredient, amount in selected_program.recipe.items():
                                        vbox:
                                            if inventory.count(ingredient) >= amount:
                                                add Solid("#444", xsize=80, ysize=80)
                                                text "[ingredient]" color "#0f0" size 18 xalign 0.5
                                            else:
                                                add Solid("#222", xsize=80, ysize=80)
                                                text "[ingredient]" color "#ff8000" size 18 xalign 0.5
                                            text "[inventory.count(ingredient)] / [amount]" size 20 xalign 0.5

                                null height 40

                                # Only allow execute if the player has all required items
                                if selected_program.can_cast(inventory):
                                    textbutton "[[ EXECUTE_PROGRAM ]]":
                                        action If(
                                            current_target,
                                            [ Hide("spellbook_screen"),
                                              Function(execute_cast_sequence, selected_program, current_target, inventory) ],
                                            None
                                        )
                                        text_size 40
                                        text_insensitive_color "#222"
                                        text_idle_color "#0f0"
                                        text_hover_color "#fff"
                                        xalign 0.5
                                else:
                                    text "[[ INSUFFICIENT_RESOURCES ]]" color "#ff8000" size 40 xalign 0.5
                        else:
                            vbox:
                                align (0.5, 0.4)
                                text "SELECT_PROGRAM_FOR_ANALYSIS" color "#444" size 34
