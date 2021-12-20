from globals import Board, player
from cards import *
from copy import deepcopy

class activation:
    ATTACK = 0
    BLOCK = 1
    DEATH = 2
    PLACE_SELF = 3
    PLACE_ENEMY = 4
    DRAW = 5
    START = 6
    END = 7
    KILL = 8
    SACRIFICE = 9
    FACING_CARD = 10

class sigil(object):
    def __init__(self, card, act=1):
        self.name = self.__class__.__name__
        self.act = act
        self.card = card

    def atack(self):
        pass

    def death(self):
        pass

    def place_self(self):
        pass

    def place_enemy(self):
        pass
    
    def draw(self):
        pass
    
    def turn_start(self):
        pass
    
    def turn_end(self):
        pass
    
    def kill(self):
        pass
    
    def sacrifice(self):
        pass
    
    def block(self):
        pass

class RabbitHole(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def place_self(self):
        Rabbit().draw(self.card.player)

class BeesWithin(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def block(self):
        Bee().draw(self.card.player)


class Sprinter(sigil):
    def __init__(self, card):
        super().__init__(card, 1)
    #NOTE:FINISH THIS


class TouchOfDeath(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def draw(self):
        self.card.touchofdeath = True


class Fledgling(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def turn_start(self):
        self.card.grow()


class DamBuilder(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def place_self(self):
        if self.card.pos > 0 and Board.board[self.card.player][self.card.pos-1] is None:
            dam = Dam()
            dam.set_side(self.card.player)
            Board.place_card(dam, self.card.player, self.card.pos-1)

        if self.card.pos < 3 and Board.board[self.card.player][self.card.pos+1] is None:
            dam = Dam()
            dam.set_side(self.card.player)
            Board.place_card(dam, self.card.player, self.card.pos+1)

class Hoarder(sigil):
    def __init__(self, card):
        super().__init__(card, 1)
    #NOTE: FINISH THIS


class Burrower(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def draw(self):
        self.card.burrower = True

class Fecundity(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def place_self(self):
        deepcopy(self).draw(self.card.player)

class LooseTail(sigil):
    def __init__(self, card):
        super().__init__(card, 1)
    #NOTE:FINISH THIS


class CorpseEater(sigil):
    def __init__(self, card):
        super().__init__(card, 1)


class BoneKing(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def death(self):
        player(self.card.player).bones += 0

class Waterborne(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def turn_end(self):
        self.card.submerged = True

class Unkillable(sigil):
    def __init__(self, card):
        super().__init__(card, 1)
    #NOTE:rework pack

class SharpQuills(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def block(self, attacker):
        attacker.block(self.card, 1)

class Hefty(sigil):
    def __init__(self, card):
        super().__init__(card, 1)
    #NOTE:FINISH THIS


class AntSpawner(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def place_self(self):
        WorkerAnt().draw(self.card.player)

class Guardian(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def place_enemy(self, enemy):
        if Board.board[self.card.player][enemy.pos] is not None:
            return

        Board.move_card(self.card.player, self.card.pos, self.card.player, enemy.pos)

class Airborne(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def draw(self):
        self.card.airborne = True


class ManyLives(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def draw(self):
        self.manylives = True

class Repulsive(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def draw(self):
        self.repulsive = True

class WorthySacrifice(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def draw(self):
        self.worthysacrifice = True


class MightyLeap(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def draw(self):
        self.mightyleap = True


class BifurcatedStrike(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def attack(self):
        if self.card.pos > 0:
            if (self.card.player, self.card.pos-1) not in self.card.to_attack:
                self.card.to_attack.append((self.card.player, self.card.pos-1))

        if self.card.pos < 3:
            if (self.card.player, self.card.pos+1) not in self.card.to_attack:
                self.card.to_attack.append((self.card.player, self.card.pos-1))


class TrifurcatedStrike(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def attack(self):
        self.card.to_attack = [(self.card.player, self.card.pos)]

        if self.card.pos > 0:
            self.card.to_attack.append((self.card.player, self.card.pos-1))

        if self.card.pos < 3:
            self.card.to_attack.append((self.card.player, self.card.pos+1))


class FrozenAway(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    #NOTE: FINISH LATER


class TrinketBearer(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    #NOTE: FINISH LATER


class SteelTrap(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def death(self, attacker):
        attacker.death(self)
        WolfPelt().draw(attacker.player)

class Amorphous(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    #NOTE:FINISH THIS


class TidalLock(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    #NOTE:FINISH THIS

class Leader(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    #NOTE:FINish THIS

class Bellist(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    def place_self(self):
        if self.card.pos > 0 and Board.board[self.card.player][self.card.pos-1] is None:
            chime = Chime(self.card)
            chime.set_side(self.card.player)
            Board.place_card(chime, self.card.player, self.card.pos-1)

        if self.card.pos < 3 and Board.board[self.card.player][self.card.pos+1] is None:
            chime = Chime(self.card)
            chime.set_side(self.card.player)
            Board.place_card(chime, self.card.player, self.card.pos+1)

class Stinky(sigil):
    def __init__(self, card):
        super().__init__(card, 1)

    #NOTE:FINISHTHIS