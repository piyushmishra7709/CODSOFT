import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        
    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=" ", font='normal 20 bold', height=3, width=6, 
                                   command=lambda r=row, c=col: self.player_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
                
    def player_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", state=tk.DISABLED)
            if self.is_winner("X"):
                messagebox.showinfo("Tic-Tac-Toe", "Congratulations! You win!")
                self.reset_board()
            elif not self.get_empty_cells():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_board()
            else:
                self.ai_move()

    def ai_move(self):
        move = self.best_move()
        if move:
            self.board[move[0]][move[1]] = "O"
            self.buttons[move[0]][move[1]].config(text="O", state=tk.DISABLED)
            if self.is_winner("O"):
                messagebox.showinfo("Tic-Tac-Toe", "AI wins! Better luck next time.")
                self.reset_board()
            elif not self.get_empty_cells():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_board()

    def is_winner(self, player):
        win_conditions = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        return [player, player, player] in win_conditions

    def get_empty_cells(self):
        return [(x, y) for x in range(3) for y in range(3) if self.board[x][y] == " "]

    def minimax(self, board, depth, is_maximizing):
        if self.is_winner("X"):
            return -1
        if self.is_winner("O"):
            return 1
        if not self.get_empty_cells():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for (x, y) in self.get_empty_cells():
                board[x][y] = "O"
                score = self.minimax(board, depth + 1, False)
                board[x][y] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for (x, y) in self.get_empty_cells():
                board[x][y] = "X"
                score = self.minimax(board, depth + 1, True)
                board[x][y] = " "
                best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -float('inf')
        move = None
        for (x, y) in self.get_empty_cells():
            self.board[x][y] = "O"
            score = self.minimax(self.board, 0, False)
            self.board[x][y] = " "
            if score > best_score:
                best_score = score
                move = (x, y)
        return move

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ", state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
