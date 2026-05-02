# Example portrait definitions to drive SideImage changes per line.
# These match your characters.rpy image tags ("dove", "raven", etc.).

# DOVE portraits
image dove neutral = "images/portraits/dove_neutral.png"
image dove happy = "images/portraits/dove_happy.png"
image dove concerned = "images/portraits/dove_concerned.png"

# RAVEN portraits
image raven neutral = "images/portraits/raven_neutral.png"
image raven smile = "images/portraits/raven_smile.png"
image raven serious = "images/portraits/raven_serious.png"

# SEAGULL portraits
image seagull neutral = "images/portraits/seagull_neutral.png"
image seagull tired = "images/portraits/seagull_tired.png"

# PTARMIGAN portraits
image ptarmigan neutral = "images/portraits/ptarmigan_neutral.png"
image ptarmigan relieved = "images/portraits/ptarmigan_relieved.png"

# Usage in script:
#   d happy "Thanks for the soda!"
#   r serious "The archives are a mess."
#   seagull tired "Gun's empty."
# Ren'Py's SideImage will swap to the matching portrait automatically.