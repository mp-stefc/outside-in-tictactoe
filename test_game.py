import unittest
from unittest.mock import MagicMock, call, Mock

from TicTacToeBoard import TicTacToeBoard
from TicTacToeGame import IConsoleOutput, TicTacToeGame


class PromptFake(object):
    def __init__(self):
        self.inputs = []

    def set_inputs(self, inputs):
        self.inputs = inputs

    def get_next_input(self):
        return self.inputs.pop(0) if len(self.inputs) > 0 else ""

BOARD_STRING = "BLA"
class ConsoleMock(IConsoleOutput):
    def __init__(self, expected_logged_string):
        self.stored_output = ""
        self.expected_logged_string = expected_logged_string
        self.call_count = 0

    def display(self, string):
        self.call_count += 1
        assert(string == self.expected_logged_string)

    def getCallCount(self):
        return self.call_count



class TicTacToeAcceptanceTestCase(unittest.TestCase):
    def setUp(self):
        self.console_input = PromptFake()
        self.console_output = ConsoleMock(BOARD_STRING)
        self.board = TicTacToeBoard()
        self.board.to_string = MagicMock(return_value=BOARD_STRING)
        self.board.set_step = Mock()

        self.ttt = TicTacToeGame(self.console_input, self.console_output, self.board)

    def test_TicTacToe_newGameStarted_printsBoard(self):
        self.console_input.set_inputs([])

        self.ttt.start()

        self.assertEquals(self.console_output.getCallCount(), 1)

    def test_TicTacToe_twoMoves_printsBoardWithXO(self):
        self.console_input.set_inputs(["A0", "B1"])

        self.ttt.start()

        self.assertEquals(self.console_output.getCallCount(), 3)
        self.board.set_step.assert_has_calls([call("A0"), call("B1")])



if __name__ == '__main__':
    unittest.main()
