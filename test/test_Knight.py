import pytest
from unittest.mock import patch
import unittest
from Piece import Knight, Player, Piece


class TestKnight(unittest.TestCase):

    @patch('chess_engine.game_state')
    def test_get_valid_peaceful_moves_on_corner_right_board(self, MockGameState):
        game_state_mock = MockGameState()
        game_state_mock.get_piece.side_effect = lambda r, c: Player.EMPTY if (r, c) in [(5, 6),
                                                                                        (6, 5)] else Player.PIECES
        knight = Knight("N", 7, 7, Player.PLAYER_1)
        expected_moves = [
            (5, 6), (6, 5)
        ]
        actual_moves = knight.get_valid_peaceful_moves(game_state_mock)
        self.assertCountEqual(actual_moves, expected_moves)

    @patch('chess_engine.game_state')
    def test_get_valid_peaceful_moves_on_middle_board(self, MockGameState):
        game_state_mock = MockGameState()
        game_state_mock.get_piece.return_value = Player.EMPTY
        knight = Knight("N", 4, 4, Player.PLAYER_1)
        expected_moves = [
            (2, 3), (2, 5), (3, 2), (3, 6),
            (5, 2), (5, 6), (6, 3), (6, 5)
        ]
        actual_moves = knight.get_valid_peaceful_moves(game_state_mock)
        self.assertCountEqual(actual_moves, expected_moves)

    @patch('chess_engine.game_state')
    def test_get_valid_peaceful_moves_on_corner_left_board(self, MockGameState):
        game_state_mock = MockGameState()
        game_state_mock.get_piece.side_effect = lambda r, c: Player.EMPTY if (r, c) in [(2, 1),
                                                                                        (1, 2)] else Player.PIECES
        knight = Knight("N", 0, 0, Player.PLAYER_1)
        expected_moves = [
            (2, 1), (1, 2)
        ]
        actual_moves = knight.get_valid_peaceful_moves(game_state_mock)
        self.assertCountEqual(actual_moves, expected_moves)

    @patch('chess_engine.game_state')
    def test_get_valid_piece_takes_nowhere_to_move(self, MockGameState):
        def get_piece_side_effect(row, col):
            return Piece('p', row, col, Player.PLAYER_1)

        game_state_mock = MockGameState()
        game_state_mock.get_piece.side_effect = get_piece_side_effect

        knight = Knight("N", 3, 3, Player.PLAYER_1)
        expected_moves = []
        actual_moves = knight.get_valid_piece_takes(game_state_mock)
        self.assertCountEqual(actual_moves, expected_moves)

    @patch('chess_engine.game_state')
    def test_get_valid_piece_takes_one_place_to_move(self, MockGameState):
        def get_piece_side_effect(row, col):
            if row == 1 and col == 2:
                return Piece('p', 1, 2, Player.PLAYER_2)
            else:
                return Piece('p', row, col, Player.PLAYER_1)

        game_state_mock = MockGameState()
        game_state_mock.get_piece.side_effect = get_piece_side_effect

        knight = Knight("N", 3, 3, Player.PLAYER_1)
        expected_moves = [
            (1, 2)
        ]
        actual_moves = knight.get_valid_piece_takes(game_state_mock)
        self.assertCountEqual(actual_moves, expected_moves)

    @patch('chess_engine.game_state')
    def test_get_valid_piece_takes_all_place_to_move(self, MockGameState):
        def get_piece_side_effect(row, col):
            return Piece('p', row, col, Player.PLAYER_2)

        game_state_mock = MockGameState()
        game_state_mock.get_piece.side_effect = get_piece_side_effect

        knight = Knight("N", 3, 3, Player.PLAYER_1)
        expected_moves = [
            (1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 4), (5, 2)
        ]
        actual_moves = knight.get_valid_piece_takes(game_state_mock)
        self.assertCountEqual(actual_moves, expected_moves)


if __name__ == '__main__':
    unittest.main()

