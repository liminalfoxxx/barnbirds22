# --- MINIGAMES MODULE ---

init python:
    import random

    def get_card_name(value):
        """Converts numerical value to card name."""
        names = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        return names.get(value, str(value))

    # --- SLOT MACHINE HELPERS ---
    def slot_symbols():
        return ["UFO", "CRESCENT MOON", "STAR", "SATURN", "BLACK HOLE"]

    def slot_spin():
        return [renpy.random.choice(slot_symbols()) for _ in range(3)]

    def slot_payout(reels, bet):
        s1, s2, s3 = reels
        unique = set(reels)
        if len(unique) == 1:
            sym = s1
            if sym == "SATURN":
                return bet * 10
            elif sym == "STAR":
                return bet * 6
            elif sym == "CRESCENT MOON":
                return bet * 5
            elif sym == "UFO":
                return bet * 4
            else:
                return 0
        if s1 == s2 or s1 == s3 or s2 == s3:
            pair = s1 if (s1 == s2 or s1 == s3) else s2
            if pair != "BLACK HOLE":
                return bet * 2
        if "BLACK HOLE" in unique:
            return 0
        return 0

label minigame_toucan:
    tou "I draw a card, you draw a card. Highest value wins the pot."

    label .bet_menu:
        $ current_balance = inventory.money
        tou "Current Units: [current_balance]. How much are you staking?"

        menu:
            "Bet 5 Units" if inventory.has_money(5):
                $ bet_amount = 5
                jump .play_game
            "Bet 10 Units" if inventory.has_money(10):
                $ bet_amount = 10
                jump .play_game
            "Bet 20 Units" if inventory.has_money(20):
                $ bet_amount = 20
                jump .play_game
            "I'm done playing.":
                tou "Until next time, then. The house always waits."
                jump overworld_loop

    label .play_game:
        $ inventory.money -= bet_amount
        tou "Staking [bet_amount] Units."
        tou "Let's see what the cards have to say."

        $ house_card = renpy.random.randint(2, 14)
        $ player_card = renpy.random.randint(2, 14)
        $ house_label = get_card_name(house_card)
        $ player_label = get_card_name(player_card)

        tou "House draws: {b}[house_label]{/b}."
        tou "Your draw is..."
        pause 0.5
        "{b}[player_label]{/b}!"

        if player_card > house_card:
            $ winnings = bet_amount * 2
            $ inventory.earn(winnings)
            tou "Clean win! The money's all yours, kid."
            sys "Received [winnings] Units."
        elif player_card < house_card:
            tou "Sorry, that's not a winning hand."
            sys "Bet Lost."
        else:
            $ inventory.earn(bet_amount)
            tou "That's a draw! Here's your money back."
            sys "Bet Refunded."

        tou "Go again?"
        jump .bet_menu

# --- SLOT MACHINE MINI GAME ---

label minigame_slots:
    sys "LUCKY_ORBIT.EXE online."
    sys "Insert Units to spin. Payouts vary by match."

    label .bet_menu:
        $ current_balance = inventory.money
        sys "Current Units: [current_balance]. Select bet size."

        menu:
            "Bet 5 Units" if inventory.has_money(5):
                $ slot_bet = 5
                jump .spin
            "Bet 10 Units" if inventory.has_money(10):
                $ slot_bet = 10
                jump .spin
            "Bet 20 Units" if inventory.has_money(20):
                $ slot_bet = 20
                jump .spin
            "[[ X ]] Leave":
                sys "Exiting SLOT_MACHINE.EXE."
                jump overworld_loop

    label .spin:
        $ inventory.money -= slot_bet
        sys "Bet accepted: [slot_bet] Units."
        sys "Spinning..."
        pause 0.4

        $ reels = slot_spin()
        $ r1, r2, r3 = reels
        "[r1] | [r2] | [r3]"

        $ winnings = slot_payout(reels, slot_bet)
        if winnings > 0:
            $ inventory.earn(winnings)
            sys "WINNER! Payout: [winnings] Units."
        else:
            sys "No payout on this spin."

        menu:
            "Spin again (same bet)" if inventory.has_money(slot_bet):
                jump .spin
            "Change bet":
                jump .bet_menu
            "[[ X ]] Leave":
                sys "Exiting LUCKY_ORBIT.EXE."
                jump overworld_loop

# --- JUKEBOX PLACEHOLDER ---
label jukebox_menu:
    sys "Accessing Local Audio Directory..."
    menu:
        "Play: Sector_01_Ambient.mp3":
            sys "Frequency set to 44.1kHz. (Audio placeholder triggered)"
        "Play: Diner_Jazz_Glitch.wav":
            sys "Frequency set to 48.0kHz. (Audio placeholder triggered)"
        "Stop Playback":
            sys "Output muted."
        "Exit Jukebox":
            jump overworld_loop
    jump jukebox_menu