class ChessPiece:
    def __init__(self, name, symbol, description):
        self.name = name
        self.symbol = symbol
        self.description = description

    def __str__(self):
        return self.symbol

    def get_description(self):
        return self.description


class King(ChessPiece):
    def __init__(self):
        super().__init__("King", "K", "Король ходит на одну клетку в любом направлении.")


class Rook(ChessPiece):
    def __init__(self):
        super().__init__("Rook", "R", "Ладья ходит по горизонтали или вертикали.")


class Queen(ChessPiece):
    def __init__(self):
        super().__init__("Queen", "Q", "Ферзь ходит по диагонали, горизонтали или вертикали.")


class Knight(ChessPiece):
    def __init__(self):
        super().__init__("Knight", "N", "Конь ходит буквой 'Г'.")


class ChessGame:
    def __init__(self):
        self.pieces = {
            'K': King(),
            'R': Rook(),
            'Q': Queen(),
            'N': Knight()
        }

    def print_piece_info(self):
        print("Доступные фигуры и их обозначения:")
        for symbol, piece in self.pieces.items():
            print(f"{symbol}: {piece.name} - {piece.get_description()}")

    def play(self):
        self.print_piece_info()

        while True:
            piece_input = input("Выберите фигуру (введите буквенное обозначение): ")

            try:
                piece = self.pieces[piece_input.upper()]
                print(piece.get_description())

                # Введем пока маленький цикл, чтобы продемонстрировать его использование
                while True:
                    start_input = input("Введите начальную клетку (например, 'e2'): ")
                    end_input = input("Введите конечную клетку (например, 'e4'): ")

                    if len(start_input) != 2 or len(end_input) != 2:
                        print("Ошибка: Неверный формат ввода. Попробуйте снова.")
                        continue

                    start = (ord(start_input[0]) - 97, int(start_input[1]) - 1)
                    end = (ord(end_input[0]) - 97, int(end_input[1]) - 1)

                    print(f"Фигура {piece.name} может ходить с {start_input} до {end_input}.")

                    # Здесь можно добавить логику проверки хода согласно правилам шахмат

                    break  # Выходим из цикла, если ход проверен

            except KeyError:
                print("Ошибка: Неверное обозначение фигуры. Попробуйте снова.")


if __name__ == "__main__":
    game = ChessGame()
    game.play()
