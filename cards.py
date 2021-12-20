from globals import *

class tribes:
    AVIAN = 0
    CANINE = 1
    HOOVED = 2
    INSECT = 3
    REPTILE = 4
    ALL = 5
    SQUIRREL = 6
    TERRAIN = 7

class card(object):

    def __init__(self, name, damage, health, blood, bones, tribe=None, image=None, sigils=None):
        if name is None:
            self.name = self.__class__.__name__
        else:
            self.name = name
        self.damage = damage
        self.touchofdeath = False
        self.health = health
        self.blood = blood
        self.bones = bones
        self.tribe = tribe
        self.image = image
        self.submerged = False
        self.airborne = False
        self.burrower = False
        self.mightyleap = False
        self.manylives = False
        self.sacrifices = 0
        self.repulsive = False

        if sigils == None: self.sigils = []
        else: self.sigils = sigils

        self.pos = None
        self.side = None
        self.to_attack = None

    def has_sigil(self, sigil):
        if isinstance(sigil, str):
            for s in self.sigils:
                if s.name == sigil:
                    return True

        else:
            for s in self.sigils:
                if isinstance(s, sigil):
                    return True

        return False

    def remove_from_deck(self):
        if self not in Player[self.player].deck.cards:
            return
        card_index = Player[self.player].deck.cards.index(self)
        Player[self.player].deck.cards.pop(card_index)

    def remove_from_pack(self):
        if self not in Player[self.player].deck.cards:
            return
        card_index = Player[self.player].pack.cards.index(self)
        Player[self.player].pack.cards.pop(card_index)

    def grow(self):
        self.name = "elder "+ self.name
        self.health += 2
        self.damage += 1

    def attack(self):
        if self.damage <= 0:
            return
        
        self.to_attack = [(self.enemy, self.pos)]
        for sigil in self.sigils:
            sigil.attack()

        for side, pos in self.to_attack:
            if Board.board[side][pos] is not None:
                Board.board[side][pos].block(self)
                if self.touchofdeath:
                    Board.board[side][pos].death(self)

            else:
                Player[side].block(self)

        self.to_attack = None

    def block(self, attacker, damage=None):
        if damage is None:
            self.health -= attacker.damage
        else:
            self.health -= damage

        if self.health <= 0:
            self.death(attacker)

    def draw(self, side):
        if side == 0:
            self.player = 0
            self.enemy = 1
        if side == 1:
            self.player = 1
            self.enemy = 0

        Player[self.player].deck.add_card(self)
        self.remove_from_pack()

    def set_side(self, side):
        if side == 0:
            self.player = 0
            self.enemy = 1
        if side == 1:
            self.player = 1
            self.enemy = 0

    def place(self, pos):
        if len(Player[self.player].deck) == 0:
            print("no cards in deck")
            return

        if Board.board[self.player][pos] is not None:
            print("You can't place a card there")
            return

        self.pos = pos
        Board.board[self.player][pos] = self
        self.remove_from_deck()

    def death(self, attacker):
        attacker.kill(self)
        Board.board[self.player][self.pos] = None

    def kill(self, defender):
        print("{0} killed {1}".format(self.name, defender.name))


class Squirrel(card):
    def __init__(self, name="squirrel", damage=0, health=1, blood=0, bones=0, tribe=tribes.SQUIRREL, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)

    def draw(self, side):
        if side == 0:
            self.player = 0
            self.enemy = 1
        if side == 1:
            self.player = 1
            self.enemy = 0

        Player[self.player].deck.add_card(self)


class Stoat(card):
    def __init__(self, name=None, damage=1, health=2, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
 

class Amalgam(card):
    def __init__(self, name=None, damage=3, health=3, blood=2, bones=0, tribe=tribes.ALL, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Amoeba(card):
    def __init__(self, name=None, damage=1, health=2, blood=0, bones=2, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class MoleMan(card):
    def __init__(self, name=None, damage=0, health=6, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class PackRat(card):
    def __init__(self, name=None, damage=2, health=2, blood=2, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class TheDaus(card):
    def __init__(self, name=None, damage=2, health=2, blood=2, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Urayuli(card):
    def __init__(self, name=None, damage=7, health=7, blood=4, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Bat(card):
    def __init__(self, name=None, damage=2, health=1, blood=0, bones=4, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class TentacleBell(card):
    def __init__(self, name="...", damage=1, health=3, blood=2, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Cat(card):
    def __init__(self, name=None, damage=0, health=1, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class UndeadCat(card):
    def __init__(self, name=None, damage=3, health=6, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class FieldMice(card):
    def __init__(self, name=None, damage=2, health=2, blood=2, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class GreatWhite(card):
    def __init__(self, name=None, damage=4, health=2, blood=3, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Grizzly(card):
    def __init__(self, name=None, damage=4, health=6, blood=3, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class TentacleDeck(card):
    def __init__(self, name=None, damage=0, health=1, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Mole(card):
    def __init__(self, name=None, damage=0, health=4, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class TentacleMirror(card):
    def __init__(self, name=None, damage=0, health=3, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Opossum(card):
    def __init__(self, name=None, damage=1, health=1, blood=0, bones=2, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Porcupine(card):
    def __init__(self, name=None, damage=1, health=2, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class RatKing(card):
    def __init__(self, name=None, damage=2, health=1, blood=2, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class RiverOtter(card):
    def __init__(self, name=None, damage=1, health=1, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Skunk(card):
    def __init__(self, name=None, damage=0, health=3, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Warren(card):
    def __init__(self, name=None, damage=0, health=2, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class RabbitPelt(card):
    def __init__(self, name=None, damage=0, health=1, blood=0, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class WolfPelt(card):
    def __init__(self, name=None, damage=0, health=2, blood=0, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class GoldenPelt(card):
    def __init__(self, name=None, damage=0, health=3, blood=0, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class BaitBucket(card):
    def __init__(self, name=None, damage=0, health=1, blood=0, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Chime(card):
    def __init__(self, owner, name=None, damage=0, health=1, blood=0, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        self.owner = owner

    def block(self, attacker):
        super().block(attacker)
        attacker.block(self.owner)
        

class GreaterSmoke(card):
    def __init__(self, name=None, damage=1, health=3, blood=0, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class LeapingTrap(card):
    def __init__(self, name=None, damage=0, health=1, blood=0, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class PackMule(card):
    def __init__(self, name=None, damage=0, health=5, blood=0, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Rabbit(card):
    def __init__(self, name=None, damage=0, health=1, blood=0, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class StrangeFrog(card):
    def __init__(self, name=None, damage=1, health=2, blood=1, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class TheSmoke(card):
    def __init__(self, name=None, damage=0, health=1, blood=0, bones=0, tribe=None, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)


###########################################################
######################     AVIAN     ######################
###########################################################


class Kingfisher(card):
    def __init__(self, name=None, damage=1, health=1, blood=1, bones=0, tribe=tribes.AVIAN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Magpie(card):
    def __init__(self, name=None, damage=1, health=1, blood=2, bones=0, tribe=tribes.AVIAN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class RavenEgg(card):
    def __init__(self, name=None, damage=0, health=2, blood=1, bones=0, tribe=tribes.AVIAN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Raven(card):
    def __init__(self, name=None, damage=2, health=3, blood=2, bones=0, tribe=tribes.AVIAN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Sparrow(card):
    def __init__(self, name=None, damage=1, health=2, blood=1, bones=0, tribe=tribes.AVIAN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class TurkeyVulture(card):
    def __init__(self, name=None, damage=3, health=3, blood=0, bones=8, tribe=tribes.AVIAN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)


###########################################################
######################     CANINE     #####################
###########################################################


class Alpha(card):
    def __init__(self, name=None, damage=1, health=2, blood=0, bones=5, tribe=tribes.CANINE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Bloodhound(card):
    def __init__(self, name=None, damage=2, health=3, blood=2, bones=0, tribe=tribes.CANINE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class CagedWolf(card):
    def __init__(self, name=None, damage=0, health=6, blood=2, bones=0, tribe=tribes.CANINE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Coyote(card):
    def __init__(self, name=None, damage=2, health=1, blood=0, bones=4, tribe=tribes.CANINE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class WolfCub(card):
    def __init__(self, name=None, damage=1, health=1, blood=1, bones=0, tribe=tribes.CANINE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Wolf(card):
    def __init__(self, name=None, damage=3, health=2, blood=2, bones=0, tribe=tribes.CANINE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

###########################################################
######################     HOOVED     #####################
###########################################################


class Child13(card):
    def __init__(self, name=None, damage=0, health=1, blood=1, bones=0, tribe=tribes.HOOVED, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class BlackGoat(card):
    def __init__(self, name=None, damage=0, health=1, blood=1, bones=0, tribe=tribes.HOOVED, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class ElkFawn(card):
    def __init__(self, name=None, damage=1, health=1, blood=1, bones=0, tribe=tribes.HOOVED, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Elk(card):
    def __init__(self, name=None, damage=2, health=4, blood=2, bones=0, tribe=tribes.HOOVED, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class MooseBuck(card):
    def __init__(self, name=None, damage=3, health=7, blood=3, bones=0, tribe=tribes.HOOVED, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Pronghorn(card):
    def __init__(self, name=None, damage=1, health=3, blood=2, bones=0, tribe=tribes.HOOVED, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)


###########################################################
######################     INSECT     #####################
###########################################################


class MantisGod(card):
    def __init__(self, name=None, damage=1, health=1, blood=1, bones=0, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class StrangeLarva(card):
    def __init__(self, name=None, damage=0, health=3, blood=1, bones=0, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class StrangePupa(card):
    def __init__(self, name=None, damage=0, health=3, blood=1, bones=0, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class MothMan(card):
    def __init__(self, name=None, damage=7, health=3, blood=1, bones=0, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class AntQueen(card):
    def __init__(self, name=None, damage=1, health=3, blood=2, bones=0, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Bee(card):
    def __init__(self, name=None, damage=1, health=1, blood=0, bones=0, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Beehive(card):
    def __init__(self, name=None, damage=0, health=2, blood=1, bones=0, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Cockroach(card):
    def __init__(self, name=None, damage=1, health=1, blood=0, bones=4, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class CorpseMaggots(card):
    def __init__(self, name=None, damage=1, health=2, blood=0, bones=5, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Mantis(card):
    def __init__(self, name=None, damage=1, health=1, blood=1, bones=0, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class RingWorm(card):
    def __init__(self, name=None, damage=0, health=1, blood=1, bones=0, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class WorkerAnt(card):
    def __init__(self, name=None, damage=1, health=2, blood=1, bones=0, tribe=tribes.INSECT, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)


###########################################################
#####################     REPTILE     #####################
###########################################################


class Geck(card):
    def __init__(self, name=None, damage=1, health=1, blood=0, bones=0, tribe=tribes.REPTILE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Ouroboros(card):
    def __init__(self, name=None, damage=1, health=1, blood=2, bones=0, tribe=tribes.REPTILE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Adder(card):
    def __init__(self, name=None, damage=1, health=1, blood=2, bones=0, tribe=tribes.REPTILE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class BullFrog(card):
    def __init__(self, name=None, damage=1, health=2, blood=1, bones=0, tribe=tribes.REPTILE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Rattler(card):
    def __init__(self, name=None, damage=3, health=1, blood=0, bones=6, tribe=tribes.REPTILE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class RiverSnapper(card):
    def __init__(self, name=None, damage=1, health=3, blood=2, bones=0, tribe=tribes.REPTILE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Skink(card):
    def __init__(self, name=None, damage=1, health=2, blood=1, bones=0, tribe=tribes.REPTILE, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)


###########################################################
#####################     TERRAIN     #####################
###########################################################


class Boulder(card):
    def __init__(self, name=None, damage=0, health=5, blood=0, bones=0, tribe=tribes.TERRAIN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Stump(card):
    def __init__(self, name=None, damage=0, health=3, blood=0, bones=0, tribe=tribes.TERRAIN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class Dam(card):
    def __init__(self, name=None, damage=0, health=2, blood=0, bones=0, tribe=tribes.TERRAIN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class GrandFir(card):
    def __init__(self, name=None, damage=0, health=3, blood=0, bones=0, tribe=tribes.TERRAIN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class SnowyFir(card):
    def __init__(self, name=None, damage=0, health=4, blood=0, bones=0, tribe=tribes.TERRAIN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)
        

class GoldNugget(card):
    def __init__(self, name=None, damage=0, health=2, blood=0, bones=0, tribe=tribes.TERRAIN, image=None, sigils=None):
        super().__init__(name, damage, health, blood, bones, tribe, image, sigils)