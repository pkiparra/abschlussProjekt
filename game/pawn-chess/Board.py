from Quad import Quad
from Pawn import Pawn

BUTTON_MOUSE_LEFT = 1
BUTTON_MOUSE_RIGHT = 3


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tileWidth = width // 6
        self.tileHeight = height // 6
        self.selectedPiece = None
        self.turn = "white"
        self.config = [
            ["b", "b", "b", "b", "b", "b"],
            [
                "",
                "",
                "",
                "",
                "",
                "",
            ],
            [
                "",
                "",
                "",
                "",
                "",
                "",
            ],
            [
                "",
                "",
                "",
                "",
                "",
                "",
            ],
            [
                "",
                "",
                "",
                "",
                "",
                "",
            ],
            ["w", "w", "w", "w", "w", "w"],
        ]
        self.squares = self.generateSquares()
        self.setupBoard()

    def draw(self, screen):
        for square in self.squares:
            square.draw(screen)

    def generateSquares(self):
        output = []
        for y in range(6):
            for x in range(6):
                output.append(Quad(x, y, self.tileWidth, self.tileHeight))
        return output

    def getSquareFromPos(self, pos):
        return self.squares[pos[1] * 6 + pos[0]]

    def getPieceFromPos(self, pos):
        return self.getSquareFromPos(pos).occupyingPiece

    def setupBoard(self):
        tileSize = (self.tileWidth, self.tileWidth)

        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                square = self.getSquareFromPos((x, y))
                if piece == "b":
                    square.occupyingPiece = Pawn((x, y), "black", tileSize)
                elif piece == "w":
                    square.occupyingPiece = Pawn((x, y), "white", tileSize)

    def isEnemyOnSquare(self, square):
        return (
            self.isPieceOnSquare(square)
            and square.occupyingPiece.color != self.turn
        )
    
    def isPieceOnSquare(self, square):
        return square.occupyingPiece is not None

    def isValidMove(self, piece, targetSquare):
        # Ignore this
        """
            diff = []

            for i in range(len(targetSquare)):
                diff.append(targetSquare[i] - piece.pos[i])

            move = tuple(diff)
        """

        move = tuple(x - y for x, y in zip(targetSquare.pos, piece.pos))

        possibleMoves = piece.getMoves()

        if move not in possibleMoves:
            return False

        # if first move, then pawn can move vertically by 2 tiles
        if move == possibleMoves[3]:
            (x, y), dir = piece.pos, move[1] // 2
            previousSquare = self.getSquareFromPos((x, y + dir))

            if self.isPieceOnSquare(targetSquare) or self.isPieceOnSquare(previousSquare):
                return False
            
            return not piece.hasMoved            

        # move is diagonal
        if move == possibleMoves[1] or move == possibleMoves[2]:
            return self.isEnemyOnSquare(targetSquare)
        # move is not diagonal
        else:
            return not self.isPieceOnSquare(targetSquare)

    def getAllPieces(self):
        pawns = []

        for square in self.squares:
            if square.occupyingPiece:
                pawns.append(square.occupyingPiece)

        return pawns

    def highlightSquares(self, shouldHighlight):
        for square in self.squares:
            if not shouldHighlight:
                square.highlight = False
                continue

            square.highlight = self.isValidMove(self.selectedPiece, square)

    def makeMove(self, piece, targetSquare):
        sourceSquare = self.getSquareFromPos(piece.pos)
        sourceSquare.occupyingPiece = None
        targetSquare.occupyingPiece = piece

        piece.pos = targetSquare.pos
        piece.hasMoved = True

    def handleClick(self, button, mx, my):
        x = mx // self.tileWidth
        y = my // self.tileHeight
        clickedSquare = self.getSquareFromPos((x, y))

        # piece not yet selected
        # check if the current player can select a given piece on the board
        if (
            not self.selectedPiece
            and clickedSquare.occupyingPiece
            and clickedSquare.occupyingPiece.color == self.turn
        ):
            if button == BUTTON_MOUSE_LEFT:
                self.selectedPiece = clickedSquare.occupyingPiece
                self.selectedPiece.setActive(True)

        # piece was selected
        # make sure the move is valid and then make the move
        if self.selectedPiece:
            if button == BUTTON_MOUSE_RIGHT:
                self.selectedPiece.setActive(False)
                self.selectedPiece = None
            elif button == BUTTON_MOUSE_LEFT:
                if self.isValidMove(self.selectedPiece, clickedSquare):
                    self.makeMove(self.selectedPiece, clickedSquare)
                    self.selectedPiece.setActive(False)
                    self.selectedPiece = None
                    self.turn = "black" if self.turn == "white" else "white"

        self.highlightSquares(self.selectedPiece is not None)

    def getStatus(self):
        # Check if white piece is in first row -> white wins.
        for i in range(0, 6):
            piece = self.getPieceFromPos((i, 0))
            if piece and piece.color == "white":
                return "white"

        # Check if black piece is in last row -> black wins.
        for i in range(0, 6):
            piece = self.getPieceFromPos((i, 5))
            if piece and piece.color == "black":
                return "black"
            
        # Check if all pawns are dead
        # Count number of pawns for each player
        numWhitePawns = 0
        numBlackPawns = 0

        for square in self.squares:
            piece = square.occupyingPiece

            if piece:
                if piece.color == "white":
                    numWhitePawns += 1
                elif piece.color == "black":
                    numBlackPawns += 1

        if numWhitePawns == 0:
            return "black"
        elif numBlackPawns == 0:
            return "white"
        
        # Draw.
        # A draw happens if there are no valid moves available for any piece
        pieces = self.getAllPieces()
        currentPieces = [piece for piece in pieces if piece.color == self.turn]

        for piece in currentPieces:
            possibleMoves = piece.getMoves()
            
            for move in possibleMoves:
                targetPos = (piece.pos[0] + move[0], piece.pos[1] + move[1])
                targetSquare = self.getSquareFromPos(targetPos)

                if self.isValidMove(piece, targetSquare):
                    return "continue"
                
        return "draw"