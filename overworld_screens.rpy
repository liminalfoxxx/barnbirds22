

init python:
    def OS_Window(w, h):
        return Composite(
            (w, h),
            (0, 0), Solid("#000", xsize=w, ysize=h),
            (0, 0), Solid("#e15a00", xsize=w, ysize=2),
            (0, h-2), Solid("#e15a00", xsize=w, ysize=2),
            (0, 0), Solid("#e15a00", xsize=2, ysize=h),
            (w-2, 0), Solid("#e15a00", xsize=2, ysize=h)
        )

screen world_interface():
    zorder 10
    modal True 
    add Solid("#0d0d0d")

    # Define room_data at the very start so all components can see it
    $ room_data = getattr(store, current_room)

    frame:
        background None
        padding (30, 30)
        xfill True yfill True
        ypos 65

        hbox:
            spacing 20

            # --- LEFT COLUMN (View & Navigation) ---
            vbox:
                spacing 20

                # 1. ENVIRONMENT VIEW
                fixed:
                    xsize 1000 ysize 600
                    add OS_Window(1000, 600)
                    add room_data.art

                    for item in room_data.contents:
                        imagebutton:
                            idle item.sprite
                            hover item.sprite 
                            xpos item.x ypos item.y
                            action SetVariable("current_target", item)

                # 2. ROOM GRID (Navigation Cluster)
                fixed:
                    xsize 1000 ysize 300
                    add OS_Window(1000, 300)

                    hbox:
                        align (0.5, 0.5)
                        spacing 60

                        # WEST
                        if room_data.west:
                            $ west_room = getattr(store, room_data.west)
                            textbutton " [[ TO [west_room.name] ]] ":
                                action [SetVariable("current_room", room_data.west), SetVariable("current_target", None)]
                        else:
                            null width 120

                        # CENTER COLUMN (North, Map, South)
                        vbox:
                            spacing 20
                            xsize 180

                            if room_data.north:
                                $ north_room = getattr(store, room_data.north)
                                textbutton " [[ TO [north_room.name] ]] ":
                                    action If(current_room == "blushwood_1" and sector_gate.locked, 
                                             Notify("ERR: GATE_LOCKED. ACCESS_KEY_REQUIRED."),
                                             [SetVariable("current_room", room_data.north), SetVariable("current_target", None)]) 
                                    xalign 0.5
                            else:
                                null height 35

                            fixed:
                                xsize 180 ysize 100
                                add OS_Window(180, 100)
                                text "[room_data.name]" align (0.5, 0.5) size 16 color "#e15a00" bold True

                            if room_data.south:
                                $ south_room = getattr(store, room_data.south)
                                textbutton " [[ TO [south_room.name] ]] ":
                                    action [SetVariable("current_room", room_data.south), SetVariable("current_target", None)] 
                                    xalign 0.5
                            else:
                                null height 35

                        # EAST
                        if room_data.east:
                            $ east_room = getattr(store, room_data.east)
                            textbutton " [[ TO [east_room.name] ]] ":
                                action [SetVariable("current_room", room_data.east), SetVariable("current_target", None)]
                        else:
                            null width 120

            # --- RIGHT COLUMN (Metadata & Actions) ---
            vbox:
                xsize 440
                spacing 20

                # 3. SUBJECT WINDOW (Metadata)
                fixed:
                    xsize 440 ysize 500
                    add OS_Window(440, 500)
                    frame:
                        background None
                        padding (15, 15)
                        vbox:
                            spacing 10
                            frame:
                                background None
                                xfill True ysize 320
                                if current_target:
                                    add current_target.img align (0.5, 0.5)
                                    textbutton " [[ X ]] " action SetVariable("current_target", None) align (1.0, 0.0)
                                else:
                                    text "SCANNING..." align (0.5, 0.5) color "#333" italic True

                            if current_target:
                                text "[current_target.name]" color "#e15a00" size 30 bold True
                                text "[current_target.description]" size 20 color "#ccc"

                # 4. INTERACTION COMMANDS
                fixed:
                    xsize 440 ysize 340
                    add OS_Window(440, 340)
                    frame:
                        background None
                        padding (25, 25)
                        vbox:
                            spacing 10

                            if interaction_mode == "main":
                                label "COMMAND_LIST" text_color "#e15a00" text_size 20

                                # --- TALK (Updated for new Animals) ---
                                textbutton "[[ TALK ]]":
                                    action If(current_target and current_target.can_talk, 
                                             If((current_target.name if current_target else "") in ["PATCH_CAT", "STRAY_DOG", "CROW", "SPIDER"] and not can_speak_with_animals,
                                                Notify("ERR: LINGUISTIC_INCOMPATIBILITY. ANIMAL_TRANSLATOR_REQUIRED."),
                                                [Hide("world_interface"), Jump(current_target.label if current_target else "nowhere")]), 
                                             None)
                                    text_idle_color ("#e15a00" if (
                                        current_target and 
                                        current_target.can_talk and 
                                        ((current_target.name if current_target else "") not in ["PATCH_CAT", "STRAY_DOG", "CROW", "SPIDER"] or can_speak_with_animals)
                                    ) else "#222")

                                # --- OPEN ---
                                textbutton "[[ OPEN ]]":
                                    action If(current_target and current_target.can_open and not current_target.locked, 
                                             Jump(current_target.label if current_target else "nowhere"), 
                                             None)
                                    text_idle_color ("#e15a00" if (current_target and current_target.can_open and not current_target.locked) else "#222")

                                # --- TAKE ---
                                textbutton "[[ TAKE ]]":
                                    action If(current_target and current_target.can_take, Function(pick_up_item, current_target, inventory, current_room), None)
                                    text_idle_color ("#f90" if (current_target and current_target.can_take) else "#222")

                                # --- CAST ---
                                textbutton "[[ CAST_PROGRAM ]]":
                                    # Only allow if object is castable and not the roots after they're deleted!
                                    action If(current_target and current_target.can_cast and (current_target.name != "MAGICAL_ROOTS" or not getattr(store, "cabin_roots_deleted", False)),
                                              Show("spellbook_screen")
                                              , None)
                                    # Highlight orange unless roots are gone and we're hovering them
                                    text_idle_color (
                                        "#e15a00" if (
                                            current_target and
                                            current_target.can_cast and
                                            (current_target.name != "MAGICAL_ROOTS" or not getattr(store, "cabin_roots_deleted", False))
                                        ) else "#222"
                                    )

                                # --- USE ITEM ---
                                textbutton "[[ USE_ITEM ]]":
                                    action If(current_target, SetVariable("interaction_mode", "use_item"), None)
                                    text_idle_color ("#e15a00" if current_target else "#222")

                            else:
                                # --- USE ITEM SUB-MENU ---
                                vbox:
                                    spacing 10
                                    hbox:
                                        label "SELECT_MODULE" text_color "#e15a00" text_size 20
                                        textbutton "[[ X ]]" action SetVariable("interaction_mode", "main") xalign 1.0 text_idle_color "#f00"

                                    vpgrid:
                                        cols 1
                                        mousewheel True
                                        spacing 5
                                        xfill True

                                        if not inventory.items:
                                            text "NO_MODULES_FOUND" color "#444" size 18 italic True
                                        else:
                                            for item in inventory.items:
                                                textbutton "> [item.name]":
                                                    action [
                                                        Function(use_item_on_target, current_target, item), 
                                                        SetVariable("interaction_mode", "main")
                                                    ]
                                                    text_idle_color "#ccc"
                                                    text_hover_color "#e15a00"