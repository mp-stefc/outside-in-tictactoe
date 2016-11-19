import unittest
from unittest.mock import MagicMock, call

from TicTacToeBoard import TicTacToeBoard
from TicTacToeGame import IConsoleOutput, TicTacToeGame

class ConsoleSpy(IConsoleOutput):
    def __init__(self):
        self.stored_output = ""

    def display(self, ttt_string):
        self.stored_output = ttt_string

    def getLoggedOuput(self):
        return self.stored_output


class PromptFake(object):
    def __init__(self, inputs):
        self.inputs = inputs

    def get_next_input(self):
        return self.inputs.pop(0) if len(self.inputs) > 0 else ""


class FakeBoard(object):
    pass


class TicTacToeAcceptanceTestCase(unittest.TestCase):
    def test_TicTacToe_newGameStarted_printsEmtpyBoard(self):
        console_input = PromptFake([])
        console_output = ConsoleSpy()
        board = TicTacToeBoard()

        expectedEmptyBoard = """\
         A B C
        0 | |
        ------
        1 | |
        ------
        2 | |
        Kommando: """

        board.to_string = MagicMock(return_value=expectedEmptyBoard)

        ttt = TicTacToeGame(console_input, console_output, board)
        ttt.start()

        self.assertEquals(console_output.getLoggedOuput(), expectedEmptyBoard)

    def test_TicTacToe_twoMoves_printsBoardWithXO(self):
        console_input = PromptFake(["A0", "B1"])
        console_output = ConsoleSpy()

        expectedBoard = """\
 A B C
0X| |
------
1 |O|
------
2 | |
Kommando: """
        board = TicTacToeBoard()
        board.to_string = MagicMock(return_value=expectedBoard)
        board.set_step = MagicMock()

        ttt = TicTacToeGame(console_input, console_output, board)
        ttt.start()

        self.assertEquals(console_output.getLoggedOuput(), expectedBoard)

        board.set_step.assert_has_calls([call("A0"), call("B1")])

if __name__ == '__main__':
    unittest.main()
