# -*- coding: utf-8 -*-

# ==== IMPORTS SECTION ========================================================
import random

# ==== CONSTANTS DEFINITIONS ==================================================
GREEN_CARD = "GREEN"
RED_CARD = "RED"
BLUE_CARD = "BLUE"
ORANGE_CARD = "ORANGE"
GREY_CARD = "GREY"
DARK_GREEN_CARD = "DARK_GREEN"
BLACK_CARD = "BLACK"

CARDS_MERGE_NUMBER = 3

ACTION_DRAW = "DRAW"
ACTION_MERGE = "MERGE"
ACTION_IDRAW = "IDRAW"
ACTION_IMERGE = "IMERGE"
ACTION_MERGE_NOT_POSSIBLE = "MERGE NOT POSSIBLE"

# ==== CLASS DEFINITION =======================================================


class Player():
    def __init__(self, name):
        self.name = name
        self.cards = {
            GREEN_CARD: 0,
            RED_CARD: 0,
            BLUE_CARD: 0,
            ORANGE_CARD: 0,
            GREY_CARD: 0,
            DARK_GREEN_CARD: 0,
            BLUE_CARD: 0,
            BLACK_CARD: 0
        }

        self.merge_results = {
            GREEN_CARD: DARK_GREEN_CARD,
            BLUE_CARD: GREY_CARD,
            RED_CARD: ORANGE_CARD
        }

        self.last_action = None
        self.draw_temptative = None
        self.merge_temptative = None

    # _________________________________________________________________________
    def draw(self, card):
        self.last_action = ACTION_DRAW
        self.draw_temptative = card

    # _________________________________________________________________________
    def merge(self, card):
        if self.cards[card] >= CARDS_MERGE_NUMBER:
            self.last_action = ACTION_MERGE
            self.merge_temptative = card
        else:
            self.last_action = ACTION_MERGE_NOT_POSSIBLE

    # _________________________________________________________________________
    def idraw(self):
        self.last_action = ACTION_IDRAW

    # _________________________________________________________________________
    def imerge(self):
        self.last_action = ACTION_IMERGE

    # _________________________________________________________________________
    def random_action(self):
        # TODO: check action is not repeated
        actions = [self.draw, self.merge, self.idraw, self.imerge]
        return random.choice(actions)

    # _________________________________________________________________________
    def choose_card_to_draw(self):
        cards = [RED_CARD, BLUE_CARD, GREEN_CARD]
        return random.choice(cards)

    # _________________________________________________________________________
    def try_action(self):
        # NOTE: This should be virtual pure
        action = self.random_action()
        if action == self.draw:
            card = self.choose_card_to_draw()
            action(card)

        elif action == self.merge:
            card = self.choose_card_to_draw()
            action(card)
        else:
            action()

        print(self.name, "Chosed option:", self.last_action)

    # _________________________________________________________________________
    def draw_sucess(self):
        print(self.name, "Sucessed on draw")
        self.cards[self.draw_temptative] += 1

    # _________________________________________________________________________
    def draw_fail(self):
        print(self.name, "Failed on draw")
        pass

    # _________________________________________________________________________
    def merge_sucess(self):
        if self.cards[self.merge_temptative] >= 3:
            got_card = self.merge_results[self.merge_temptative]
            self.cards[got_card] += 1
            print(self.name, "Merged Sucess")
        else:
            print(self.name, "Tried to merge but do not have enought cards")

    # _________________________________________________________________________
    def merge_fail(self):
        print(self.name, "Failed Merge")
        self.cards[self.merge_temptative] -= 1

    # _________________________________________________________________________
    def idraw_sucess(self, cards):
        print(self.name, "Sucessed on Idraw")
        for card in cards:
            self.cards[card] += 1

    # _________________________________________________________________________
    def idraw_fail(self):
        print(self.name, "Failed on Idraw")
        pass

    # _________________________________________________________________________
    def imerge_sucess(self, options):
        print(self.name, "Sucessed on Imerge")
        for opt in options:
            self.cards[opt] += 1
        pass

    # _________________________________________________________________________
    def imerge_fail(self):
        print(self.name, "Failed on Imerge")
        pass

    # _________________________________________________________________________
    def merge_not_possible(self):
        print(self.name, "Tried an impossible merge")

    # _________________________________________________________________________
    def summary(self):
        print(
            self.name,
            "have {}red, "
            "{}blue, "
            "{}green, "
            "{}orange, "
            "{}dgreen, "
            "{}grey, "
            "{}black".format(
                self.cards[RED_CARD],
                self.cards[BLUE_CARD],
                self.cards[GREEN_CARD],
                self.cards[ORANGE_CARD],
                self.cards[DARK_GREEN_CARD],
                self.cards[GREY_CARD],
                self.cards[BLACK_CARD]
            )
        )
