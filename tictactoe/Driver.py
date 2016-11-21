from tictactoe.Board import TicTacToeBoard
from tictactoe.GameLoop import GameLoop, ConsoleInput, ConsoleOutput


class GameDriver(object):
    def __init__(self, input, output):
        self.game = GameLoop(input, output, TicTacToeBoard())

    def run(self):
        self.game.start()


def main():
    GameDriver(ConsoleInput(), ConsoleOutput()).run()


if __name__ == '__main__':
    main()