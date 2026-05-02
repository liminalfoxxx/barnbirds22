# Define all possible spells in the game here

# These are "templates" that you can award to the player later with:
#   $ inventory.learn_spell(<spell_var>)
default ghost_speak_prog = Spell("Speak_With_Ghosts", {"Cassette": 1, "Belladonna": 1, "Mugwort": 1}, "Establishes a spectral link. Allows communication with the dead.", frequency_type="Death")
default animal_speak_prog = Spell("Speak_With_Animals", {"Bird of Paradise": 1, "Catnip": 1, "Bone": 1}, "Activates the Animal Translator. Allows communication with animals.", frequency_type="Primal")
default satellite_prog = Spell("Satellite", {"Apple": 1, "Gold Foil": 1, "Sunflower": 1}, "Displays hidden data signals for a living target: Frequency, Signal, Status.", frequency_type="Life")
default heal_blight_prog = Spell("Heal_Blight", {"Snowdrop": 1, "Lemon Balm": 1, "Candle": 1}, "Cleanses a living system of the Blight. Can only be cast on the infected.", frequency_type="Seelie")
default prune_prog = Spell("Prune", {"Foxglove": 1, "Sassafras": 1, "Corrupted VHS Tape": 1}, "Clears corrupted growth from sealed pathways.", frequency_type="Unseelie")
default money_manifest_prog = Spell("Money_Manifest", {"Honeycomb": 1, "Blood": 1, "Gold Coin": 1}, "Manifests currency through blood ritual. Amount is randomized.", frequency_type="Blood")
default hack_prog = Spell("Hack", {"Circuit Board": 1, "Copper Wire": 1, "Quartz": 1}, "Interfaces with devices and automation systems to unlock hidden data or alter properties.", frequency_type="Storm")


init python:
    def execute_cast_sequence(program, target, inv):
        """
        Central router for resolving a spell cast on the current_target.

        program: a Spell instance from inventory.known_spells
        target:  a WorldObject currently selected (current_target), or None for self-targeting spells
        inv:     the player's Inventory
        """
        if not program:
            return

        # 1) Normalize program name for matching
        program_id = program.name.upper().replace(" ", "_").replace(".EXE", "")

        # Compute target_id only when a target is provided
        if target is not None:
            target_id = target.name.upper().replace(" ", "_")
        else:
            target_id = None

        # Debug helper in Shift+O
        print(f"CLEAN_ID: Program({program_id}) Target({target_id})")

        # Check and spend frequency before anything else
        if program.frequency_type:
            if not inv.spend_frequency(program.frequency_type):
                renpy.notify("ERROR: INSUFFICIENT_FREQUENCY")
                renpy.jump("overworld_loop")
                return

        # 2) Dispatch by program_id

        # --- SPEAK_WITH_GHOSTS LOGIC ---
        if program_id == "SPEAK_WITH_GHOSTS":
            if target is None:
                renpy.notify("ERROR: NO_TARGET_SELECTED")
                renpy.jump("overworld_loop")
                return
            valid_targets = {"SCARLET_TANAGER", "SCARLET_WRAITH", "FALCON", "SHRIKE", "SNOWY_OWL", "KITE", "MURMURATION", "LOST_SOUL", "CASSOWARY", "ROOSTER", "GHOST_CAT"}
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

        # --- SPEAK_WITH_ANIMALS LOGIC ---
        elif program_id == "SPEAK_WITH_ANIMALS":
            if target is None:
                renpy.notify("ERROR: NO_TARGET_SELECTED")
                renpy.jump("overworld_loop")
                return
            valid_targets = {"PATCH_CAT", "STRAY_DOG", "CROW", "SPIDER", "STRAWBERRY_COW", "ROYAL_UNICORN"}
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

        # --- SATELLITE LOGIC ---
        elif program_id == "SATELLITE":
            if target is None:
                renpy.notify("ERROR: NO_TARGET_SELECTED")
                renpy.jump("overworld_loop")
                return
            if not hasattr(target, "sat_frequency"):
                renpy.notify("ERROR: NO_SIGNAL_DETECTED")
                renpy.jump("overworld_loop")
                return
            if inv.execute_program(program):
                renpy.show_screen("satellite_screen", target=target)
            else:
                renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                renpy.jump("overworld_loop")

        # --- HEAL_BLIGHT LOGIC ---
        elif program_id == "HEAL_BLIGHT":
            if target is None:
                renpy.notify("ERROR: NO_TARGET_SELECTED")
                renpy.jump("overworld_loop")
                return
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

        # --- PRUNE LOGIC ---
        elif program_id == "PRUNE":
            if target is None:
                renpy.notify("ERROR: NO_TARGET_SELECTED")
                renpy.jump("overworld_loop")
                return
            if target_id in {"MAGICAL_ROOTS", "CABIN_DOOR"}:
                if not getattr(store, "cabin_roots_deleted", False):
                    if inv.execute_program(program):
                        renpy.notify("PRUNE.EXE SUCCESSFUL. Corruption cleared.")
                        store.cabin_roots_deleted = True
                        renpy.jump("after_prune_roots")
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")
                else:
                    renpy.notify("Nothing left to prune here.")
                    renpy.jump("overworld_loop")
            else:
                renpy.notify("ERROR: THIS PROGRAM'S CODE WILL NOT WORK HERE.")
                renpy.jump("overworld_loop")

        # --- MONEY_MANIFEST LOGIC ---
        elif program_id == "MONEY_MANIFEST":
            if inv.execute_program(program):
                amount = renpy.random.randint(1, 99)
                inv.earn(amount)
                renpy.notify("MANIFEST_SUCCESSFUL: +{}_UNITS".format(amount))
                renpy.jump("overworld_loop")
            else:
                renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                renpy.jump("overworld_loop")

        # --- HACK LOGIC ---
        elif program_id == "HACK":
            if target is None:
                renpy.notify("ERROR: NO_TARGET_SELECTED")
                renpy.jump("overworld_loop")
                return
            valid_targets = {"AUTOMATON_GUIDE", "PC_TERMINAL", "ARCADE_MACHINE", "VENDING_MACHINE", "VENDING_MILL", "VENDING_SQUARE", "VENDING_PARLOR", "SLOT_MACHINE"}
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
                        renpy.jump("hack_pc_terminal")
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")

                # Arcade Machine fix
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

                # Vending machines
                elif target_id in {"VENDING_MACHINE", "VENDING_MILL", "VENDING_SQUARE", "VENDING_PARLOR"}:
                    if inv.execute_program(program):
                        store.hack_target = target
                        renpy.jump("hack_vending_machine")
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")

                # Slot machine
                elif target_id == "SLOT_MACHINE":
                    if inv.execute_program(program):
                        store.hack_target = target
                        renpy.jump("hack_slot_machine")
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

                                # Self-targeting spells vs target-required spells
                                $ _is_self_spell = selected_program.name.upper().replace(" ", "_") == "MONEY_MANIFEST"

                                if _is_self_spell:
                                    if selected_program.can_cast(inventory):
                                        textbutton "[[ EXECUTE_PROGRAM ]]":
                                            action [Hide("spellbook_screen"),
                                                    Function(execute_cast_sequence, selected_program, None, inventory)]
                                            text_size 40
                                            text_idle_color "#0f0"
                                            text_hover_color "#fff"
                                            xalign 0.5
                                    else:
                                        text "[[ INSUFFICIENT_RESOURCES ]]" color "#ff8000" size 40 xalign 0.5
                                else:
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

                                null height 20
                                label "FREQUENCY_LEVELS" text_color "#e15a00"
                                for freq_name in ["Primal", "Seelie", "Unseelie", "Storm", "Life", "Death", "Blood", "Void"]:
                                    hbox:
                                        spacing 10
                                        $ freq_label = "> " + freq_name.upper() + "....."
                                        $ freq_val = 0 if freq_name == "Void" else inventory.frequency[freq_name]
                                        $ is_active = selected_program.frequency_type == freq_name
                                        text "[freq_label]" color ("#fff" if is_active else "#e15a00") size 22
                                        text "[freq_val]" color ("#0f0" if is_active else "#ccc") size 22
                        else:
                            vbox:
                                align (0.5, 0.4)
                                text "SELECT_PROGRAM_FOR_ANALYSIS" color "#444" size 34


screen satellite_screen(target):
    modal True
    zorder 200
    add Solid("#0d0d0d", alpha=0.85)

    frame:
        background Solid("#e15a00")
        padding (2, 2)
        align (0.5, 0.5)
        xsize 600
        frame:
            background Solid("#0d0d0d")
            padding (40, 40)
            vbox:
                spacing 20
                label "SATELLITE.EXE // SIGNAL_SCAN" text_color "#e15a00" text_size 30
                null height 10

                text "[target.name]" color "#ff8000" size 36

                null height 10
                add Solid("#333", xsize=520, ysize=2)
                null height 10

                hbox:
                    spacing 20
                    text "FREQUENCY:" color "#e15a00" size 24 yalign 0.5
                    text "[target.sat_frequency]" color "#0f0" size 24 yalign 0.5

                hbox:
                    spacing 20
                    text "SIGNAL:" color "#e15a00" size 24 yalign 0.5
                    text "[target.sat_signal]" color "#0f0" size 24 yalign 0.5

                hbox:
                    spacing 20
                    text "STATUS:" color "#e15a00" size 24 yalign 0.5
                    text "[target.sat_status]" color "#0f0" size 24 yalign 0.5

                null height 20
                textbutton "[[ CLOSE_SCAN ]]":
                    action Hide("satellite_screen")
                    xalign 0.5
                    text_size 30
                    text_idle_color "#e15a00"
                    text_hover_color "#fff"
