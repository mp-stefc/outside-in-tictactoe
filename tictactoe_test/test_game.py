import unittest
from unittest.mock import MagicMock, call, Mock


from tictactoe.Board import TicTacToeBoard
from tictactoe.GameLoop import IConsoleInput, IConsoleOutput, GameLoop


class PromptFake(IConsoleInput):
    def __init__(self):
        self.inputs = []

    def set_inputs(self, inputs):
        self.inputs = inputs

    def get_next_input(self):
        return self.inputs.pop(0) if len(self.inputs) > 0 else ""


BOARD_STRING = "WHATEVER THE BOARD RETURNS"


class ConsoleMock(IConsoleOutput):
    def __init__(self, expected_logged_string):
        self.stored_output = ""
        self.expected_logged_string = expected_logged_string
        self.call_count = 0

    def display(self, string):
        self.call_count += 1
        assert(string == self.expected_logged_string)

    def get_call_count(self):
        return self.call_count


class TicTacToeAcceptanceTestCase(unittest.TestCase):
    def setUp(self):
        self.console_input = PromptFake()
        self.console_output = ConsoleMock(BOARD_STRING)
        self.board = TicTacToeBoard()
        self.board.to_string = MagicMock(return_value=BOARD_STRING)
        self.board.set_step = Mock()

        self.ttt = GameLoop(self.console_input, self.console_output, self.board)

    def test_TicTacToeGame_noInput_triggersNoMovesOnBoard(self):
        self.console_input.set_inputs([])

        self.ttt.start()

        self.board.set_step.assert_has_calls([])

    def test_TicTacToeGame_twoMoves_triggersTwoMovesOnBoard(self):
        self.console_input.set_inputs(["A0", "B1"])

        self.ttt.start()

        self.board.set_step.assert_has_calls([call("A0"), call("B1")])

    def test_TicTacToeGame_noInput_emptyBoardIsPrintedOnce(self):
        self.console_input.set_inputs([])

        self.ttt.start()

        self.assertEquals(self.console_output.get_call_count(), 1)

    def test_TicTacToeGame_n_moves_outputPrinted_n_plus_one_times(self):
        self.console_input.set_inputs(["A0", "B1"])

        self.ttt.start()

        self.assertEquals(self.console_output.get_call_count(), 3)



if __name__ == '__main__':
    unittest.main()
