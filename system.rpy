

# This redirects the Escape key (and right-click) to your custom screen
define config.game_menu_action = ShowMenu("system_screen")

default system_subtab = "CONFIG" # Can be "CONFIG" or "HISTORY"





#    SCREENS
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣀⡀⠀⠀⠀⢀⣠⣴⣾⡛⣛⠿⢭⡉⢉⣹⣿⡛⠶⣤⡀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢀⠈⡉⠳⢦⠾⣯⣞⣉⠀⢙⣡⠤⣄⣨⠷⣄⣀⣸⠋⠙⣻⣷⣤⣤⠶⠟⠛⢹⣧⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠐⢎⢷⡱⡄⠀⠀⠀⠀⠉⠛⢧⣄⡤⠶⢧⠤⣄⣩⠽⠟⠛⠉⠉⠉⣡⣶⠀⠀⣸⡇⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠈⠉⠉⠈⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠛⠟⠁⢠⡿⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠆⠀⠀⠀⣠⡖⡖⠶⢤⡀⠀⠀⠀⠹⠋⠀⠀⣠⠒⣟⠛⠲⢄⠀⠀⠀⣶⡟⠁⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⣼⣿⣧⣿⠀⠀⢹⡄⠀⠀⠀⠀⠀⣼⣿⣷⣿⠀⠀⠀⢳⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⠀⢻⣿⣿⠏⠀⠀⢸⠇⠀⠀⠀⠀⠀⢿⣿⣿⡟⠀⠀⢀⡾⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠛⠥⣤⡤⠔⠋⢀⣤⠶⠶⠶⠦⣌⠛⠿⠤⠤⠖⠋⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⣴⣾⣿⣿⣶⡄⠀⠀⢻⣆⠀⣠⡞⠁⠀⢀⣴⣾⣿⣿⡶⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠈⠛⠛⠛⠋⠁⠀⠀⠀⠹⣶⠋⠀⠀⠀⠀⠉⠙⠋⠉⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⡶⠶⠶⠶⠶⣤⣀⡀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⠈⣻⡶⠶⠤⠤⠶⠾⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠛⣿⡙⢦⡀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠙⢦⡀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⢰⡏⠀⠰⡄⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⣰⣄⣀⣀⡤⠸⣇⠀⠈⢳⡄⠀⠀⠀
# ⠀⠀⠀⠀⢠⡾⠁⠀⠀⠀⢀⣿⠀⠀⠀⠙⠲⠦⠶⠖⠋⠙⠦⠤⣤⠤⠖⠋⠈⠙⠓⠒⠋⠁⠈⠉⠁⠀⠀⣿⡄⠀⠀⠹⡄⠀⠀
# ⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⢸⣧⣀⣠⣤⣿⡄⠀
# ⠀⠀⣠⣿⠀⠀⣰⡆⠀⢀⣿⠁⠀⠀⠀⣧⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⣰⡄⠀⠀⠀⣰⠧⠤⠤⠞⠁⠀⢸⡇⣧⠘⡇⢹⣿⡄
# ⠀⢠⣟⡞⢹⠏⡟⣸⢛⡏⣿⠀⠀⠀⠀⠈⠓⠦⠤⠴⠊⠉⠲⠦⠤⠖⠚⠁⠈⠙⠛⠉⠁⠀⠀⠀⠀⠀⠀⢸⡇⠸⡄⢻⠈⣿⣷
# ⢀⣿⡿⢀⡏⣼⢁⡏⣼⢡⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣧⠀⣇⠸⡆⢹⣿
# ⣸⣿⠇⡼⢰⡇⣼⢠⡇⣸⢻⡇⠀⠀⠀⠀⢦⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⢠⡀⠀⠀⠀⣀⠜⠀⠀⠀⠀⢀⣿⠹⡆⢹⡄⣿⣾⡿
# ⣿⣹⢠⠇⣾⢧⡇⢸⣇⡏⣼⣿⡀⠀⠀⠀⠈⠓⠶⠤⠖⠋⠙⠶⠤⠤⠖⠊⠉⠛⠛⠋⠁⠀⠀⠀⠀⠀⣼⠇⠳⢷⠾⠙⠋⠀⠀
# ⣿⡏⣼⡼⣿⣸⢠⣿⣿⡿⠃⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀
# ⠙⠳⠋⠀⠙⠿⠋⠀⠉⠀⠀⠀⠈⠻⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⡓⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠧⣷⡀⠀⡀⠀⢀⣤⡶⠞⠋⠙⣧⣄⣤⣀⣤⣶⣻⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠿⣿⡿⠿⠿⣿⣷⡀⠀⠀⣼⣟⣺⣟⣻⣻⣿⣺⣯⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣋⣛⣿⡿⠿⣿⣯⣭⣿⡇⠀⢸⣿⣶⠿⣿⣷⣾⠿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣬⠟⣿⣿⣽⠏⢻⣿⡿⠁⠀⠈⠛⠁⠀⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣋⣁⠀⢙⣛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀





screen system_screen():
    tag menu
    modal True
    add Solid("#0d0d0d")

    # THIS CAPTURES THE ESCAPE KEY TO CLOSE THE MENU
    key "game_menu" action Return()

    frame:
        background None
        padding (50, 50)
        xfill True
        yfill True

        hbox:
            spacing 40
            
            # --- LEFT COLUMN: KERNEL COMMANDS ---
            vbox:
                xsize 400
                spacing 15
                label "KERNEL_COMMANDS" text_color "#e15a00"
                
                # SUB-TAB SWITCHERS
                textbutton "> HARDWARE_CONFIG":
                    action SetVariable("system_subtab", "CONFIG")
                    text_idle_color ("#fff" if system_subtab == "CONFIG" else "#e15a00")
                    text_hover_color "#ff8000"

                textbutton "> MESSAGE_HISTORY":
                    action SetVariable("system_subtab", "HISTORY")
                    text_idle_color ("#fff" if system_subtab == "HISTORY" else "#e15a00")
                    text_hover_color "#ff8000"

                null height 50
                
                # SYSTEM ACTIONS
                textbutton "> SAVE_STATE":
                    action ShowMenu("save")
                    text_idle_color "#e15a00"
                    text_hover_color "#ff8000"
                
                textbutton "> LOAD_STATE":
                    action ShowMenu("load")
                    text_idle_color "#e15a00"
                    text_hover_color "#ff8000"

                textbutton "> MAIN_MENU":
                    action MainMenu()
                    text_idle_color "#e15a00"
                    text_hover_color "#ff8000"

                null height 50

                textbutton "> TERMINATE_PROCESS (EXIT)":
                    action Quit(confirm=True)
                    text_idle_color "#f00"
                    text_hover_color "#ff8000"

            # --- RIGHT COLUMN: THE CONTENT FRAME ---
            frame:
                background Solid("#e15a00")
                padding (2, 2)
                xfill True
                yfill True
                frame:
                    background Solid("#0d0d0d")
                    padding (40, 40)
                    xfill True
                    yfill True

                    # --- VIEW 1: CONFIGURATION ---
                    if system_subtab == "CONFIG":
                        vbox:
                            spacing 30
                            label "HARDWARE_CONFIGURATION" text_color "#e15a00" text_size 40

                            # VOLUME
                            vbox:
                                spacing 10
                                text "AUDIO_OUTPUT_GAIN" color "#ccc" size 20
                                hbox:
                                    spacing 20
                                    text "MIN" size 14 color "#666" yalign 0.5
                                    bar value MixerValue("master"): 
                                        xsize 500
                                        left_bar Solid("#e15a00")
                                        right_bar Solid("#333")
                                        thumb None 
                                    text "MAX" size 14 color "#666" yalign 0.5

                            # TEXT SPEED
                            vbox:
                                spacing 10
                                text "DATA_TRANSFER_RATE (TEXT SPEED)" color "#ccc" size 20
                                bar value Preference("text speed"):
                                    xsize 500
                                    left_bar Solid("#e15a00")
                                    right_bar Solid("#333")
                                    thumb None

                            # DISPLAY MODE
                            vbox:
                                spacing 10
                                text "DISPLAY_MODE" color "#ccc" size 20
                                hbox:
                                    spacing 30
                                    textbutton " [[ WINDOWED ]] ":
                                        action Preference("display", "window")
                                        text_idle_color "#e15a00"
                                        text_selected_color "#ffffff"
                                    textbutton " [[ FULLSCREEN ]] ":
                                        action Preference("display", "fullscreen")
                                        text_idle_color "#e15a00"
                                        text_selected_color "#ffffff"

                    # --- VIEW 2: MESSAGE HISTORY ---
                    elif system_subtab == "HISTORY":
                        vbox:
                            spacing 20
                            label "LOCAL_DATA_CACHE (HISTORY)" text_color "#e15a00" text_size 40
                            
                            frame:
                                background Solid("#111")
                                padding (10, 10)
                                xfill True
                                yfill True
                                
                                viewport:
                                    scrollbars "vertical"
                                    mousewheel True
                                    yinitial 1.0 # Focus on the most recent text
                                    
                                    vbox:
                                        spacing 15
                                        xfill True
                                        for h in _history_list:
                                            vbox:
                                                if h.who:
                                                    text "[h.who]" color "#e15a00" size 18 font "gui/font/Monospace.ttf" # Use your terminal font
                                                text "[h.what]" color "#ccc" size 22
                                                null height 5
                                                add Solid("#333", ysize=1, xfill=True)
                                        
                                        if not _history_list:
                                            text "NO_HISTORY_LOGGED" color "#444" align (0.5, 0.4)

    # UNIVERSAL CLOSE BUTTON
    textbutton " [[ X ]] CLOSE_TERMINAL ":
        action Return()
        align (1.0, 0.0)
        offset (-50, 50)
        text_idle_color "#e15a00"
        text_hover_color "#fff"