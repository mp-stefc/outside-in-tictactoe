class IConsoleOutput:
    def display(self, ttt_string):
        pass


class ConsoleOutput(IConsoleOutput):
    def display(self, ttt_string):
        print(ttt_string)


class TicTacToeGame(object):
    def __init__(self, ui_input, ui_output, game_board):
        self.input = ui_input
        self.output = ui_output
        self.board = game_board

    def display_board(self):
        self.output.display(self.board.to_string())

    def start(self):
        while True:
            self.display_board()
            next_step = self.input.get_next_input()
            if next_step == "":
                return
            self.board.set_step(next_step)


def main():
    ttt = TicTacToeGame(None, ConsoleOutput())
    ttt.start()

if __name__ == '__main__':
    main()