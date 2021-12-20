from cards import *
from sigils import *
from globals import Board, Player
import random

Player[0].pack.cards = [
    Stoat(),
    Stoat(),
    Stoat(),
    Stoat(),
    Stoat(),
    Stoat()
]

Player[1].pack.cards = [
    Stoat(),
    Stoat(),
    Stoat(),
    Stoat(),
    Stoat()
]

for p in range(1):
    for i in range(20):
        Player[p].squirrels.append(Squirrel())

Squirrel().draw(0)
for c in Player[0].pack.cards[:4]:
    c.draw(0)

Squirrel().draw(1)
for c in Player[1].pack.cards[:4]:
    c.draw(1)

turn = 0

print(Player[0].deck)
while abs(Player[0].damage - Player[1].damage) < 5:
    turn += 1
    plr = (turn-1) % 2
    action = ""
    
    print("\n\nNEW TURN -----------------------------\n")
    print("PLAYER{0}'s turn".format(plr))
    if not Player[plr].is_starving():
        if input("draw from deck or a squirrel(d/s)? You have {0} cards and {1} squirrels left: ".format(len(Player[plr].pack.cards), len(Player[plr].squirrels))) == "d":
            Player[plr].pack_draw()
        else:
            Player[plr].squirrel_draw()
    else:
        print("Starvation began to set in")

    while action != "endturn":
        print("actions:\n   deck\n   place\n   endturn\n   board")
        action = input("action: ")

        if action == "place":
            while True:
                print(Player[plr].deck)
                card_index = int(input("index: "))
                if card_index == "cancel":
                    break
                if 0 <= card_index < len(Player[plr].deck.cards):
                    break
                print("not valid")

            if card_index == 'cancel':
                continue
            
            while True:
                print(Board)
                place_index = int(input("index('cancel'): "))
                if card_index == "cancel":
                    break
                if 0 <= place_index < 4:
                    break
                print("outside of board")

            if place_index == 'cancel':
                continue

            Player[plr].deck.cards[card_index].place(place_index)
            continue

        if action == "deck":
            print(Player[plr].deck)
            continue

        if action == "board":
            print(Board)
            continue

    for c in Board.board[plr]:
        if c is None:
            continue
        c.attack()

    for c in Board.board[1 if plr == 0 else 0]:
        if c is None:
            continue
        c.attack()

winner = 0 if Player[0].damage > Player[1].damage else 1

print()
print("PLAYER {0} WON!".format(winner))
