# Minimal AI pop-up screen (single-instance, always on top)
init offset = -3

default ai_pop_title = "SYSTEM"
default ai_pop_text = "Signal online."
default ai_pop_image = None
default ai_pop_has_choice = False
default ai_pop_choice_caption = "OK"
default ai_pop_choice_action = NullAction()

screen ai_popup():
    zorder 1000
    modal True
    layer "screens"

    frame:
        background Frame(Solid("#dddddd"), 6, 6)  # mac-like later; theme switchable
        padding (24, 24)
        xalign 0.5
        yalign 0.15
        xsize 780

        vbox:
            spacing 14

            hbox:
                xfill True
                text "[ai_pop_title]":
                    size 28
                    color "#000"
                textbutton " [X] ":
                    action Hide("ai_popup")
                    xalign 1.0
                    text_idle_color "#000"
                    text_hover_color "#f00"

            if ai_pop_image:
                add ai_pop_image xalign 0.5

            text "[ai_pop_text]":
                size 24
                color "#000"

            if ai_pop_has_choice:
                textbutton "[ai_pop_choice_caption]":
                    action [ai_pop_choice_action, Hide("ai_popup")]
                    xalign 0.5
                    text_idle_color "#000"
                    text_hover_color "#333"