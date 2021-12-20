class player(object):
    def __init__(self, id):
        self.id = id
        self.damage = 0
        self.pack = pack()
        self.deck = deck()
        self.squirrels = []
        self.bones = 0

    def __new__(cls, id):
        if id in Player:
            return Player[id]

    def turn_start(self):
        for card in Board.board[self.id]:
            for sigil in card.sigils:
                sigil.turn_start()

    def block(self, attacker):

        for card in Board.board[self.id]:
            if not card.burrower:
                continue

            if attacker.airborne and not card.mightyleap:
                continue

            Board.move_card(card.player, card.pos, card.enemy, attacker.pos)
            card.block(attacker)
            return

        self.damage += attacker.damage

    def pack_draw(self):
        if len(self.pack) <= 0:
            print("card pack empty")
            return
        self.pack.cards[0].draw(self.id)

    def squirrel_draw(self):
        if self.squirrels <= 0:
            print("no more squirrels")
            return
        self.squirrels[0].draw(self.id)

    def is_starving(self):
        if len(self.deck.cards) == 0 and len(self.squirrels) == 0:
            return True

        return False

class deck(object):
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        prefab = [
        "______________ ",
        "|{name}| ",
        "|          {blood} | ",
        "|            | ",
        "|            | ",
        "|            | ",
        "|            | ",
        "| {damage}        {health} | ",
        "|____________| "
        ]
        out = ""
        ROW_LEN = 6
        for row in range(1+len(self.cards)//ROW_LEN):
            for line in prefab[:]:
                for col in range(ROW_LEN):
                    if row*ROW_LEN+col >= len(self.cards):
                        break
                    name = self.cards[row+col].name
                    if len(name)<12: name += ' '*(12-len(name))
                    if len(name)>12: name = name[:12]
                    out += line.format(name=name, damage=self.cards[row+col].damage, health=self.cards[row+col].health, blood=self.cards[row+col].blood)
                if row*ROW_LEN < len(self.cards):
                    out += '\n'

        return out

    def __repr__(self):
        return self.__str__()

class pack(deck):
    def __init__(self):
        super().__init__()

class board(object):
    def __init__(self, width=4):
        self.width = width
        self.board = [
            [None, None, None, None],
            [None, None, None, None]
        ]

    def move_card(self, curr_side, curr_pos, end_side, end_pos):
        if self.board[end_side][end_pos] is not None:
            raise Warning("attemting to move card onto another card")

        self.board[end_side][end_pos] = self.board[curr_side][curr_pos]
        self.board[curr_side][curr_pos] = None

    def place_card(self, card, side, pos):
        if self.board[side][pos] is not None:
            raise Warning("Attempted to place card on top of another card")

        self.board[side][pos] = card

    def __str__(self):
        prefab = [
        "______________ ",
        "|{name}| ",
        "|          {blood} | ",
        "|            | ",
        "|            | ",
        "|            | ",
        "|            | ",
        "| {damage}        {health} | ",
        "|____________| "
        ]
        out = ""
        for row in range(2):
            for line in prefab[:]:
                for col in range(self.width):

                    if self.board[row][col] is None:
                        out += line.format(name="EMPTY       ", damage = ' ', health=' ', blood=' ')
                        continue

                    name = self.board[row][col].name
                    if len(name)<12: name += ' '*(12-len(name))
                    if len(name)>12: name = name[:12]
                    out += line.format(name=name, damage=self.board[row][col].damage, health=self.board[row][col].health, blood=self.board[row][col].blood)
                out += '\n'

        return out

    def __repr__(self):
        self.__str__()

Board = board()

Player = {
    0 : player(0),
    1 : player(1)
}
