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
        index = pos[1] * 6 + pos[0]

        if index >= len(self.squares) or index < 0:
            return None

        return self.squares[index]

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

        if targetSquare == None:
            return False

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

    def makeMove(self, piece, targetSquare, isAI):
        sourceSquare = self.getSquareFromPos(piece.pos)
        sourceSquare.occupyingPiece = None
        targetSquare.occupyingPiece = piece

        piece.pos = targetSquare.pos

        if not isAI:
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
                    self.makeMove(self.selectedPiece, clickedSquare, False)
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

    def evaluate(self, isEnemy):
        # Heuristic:
        # * +1 for white piece, -1 for black piece
        # * Distance to goal: How close are all pieces to the last row

        pawnTable = [
            [100, 100, 100, 100, 100, 100],
            [50, 50, 50, 50, 50, 50],
            [20, 20, 20, 20, 20, 20],
            [10, 10, 10, 10, 10, 10],
            [5, 5, 5, 5, 5, 5],
            [0, 0, 0, 0, 0, 0]
        ]

        pieces = self.getAllPieces()

        whitePieces = [p for p in pieces if p.color == "white"]
        blackPieces = [p for p in pieces if p.color == "black"]

        value = len(whitePieces) - len(blackPieces)

        for pawn in blackPieces:
            value += pawnTable[pawn.pos[1]][pawn.pos[0]]

        return value

    def alphaBetaMinimax(self, player, alpha, beta, depth):
        if depth == 0:
            return (self.evaluate(True), None) if player == "white" else (-self.evaluate(False), None)
        
        pieces = [p for p in self.getAllPieces() if p.color == player]
        bestAction = None

        for piece in pieces:
            moves = piece.getMoves()

            for move in moves:
                targetPos = (piece.pos[0] + move[0], piece.pos[1] + move[1])
                prevSquare = self.getSquareFromPos(piece.pos)
                targetSquare = self.getSquareFromPos(targetPos)

                if targetSquare == None or not self.isValidMove(piece, targetSquare):
                    continue

                action = (piece, targetSquare)
                bestAction = action
                nextPlayer = "black" if player == "white" else "white"

                # prevPawn -> targetSquare
                # if there is a pawn, targetPawn -> None
                prevPawn = None
                if targetSquare.occupyingPiece:
                    prevPawn = targetSquare.occupyingPiece

                # Make the move
                self.makeMove(piece, targetSquare, True)

                (score, _) = self.alphaBetaMinimax(nextPlayer, alpha, beta, depth - 1)

                # Undo the move
                # 1. Move piece back into original position
                prevSquare.occupyingPiece = piece
                piece.pos = prevSquare.pos
                targetSquare.occupyingPiece = None

                # 2. If the move killed an enemy pawn, reinstate that pawn
                if prevPawn:
                    targetSquare.occupyingPiece = prevPawn
                    prevPawn.pos = targetSquare.pos

                if player == "white":
                    if score >= beta:
                        return (beta, None)
                    
                    if score > alpha:
                        alpha = score
                else:
                    if score <= alpha:
                        return (alpha, action)
                
                    if score < beta:
                        beta = score
                        bestAction = action
        
        return (alpha, None) if player == "white" else (beta, bestAction)