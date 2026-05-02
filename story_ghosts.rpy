


label ghost_dialogue:
    "SPECTRE_DEALER" "Signal received... data packets reconstructed... thank you, Operator."
    
    menu:
        "Analyze signal.":
            "SPECTRE_DEALER" "My memory banks are corrupted, but my core logic remains intact."
        "End transmission.":
            pass

    # This returns them to the overworld view
    show screen world_interface
    return