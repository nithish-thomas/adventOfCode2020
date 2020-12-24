import re
from collections import defaultdict
from typing import List, Any, Tuple, Dict, Set



def get_input() -> List[List[str]]:
    f = open("input2.txt", "r")
    inp = f.read().strip().split('\n\n')
    inp_ = [player.strip().split('\n') for player in inp]
    return [[int(card) for card in player_deck_inp[1:]] for player_deck_inp in inp_]


def main():
    decks = get_input()
    print(decks)
    player1 = decks[0]
    player2 = decks[1]

    while len(player1) != 0 and len(player2) != 0:
        player1_card = player1[0]
        player2_card = player2[0]

        if player1_card > player2_card:
            player1 = player1[1:] + [player1_card] + [player2_card]
            player2 = player2[1:]
        else:
            player1 = player1[1:]
            player2 = player2[1:] + [player2_card] + [player1_card]


    if len(player1) != 0:
        winning = player1
    else:
        winning = player2

    res = 0
    for i, card in enumerate(reversed(winning)):
        res += (i+1)*card

    print(res)


if __name__ == "__main__":
    main()
