# Chat-style dialogue UI: portrait (left), text (right), choices (right).
# Load before screens.rpy so "use chat_say" works.
init offset = -3

init python:
    def ChatWindow(w, h):
        try:
            return OS_Window(w, h)
        except Exception:
            return Frame(Solid("#ead17a"), 10, 10)  # simple bordered fallback

    _portrait_colors = {
        "Dove": "#e1c400",
        "Raven": "#4700d1",
        "Swan": "#ffffff",
        "Seagull": "#333366",
        "Scarlet Tanager": "#0fa",
        "Toucan": "#0fa",
        "Hummingbird": "#0fa",
        "Ptarmigan": "#0fa",
        "Secretary": "#0fa",
        "Falcon": "#0fa",
        "Shrike": "#0fa",
        "AUTOMATON GUIDE": "#0fa",
        "System": "#e15a00",
    }

default _current_who = None

# SAY: portrait left (taller), name bar + dialogue window right
screen chat_say(who, what):
    zorder 150

    on "show" action SetVariable("_current_who", who)

    hbox:
        spacing 80
        xalign 0.5
        yalign 0.60

        # LEFT: Taller portrait window
        frame:
            background ChatWindow(640, 680)
            xsize 640
            ysize 680
            if not renpy.variant("small"):
                if SideImage():
                    add SideImage() align (0.5, 0.5)
                elif who and who in _portrait_colors:
                    add Solid(_portrait_colors[who], xsize=200, ysize=400) align (0.5, 0.5)
                    text who size 24 color "#000" align (0.5, 0.9)

        # RIGHT: Name bar above the dialogue window
        vbox:
            spacing 12
            xsize 980

            # Name bar (dark)
            if who is not None:
                frame:
                    background ChatWindow(980, 56)
                    xsize 980
                    ysize 56
                    padding (12, 8)
                    text who id "who" style "chat_namebox_text"

            # Dialogue window (white background comes from Character.window_background)
            window:
                id "window"
                style "chat_window"
                xsize 980
                ysize 480

                # Inner transparent frame to provide real padding for the text.
                frame:
                    background None
                    left_padding 34
                    right_padding 28
                    top_padding 64     # bump down more; adjust to taste
                    bottom_padding 28

                    # Dialogue text (black)
                    text what id "what" style "chat_what"

# CHOICE: portrait left, larger choices panel right
screen chat_choice(items):
    zorder 150

    hbox:
        spacing 80
        xalign 0.5
        yalign 0.60

        frame:
            background ChatWindow(640, 680)
            xsize 640
            ysize 680
            if not renpy.variant("small"):
                if SideImage():
                    add SideImage() align (0.5, 0.5)
                elif _current_who and _current_who in _portrait_colors:
                    add Solid(_portrait_colors[_current_who], xsize=200, ysize=400) align (0.5, 0.5)
                    text _current_who size 24 color "#000" align (0.5, 0.9)

        frame:
            background ChatWindow(980, 620)   # taller to fit ~8 buttons
            padding (18, 18)
            xsize 980
            ysize 620

            vbox:
                spacing 14
                xfill True
                for i in items:
                    textbutton i.caption:
                        action i.action
                        style "chat_choice_button"

# Styles
style chat_window is default
style chat_namebox_text is default
style chat_what is default
style chat_choice_button is button
style chat_choice_button_text is button_text

# Name in the dark bar (accent color)
style chat_namebox_text:
    size 32
    color "#e15a00"
    bold True

# Dialogue text: black
style chat_what:
    size 26
    color "#000000"
    layout "subtitle"

# Keep window padding minimal; inner frame above controls text position.
style chat_window:
    left_padding 0
    right_padding 0
    top_padding 0
    bottom_padding 0

# Choices (larger font)
style chat_choice_button:
    xfill True
    padding (12, 10)
    background Frame(Solid("#1a1a1a"), 6, 6)
    hover_background Frame(Solid("#2a2a2a"), 6, 6)

style chat_choice_button_text:
    size 28
    color "#e15a00"
    hover_color "#ffffff"
