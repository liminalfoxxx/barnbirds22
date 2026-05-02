init -10 python:
    class Item:
        # Added use_func=None to the parameters
        def __init__(self, name, cost=0, description="No data found.", img=None, use_func=None, frequency_type=None):
            self.name = name
            self.cost = cost
            self.description = description
            self.img = img 
            self.amount = 1
            self.use_func = use_func # Stores the transformation logic
            self.frequency_type = frequency_type

    class Spell: 
        def __init__(self, name, recipe, description="", frequency_type=None):
            self.name = name
            self.recipe = recipe 
            self.description = description
            self.frequency_type = frequency_type

        def can_cast(self, inventory):
            for item_name, req_amount in self.recipe.items():
                if inventory.count(item_name) < req_amount:
                    return False
            return True

    class Inventory:
        def __init__(self, money=0):
            self.money = money
            self.items = []
            self.known_spells = []
            self.frequency = {"Primal": 0, "Seelie": 0, "Unseelie": 0, "Storm": 0, "Death": 0, "Blood": 0, "Void": 0}
            
        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                self.add_item(item)
                return True
            return False

        def earn(self, amount):
            self.money += amount
            
        def has_money(self, amount):
            return self.money >= amount

        def has_item(self, item_name):
            return any(i.name == item_name for i in self.items)
                
        def learn_spell(self, spell):
            if spell not in self.known_spells:
                self.known_spells.append(spell)

        def add_item(self, item_obj):
            for i in self.items:
                if i.name == item_obj.name:
                    i.amount += 1
                    return
            import copy
            new_item = copy.copy(item_obj)
            new_item.amount = 1
            self.items.append(new_item)

        def count(self, item_name):
            for i in self.items:
                if i.name == item_name:
                    return i.amount
            return 0
                
        def remove_by_name(self, name):
            for i in self.items:
                if i.name == name:
                    if i.amount > 1:
                        i.amount -= 1
                    else:
                        self.items.remove(i)
                    return True
            return False

        def execute_program(self, spell):
            if spell.can_cast(self):
                for item_name, req_amount in spell.recipe.items():
                    for _ in range(req_amount):
                        self.remove_by_name(item_name)
                return True 
            return False

        def gain_frequency(self, freq_type, amount=1):
            if freq_type and freq_type in self.frequency and freq_type != "Void":
                self.frequency[freq_type] = min(33, self.frequency[freq_type] + amount)

        def spend_frequency(self, freq_type):
            if freq_type and freq_type in self.frequency and freq_type != "Void":
                if self.frequency[freq_type] > 0:
                    self.frequency[freq_type] -= 1
                    return True
                return False
            return True  # If no freq_type required, don't block the cast

# --- SCREENS ---
default selected_item = None

init python:
    def use_frequency_item():
        freq_type = selected_item.frequency_type
        inventory.remove_by_name(selected_item.name)
        inventory.gain_frequency(freq_type)
        renpy.notify("ABSORBED: +1 " + freq_type.upper() + " FREQUENCY")
        store.selected_item = None

screen inventory_screen():
    modal True
    zorder 100
    add Solid("#0d0d0d") 

    frame:
        background None
        padding (50, 50)
        xfill True yfill True

        hbox:
            spacing 40
            xfill True yfill True

            # --- LEFT COLUMN (Metadata) ---
            vbox:
                xsize 450
                spacing 20

                frame:
                    background Solid("#e15a00")
                    padding (2, 2)
                    xfill True
                    frame: 
                        background Solid("#0d0d0d")
                        padding (20, 20)
                        xfill True
                        vbox:
                            label "DEVICE DRIVE: /root" text_color "#e15a00"
                            text "Memory: [inventory.money] Units" size 26 
                            text "Logs: [len(inventory.items)] Unique Entries" size 26

                frame:
                    background Solid("#e15a00")
                    padding (2, 2)
                    xfill True yfill True 
                    frame:
                        background Solid("#0d0d0d")
                        padding (25, 25)
                        xfill True yfill True 
                        
                        if selected_item:
                            vbox:
                                spacing 20
                                label "INSPECT_ITEM" text_color "#e15a00"
                                
                                if selected_item.img:
                                    add selected_item.img xalign 0.5
                                elif renpy.loadable("gui/items/" + selected_item.name + ".png"):
                                    add "gui/items/[selected_item.name].png" xalign 0.5
                                else:
                                    add Solid("#222", xsize=180, ysize=180) xalign 0.5
                                
                                text "[selected_item.name]" color "#ff8000" size 34
                                text "[selected_item.description]" color "#ccc" size 22

                                # --- NEW: DYNAMIC USE BUTTON ---
                                if selected_item.use_func:
                                    null height 20
                                    textbutton "[[ USE_MODULE ]]":
                                        action Function(selected_item.use_func)
                                        xalign 0.5
                                        text_size 30
                                        text_idle_color "#0f0"
                                        text_hover_color "#fff"
                                elif selected_item.frequency_type:
                                    null height 20
                                    textbutton "[[ USE_MODULE ]]":
                                        action Function(use_frequency_item)
                                        xalign 0.5
                                        text_size 30
                                        text_idle_color "#0f0"
                                        text_hover_color "#fff"
                        else:
                            vbox:
                                align (0.5, 0.4)
                                text "NO DATA FOUND" color "#444" size 34 kerning 2
                                text "Select an entry to begin scan..." color "#333" size 20 xalign 0.5

            # --- RIGHT COLUMN (Logs) ---
            vbox:
                xfill True
                spacing 15
                hbox:
                    xfill True
                    label "ITEMIZED_LOGS.EXE" text_size 45 text_color "#e15a00"
                    textbutton " [[ X ]] CLOSE ":
                        action [Hide("inventory_screen"), SetVariable("selected_item", None)]
                        xalign 1.0
                        text_idle_color "#e15a00"
                        text_hover_color "#f00" 
                        text_size 30

                frame:
                    background Solid("#e15a00")
                    padding (2, 2)
                    xfill True yfill True
                    frame:
                        background Solid("#0d0d0d")
                        padding (10, 10)
                        xfill True yfill True
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            vbox:
                                xfill True
                                spacing 4
                                if not inventory.items:
                                    text "> NO_DATA_FOUND" color "#444" size 30 xpos 20
                                else:
                                    for item in inventory.items:
                                        button:
                                            action SetVariable("selected_item", item)
                                            xfill True
                                            ysize 50
                                            background (Solid("#e15a00") if selected_item == item else None)
                                            text "> [item.name] (x[item.amount])":
                                                xpos 15 yalign 0.5 size 28
                                                color ("#0d0d0d" if selected_item == item else "#e15a00")