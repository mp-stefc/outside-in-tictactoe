from tictactoe.Board import TicTacToeBoard
from tictactoe.GameLoop import GameLoop, IConsoleOutput, IConsoleInput


class ConsoleOutput(IConsoleOutput):
    def display(self, ttt_string):
        print(ttt_string)


class ConsoleInput(IConsoleInput):
    def get_next_input(self):
        return input()


class Application(object):
    def __init__(self, input, output):
        self.game = GameLoop(input, output, TicTacToeBoard())

    def run(self):
        self.game.start()


def main():
    Application(ConsoleInput(), ConsoleOutput()).run()


if __name__ == '__main__':
    main()

