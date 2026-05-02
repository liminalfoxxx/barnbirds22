


#IMAGE BUTTON GALLERY
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

init:
    image dove_idle:
        "images/ows/dove1.png"
        pause 1.0
        "images/ows/dove2.png"
        pause 1.0
        repeat

    image dove_hover:
        "images/ows/dove_hover_1.png"
        pause 1.0
        "images/ows/dove_hover_2.png"
        pause 1.0
        repeat

screen dove_overworld:
    imagebutton:
            xpos 555
            ypos 420
            idle "dove_idle"
            hover "dove_hover"
            action Jump("dove_orchard_1")