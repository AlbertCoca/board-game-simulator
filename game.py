# -*- coding: utf-8 -*-

# ==== IMPORTS SECTION ========================================================
import player

# ==== CONSTANTS DEFINITIONS ==================================================

# ==== CLASS DEFINITION =======================================================


class Game():
    def __init__(self, players):
        self.players = players
        self.reset()

    # _________________________________________________________________________
    def reset(self):
        self.action_players = {
            player.ACTION_DRAW: [],
            player.ACTION_IDRAW: [],
            player.ACTION_MERGE: [],
            player.ACTION_IMERGE: [],
            player.ACTION_MERGE_NOT_POSSIBLE: []
        }

    # _________________________________________________________________________
    def play(self):
        for p in self.players:
            p.try_action()
            self.action_players[p.last_action].append(p)

        if len(self.action_players[player.ACTION_DRAW]) > 0:

            # draw failed, idraw sucess
            if(len(self.action_players[player.ACTION_IDRAW]) > 0):
                drawed_cards = [
                    p.draw_temptative
                    for p in self.action_players[player.ACTION_DRAW]
                ]
                # idraw sucess action
                for p in self.action_players[player.ACTION_IDRAW]:
                    p.idraw_sucess(drawed_cards)

                # draw failed action
                for p in self.action_players[player.ACTION_DRAW]:
                    p.draw_fail()
            # draw sucess
            else:
                for p in self.action_players[player.ACTION_DRAW]:
                    p.draw_sucess()
        # idraw failed
        else:
            for p in self.action_players[player.ACTION_IDRAW]:
                p.idraw_fail()

        if len(self.action_players[player.ACTION_MERGE]) > 0:
            # merge failed, imerge sucess
            if(len(self.action_players[player.ACTION_IMERGE]) > 0):
                merged_cards = [
                    p.merge_temptative
                    for p in self.action_players[player.ACTION_MERGE]
                ]
                # imerge sucess action
                for p in self.action_players[player.ACTION_IMERGE]:
                    p.imerge_sucess(merged_cards)

                # merge failed action
                for p in self.action_players[player.ACTION_MERGE]:
                    p.merge_fail()
            # merge sucess
            else:
                for p in self.action_players[player.ACTION_MERGE]:
                    p.merge_sucess()
        # idraw failed
        else:
            for p in self.action_players[player.ACTION_IMERGE]:
                p.imerge_fail()

        for p in self.action_players[player.ACTION_MERGE_NOT_POSSIBLE]:
            p.merge_not_possible()

        for p in self.players:
            p.summary()


if __name__ == "__main__":
    player1 = player.Player("Oscar")
    player2 = player.Player("Edu")
    player3 = player.Player("Albert")
    g = Game([player1, player2, player3])
    while(True):
        g.play()
        g.reset()
        input()
