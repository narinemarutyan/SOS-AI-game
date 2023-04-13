from typing import Iterator

from game_board import GameBoard
from players import AbstractPlayer


class Game:
    def __init__(
        self, player_1: AbstractPlayer, player_2: AbstractPlayer, game_board: GameBoard
    ):
        self._player_1 = player_1
        self._player_2 = player_2
        self._game_board = game_board
        self._sos_count = 0

    def _next_player_generator(self) -> Iterator[AbstractPlayer]:
        while True:
            yield self._player_1
            yield self._player_2

    def _print_game_result(self):
        print(self._player_1)
        print(self._player_2)
        if self._player_1.get_score() != self._player_2.get_score():
            winner = (
                self._player_1
                if self._player_1.get_score() > self._player_2.get_score()
                else self._player_2
            )
            print(f"good game {winner} won the game")
        else:
            print("bad game, it's a draw")

    def run(self):
        self._game_board.print_game_board()
        players_iterator = self._next_player_generator()
        current_player = next(players_iterator)

        while self._game_board.has_empty_locations():
            move = current_player.make_move(self._game_board)
            self._game_board.play_move(move)
            current_sos_count = self._game_board.get_sos_count()
            score = current_sos_count - self._sos_count

            if score:
                self._sos_count = current_sos_count
                current_player.update_score(score)
                print(f"{current_player} got {score} point(s)\n")
            else:
                current_player = next(players_iterator)

            self._game_board.print_game_board()

        self._print_game_result()
