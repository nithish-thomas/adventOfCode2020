import re
from collections import defaultdict
from typing import List, Any, Tuple, Dict, Set


def get_input() -> List[List[int]]:
    f = open("input2.txt", "r")
    inp = f.read().strip().split('\n\n')
    inp_ = [player.strip().split('\n') for player in inp]
    return [[int(card) for card in player_deck_inp[1:]] for player_deck_inp in inp_]


def combat(player1, player2, game):
    print('game '+ str(game))
    player1_stages = set()
    while len(player1) != 0 and len(player2) != 0:
        cur_player_1_stage = tuple(player1), tuple(player2)

        if cur_player_1_stage in player1_stages:
            return True, player1, player2

        player1_stages.add(cur_player_1_stage)

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if len(player1) >= card1 and len(player2) >= card2:
            game += 1
            sub_game_res = combat(player1[:card1], player2[:card2], game)
            player_1_won = sub_game_res[0]
        else:
            player_1_won = card1 > card2
        if player_1_won:
            player1 = player1 + [card1, card2]
        else:
            player2 = player2 + [card2, card1]
    return len(player1) != 0, player1, player2


def main():
    decks = get_input()
    print(decks)
    player1 = decks[0]
    player2 = decks[1]

    player_1_won, player1, player2 = combat(player1, player2, 1)

    if player_1_won:
        winning = player1
    else:
        winning = player2

    res = 0
    for i, card in enumerate(reversed(winning)):
        res += (i + 1) * card

    print(res)
    print (res == 33441)


if __name__ == "__main__":
    main()
