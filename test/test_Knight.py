import pytest
from unittest.mock import patch
import unittest
from Piece import Knight, Player


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


if __name__ == '__main__':
    unittest.main()

