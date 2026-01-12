#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        """Check if all non-mine cells have been revealed"""
        total_cells = self.width * self.height
        mine_cells = len(self.mines)
        non_mine_cells = total_cells - mine_cells
        
        # Count revealed non-mine cells
        revealed_non_mine = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.revealed[y][x] and (y * self.width + x) not in self.mines:
                    revealed_non_mine += 1
        
        # Win if all non-mine cells are revealed
        return revealed_non_mine == non_mine_cells

    def play(self):
        while True:
            self.print_board()
            
            # Check for win condition
            if self.check_win():
                self.print_board(reveal=True)
                print("Congratulations! You've won the game.")
                break
                
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
            except IndexError:
                print(f"Coordinates out of bounds. Please use 0-{self.width-1} for x and 0-{self.height-1} for y.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
