import unittest

import tictactoe.GameLoop
from tictactoe.Driver import GameDriver


class ConsoleSpy(tictactoe.GameLoop.IConsoleOutput):
    def __init__(self):
        self.stored_output = ""

    def display(self, ttt_string):
        self.stored_output = ttt_string

    def getLoggedOuput(self):
        return self.stored_output


class PromptFake(tictactoe.GameLoop.IConsoleInput):
    def __init__(self):
        self.inputs = []

    def set_inputs(self, inputs):
        self.inputs = inputs

    def get_next_input(self):
        return self.inputs.pop(0) if len(self.inputs) > 0 else ""


class TicTacToeAcceptanceTestCase(unittest.TestCase):
    def setUp(self):
        self.console_input = PromptFake()
        self.console_output = ConsoleSpy()
        self.driver = GameDriver(self.console_input, self.console_output)

    def test_TicTacToe_newGameStarted_printsEmtpyBoard(self):
        self.console_input.set_inputs([])
        self.driver.run()

        expectedEmptyBoard = """\
 A B C
0 | |
------
1 | |
------
2 | |
Kommando: """
        self.assertEquals(self.console_output.getLoggedOuput(), expectedEmptyBoard)

    def test_TicTacToe_twoMoves_printsBoardWithXO(self):
        self.console_input.set_inputs(["A0", "B1"])
        self.driver.run()

        expectedBoard = """\
 A B C
0X| |
------
1 |O|
------
2 | |
Kommando: """
        self.assertEquals(self.console_output.getLoggedOuput(), expectedBoard)


if __name__ == '__main__':
    unittest.main()
