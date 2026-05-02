# --- DATA MODELS ---

# Global state for the map
default selected_location = None
default can_travel = True
default load_progress = 0.0

init python:
    class Location:
        def __init__(self, name, description, target_room, locked=False):
            self.name = name
            self.description = description
            self.target_room = target_room 
            self.locked = locked    # New: controls fast travel lock/unlock

# Definitions pointing to your new overworld_logic rooms
default blushwood = Location("Blushwood Court", "A dense thicket of bioluminescent flora. Sector 01.", "blushwood_1")
default sundapple = Location("Sundapple Square", "Central hub with high solar exposure. Sector 02.", "sundapple_1")
default parlor = Location("Parlor District", "Residential sector of the upper echelon. Sector 03.", "parlor_1")
default avm_facility = Location("AVM Facility", "A sealed data core. FINAL AREA. Accessible only after route 'lock-in'.", "avm_facility_room", locked=True)

# --- SCREENS ---

screen map_screen():
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

            # --- LEFT COLUMN: THE SATELLITE MAP ---
            fixed:
                xsize 1200
                yfill True

                add OS_Window(1200, 980) 

                # Check for map image, otherwise use a placeholder
                if renpy.loadable("images/ui/world_map.png"):
                    add "images/ui/world_map.png"
                else:
                    add Solid("#111")

                # Blushwood Court Node
                vbox:
                    xpos 555 ypos 600
                    spacing 10
                    imagebutton:
                        idle Solid("#e15a00", xsize=20, ysize=20) 
                        hover Solid("#ffffff", xsize=20, ysize=20)
                        selected_idle Solid("#ffffff", xsize=20, ysize=20) 
                        action SetVariable("selected_location", blushwood)
                        xalign 0.5
                    text "BLUSHWOOD_COURT":
                        size 28 color "#ffffff" bold True xalign 0.5
                        outlines [ (2, "#000", 0, 0) ]

                # Sundapple Square Node
                vbox:
                    xpos 800 ypos 350
                    spacing 10
                    imagebutton:
                        idle Solid("#e15a00", xsize=20, ysize=20)
                        hover Solid("#ffffff", xsize=20, ysize=20)
                        selected_idle Solid("#ffffff", xsize=20, ysize=20)
                        action SetVariable("selected_location", sundapple)
                        xalign 0.5
                    text "SUNDAPPLE_SQUARE":
                        size 28 color "#ffffff" bold True xalign 0.5
                        outlines [ (2, "#000", 0, 0) ]

                # Parlor District Node
                vbox:
                    xpos 188 ypos 300
                    spacing 10
                    imagebutton:
                        idle Solid("#e15a00", xsize=20, ysize=20)
                        hover Solid("#ffffff", xsize=20, ysize=20)
                        selected_idle Solid("#ffffff", xsize=20, ysize=20)
                        action SetVariable("selected_location", parlor)
                        xalign 0.5
                    text "PARLOR_DISTRICT":
                        size 28 color "#ffffff" bold True xalign 0.5
                        outlines [ (2, "#000", 0, 0) ]

                # --- AVM Facility Node (FINAL AREA; only enabled after lock-in) ---
                vbox:
                    xpos 340 ypos 150
                    spacing 10
                    imagebutton:
                        idle Solid("#aa4444", xsize=24, ysize=24)
                        hover Solid("#ffffff", xsize=24, ysize=24)
                        selected_idle Solid("#ffffff", xsize=24, ysize=24)
                        action If(avm_facility_accessible, SetVariable("selected_location", avm_facility), Notify("ACCESS DENIED: No clearance detected."))
                        xalign 0.5
                    text "AVM_FACILITY":
                        size 28 color ("#ff0000" if avm_facility_accessible else "#555") bold True xalign 0.5
                        outlines [ (2, "#000", 0, 0) ]

            # --- RIGHT COLUMN: LOCATION METADATA ---
            vbox:
                xfill True
                spacing 20

                hbox:
                    xfill True
                    label "NAVIGATION_NODE.EXE" text_size 40 text_color "#e15a00"
                    textbutton " [[ X ]] ":
                        action [Hide("map_screen"), SetVariable("selected_location", None)]
                        xalign 1.0
                        text_idle_color "#e15a00"
                        text_hover_color "#ff8000"

                fixed:
                    xfill True
                    yfill True
                    add OS_Window(600, 900) 

                    frame:
                        background None
                        padding (30, 30)
                        xfill True yfill True

                        if selected_location:
                            vbox:
                                spacing 20
                                label "LOCATION_DATA" text_color "#e15a00"

                                fixed:
                                    xsize 400 ysize 250
                                    add OS_Window(400, 250)
                                    # Optional: add "images/ui/previews/[selected_location.target_room].png"

                                text "[selected_location.name]" size 34 color "#ff8000"
                                text "[selected_location.description]" size 22 color "#ccc"

                                null height 40

                                if can_travel and (selected_location != avm_facility or avm_facility_accessible):
                                    textbutton "[[ INITIATE_TRAVEL ]]":
                                        action [Hide("map_screen"), Jump("initiate_fast_travel")]
                                        text_size 36
                                        text_idle_color "#e15a00"
                                        text_hover_color "#fff"
                                        xalign 0.5
                                elif selected_location == avm_facility and not avm_facility_accessible:
                                    vbox:
                                        xalign 0.5
                                        text "[[ ACCESS DENIED ]]" color "#e15a00" size 36 xalign 0.5
                                        text "This node is encrypted. Progress a route to unlock." size 18 color "#666" xalign 0.5
                                else:
                                    vbox:
                                        xalign 0.5
                                        text "[[ SIGNAL_LOCKED ]]" color "#e15a00" size 36 xalign 0.5
                                        text "Active process must conclude before jump." size 18 color "#666" xalign 0.5
                        else:
                            text "SELECT_COORDINATES..." align (0.5, 0.4) color "#444" size 34

# --- JUMP ENGINE ---

label initiate_fast_travel:
    $ load_progress = 0.0
    call screen loading_screen("finish_fast_travel")
    return

label finish_fast_travel:
    $ current_room = selected_location.target_room
    $ current_target = None
    $ selected_location = None
    $ can_travel = True
    with fade
    jump overworld_loop

# --- LOADING SCREEN ---

screen loading_screen(target_label):
    modal True
    zorder 200
    add Solid("#0d0d0d")

    if load_progress < 1.0:
        timer 0.05 repeat True action SetVariable("load_progress", load_progress + 0.03)

    vbox:
        align (0.5, 0.5)
        spacing 20
        xsize 600

        text "INITIATING_SECTOR_JUMP..." size 18 color "#e15a00"

        fixed:
            ysize 30
            add OS_Window(600, 30)
            bar value load_progress range 1.0:
                xsize 590 ysize 20
                align (0.5, 0.5)
                left_bar Solid("#e15a00")
                right_bar Solid("#00000000")

        if load_progress < 1.0:
            $ display_percent = int(load_progress * 100)
            text "[display_percent] %" size 24 color "#e15a00" xalign 1.0

            if load_progress < 0.4:
                text "CACHING_ENVIRONMENT_GEOMETRY..." size 14 color "#444"
            else:
                text "DECRYPTING_LOCAL_ENTITIES..." size 14 color "#444"
        else:
            textbutton "[[CLICK_TO_PROCEED]]":
                action [Hide("loading_screen"), Jump(target_label)]
                text_color "#e15a00"
                text_size 24
                xalign 0.5
                at transform:
                    alpha 1.0
                    linear 0.5 alpha 0.4
                    linear 0.5 alpha 1.0
                    repeat

            text "SYSTEM_SYNCHRONIZED_100%" size 14 color "#e15a00" xalign 0.5