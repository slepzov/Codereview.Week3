class ChessPieces:

    def __init__(self, color, coordinate):
        self.state = 1
        self.color = color
        self.coordinate = coordinate

    def move(self, coordinate):
        pass


class King(ChessPieces):
    def move(self, coordinate):
        pass


class Queen(ChessPieces):
    def move(self, coordinate):
        pass


class Rook(ChessPieces):
    def move(self, coordinate):
        pass


class Bishop(ChessPieces):
    def move(self, coordinate):
        pass


class Knight(ChessPieces):
    def move(self, coordinate):
        pass


class Pawn(ChessPieces):
    def move(self, coordinate):
        pass


class Movement:
    # рокировка
    def Castling(first_piece: King, second_piece: Rook):
        pass

    # превращение пешки в фигуру
    def Promotion(begin_pawn: Pawn, chosen_piece: ChessPieces):
        pass

    # поедание фигуры
    def Capturing(first_piece: ChessPieces, second_piece: ChessPieces):
        pass

    # шах
    def Check(king: King):
        pass

    # мат
    def Checkmate(king: King):
        pass


if __name__ == "__main__":
    my_korol = King("white", "e1")
    my_ladia = Rook("white", "h1")
    Movement.Castling(my_korol, my_ladia)
    my_korol.move("h2")
    print(type(my_korol))