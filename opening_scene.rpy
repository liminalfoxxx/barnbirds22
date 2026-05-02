# opening_scene.rpy

# Remove these if set elsewhere to avoid duplication/crashes.
$ dove_route_stage = 0
$ raven_route_stage = 0
$ swan_route_stage = 0

# Initial Inventory & Spells
init python:
    inventory = Inventory(money=10)
    #inventory.learn_spell(ghost_speak)
    # inventory.learn_spell(animal_speak)
    # inventory.learn_spell(hack_prog)
    # inventory.learn_spell(heal_blight_prog)

#default journal_entries = [JournalEntry("ROOT", "System Online", "2026-01-15", "OS stabilized. Cleric credentials verified. Blight investigation beginning in Sector 01.")]
default prologue_link_ready = False
default prologue_modules_ready = False
default prologue_modules_button_enabled = False
default prologue_select_idx = None
default prologue_connect_ready = False
default prologue_loading_progress = 0.0

label opening_cutscene:
    $ prologue_loading_progress = 0.0
    $ prologue_link_ready = False
    $ prologue_modules_ready = False
    $ prologue_modules_button_enabled = False
    $ prologue_select_idx = None
    $ prologue_connect_ready = False

    call screen prologue_loading_screen
    while not prologue_link_ready:
        $ renpy.pause(0.1)
    $ prologue_link_ready = False

    call screen prologue_video_screen
    while not prologue_modules_ready:
        $ renpy.pause(0.1)
    $ prologue_modules_ready = False
    $ prologue_modules_button_enabled = False

    call screen prologue_player_select_screen
    while not prologue_connect_ready:
        $ renpy.pause(0.1)
    $ prologue_connect_ready = False

    $ current_room = "prologue_room"
    $ current_target = None
    show screen world_interface

    while current_room == "prologue_room":
        $ renpy.pause(0.2)

    $ prologue_room_accessible = False
    return

screen prologue_loading_screen():
    modal True
    zorder 101
    add Solid("#0d0d0d")
    vbox:
        align (0.5, 0.37)
        spacing 44

        frame:
            background Solid("#e15a00")
            xsize 420
            ysize 120
            align (0.5, 0.5)
            text "LOGO" color "#0d0d0d" size 62 xalign 0.5 yalign 0.5

        use prologue_loading_bar

        if prologue_loading_progress >= 1.0:
            textbutton "[[INITIATE LINK]]" style "prologue_initial_button" action [SetVariable("prologue_link_ready", True), Hide("prologue_loading_screen")] xalign 0.5

    if prologue_loading_progress < 1.0:
        timer 0.04 repeat True action SetVariable("prologue_loading_progress", prologue_loading_progress+0.025)

style prologue_initial_button is default
style prologue_initial_button:
    color "#e15a00"
    background None
    size 38
    xalign 0.5

screen prologue_loading_bar():
    vbox:
        spacing 10
        align (0.5, 0.5)
        text "Establishing Uplink..." color "#e15a00" size 26 xalign 0.5
        bar value prologue_loading_progress range 1.0 xsize 600 ysize 16 left_bar Solid("#e15a00") right_bar Solid("#332")
        text "[int(prologue_loading_progress*100)] %" size 22 color "#e15a00" xalign 0.5

screen prologue_video_screen():
    modal True
    zorder 101
    add Solid("#0d0d0d")
    vbox:
        align (0.5, 0.5)
        spacing 34
        frame:
            background Solid("#222")
            xsize 940
            ysize 400
            xalign 0.5
            yalign 0.5
            add Movie(size=(640,360), play="images/vids/open_1.webm", loop=False) align (0.5,0.5)
            text "Opening Video" color "#fff" size 18 xalign 0.5 yalign 1.0
    textbutton "[VIEW MODULES]" style "prologue_initial_button" action [SetVariable("prologue_modules_ready", True), Hide("prologue_video_screen")] xalign 0.5

screen prologue_player_select_screen():
    modal True
    zorder 101
    add Solid("#0d0d0d")

    vbox:
        align (0.5, 0.5)
        spacing 30
        frame:
            background Frame(Solid("#e15a00"), 6, 6)
            xsize 700
            ysize 650
            vbox:
                spacing 0
                hbox:
                    xsize 670
                    spacing 6
                    text "PLAYER SELECT" color "#e15a00" size 34 bold True xalign 0.0
                    null width 20
                    textbutton "[[CONNECT]]" style "prologue_connect_button" sensitive prologue_select_idx == 6 action If(prologue_select_idx == 6, [SetVariable("prologue_connect_ready", True), Hide("prologue_player_select_screen")]) xalign 1.0
                null height 30

                vbox:
                    spacing 10
                    for i in range(13):
                        if i == 6:
                            button:
                                background (Solid("#e15a00") if prologue_select_idx == 6 else None)
                                xfill True
                                ysize 44
                                action SetVariable("prologue_select_idx", 6)
                                text "[BARN_OWL]" color ("#0d0d0d" if prologue_select_idx==6 else "#e15a00") size 26 xalign 0.5
                        else:
                            button:
                                background None
                                xfill True
                                ysize 44
                                action None
                                text "[OFFLINE]" color "#444" size 24 xalign 0.5

style prologue_connect_button is default
style prologue_connect_button:
    color "#e15a00"
    background None
    size 28
    insensitive_color "#664400"