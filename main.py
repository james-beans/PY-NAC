# PY-NAC | Noughts And Crosses (Tic-Tac-Toe)
# By: james-beans

# Date made: 2024-11-06
# Description: Noughts-And-Crosses/Tic-Tac-Toe in Python.


# Import system modules
import os
import sys
import ctypes

# Import logic modules
import turtle
import random
import numpy as np

# Import GUI modules
import win32api                # For displaying alert box on Windows
import tkinter as tk           # For displaying alert box on Linux
from tkinter import messagebox # For displaying alert box on Linux


# Initialize turtle screen
screen = turtle.Screen()
screen.title("PY-NAC | Noughts And Crosses (Tic-Tac-Toe)")
screen.setup(width=600, height=600)
screen.tracer(0)

# Global variables
board = [["" for _ in range(3)] for _ in range(3)]
cell_size = 200
player = "X"  # User's symbol
computer = "O"  # Computer's symbol

# Function to check if a font is installed on the system
def is_font_installed(font_name):
    try:
        # Check if font is available in the system fonts (using ctypes to call Windows API)
        hdc = ctypes.windll.gdi32.CreateCompatibleDC(0)  # Create device context
        hfont = ctypes.windll.gdi32.CreateFontW(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, font_name)
        ctypes.windll.gdi32.SelectObject(hdc, hfont)
        return True
    except Exception:
        return False

# Get the path to the font file
def get_font_path():
    if getattr(sys, 'frozen', False):  # Check if running as a standalone .exe
        # Access the bundled font in the executable
        font_path = os.path.join(sys._MEIPASS, 'fonts/ProductSans-Regular.ttf')
    else:
        # Access the font in development mode (when running as script)
        font_path = os.path.join(os.path.dirname(__file__), 'fonts/ProductSans-Regular.ttf')

    print(f"Font path: {font_path}")  # Debugging line
    return font_path

# Drawing the game board
def draw_grid():
    turtle.clear()
    turtle.color("black")
    turtle.pensize(5)

    # Draw vertical lines
    for i in range(1, 3):
        turtle.penup()
        turtle.goto(i * cell_size - cell_size * 1.5, cell_size * 1.5)
        turtle.pendown()
        turtle.goto(i * cell_size - cell_size * 1.5, -cell_size * 1.5)

    # Draw horizontal lines
    for i in range(1, 3):
        turtle.penup()
        turtle.goto(-cell_size * 1.5, i * cell_size - cell_size * 1.5)
        turtle.pendown()
        turtle.goto(cell_size * 1.5, i * cell_size - cell_size * 1.5)

    turtle.penup()
    screen.update()

def draw_symbol(x, y, symbol):
    """Draw X or O on the board at a specific row, column."""

    font_path = get_font_path()
    font_name = "Product Sans"

    full = (font_path, 60, "bold") if os.path.exists(font_path) else (font_name if is_font_installed(font_name) else "Arial", 60, "bold")

    row, col = y, x
    x = (col - 1) * cell_size
    y = (1 - row) * cell_size
    turtle.penup()
    turtle.goto(x, y - 50)
    turtle.write(symbol, align="center", font=full)
    board[row][col] = symbol
    screen.update()

def get_empty_cells():
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == ""]

def is_winner(symbol):
    """Check if the given symbol has won."""
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol or board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False

def check_tie():
    """Check if the board is full and there's no winner."""
    if all(board[row][col] != "" for row in range(3) for col in range(3)):
        show_game_over("It's a tie!", "warning", "retrycancel")
        return True
    return False

def computer_move():
    """Computer makes a move based on winning, blocking, or random strategy."""
    # Convert the board to a numpy array for easier manipulation
    board_array = np.array(board)

    # Check for a winning move
    for row, col in get_empty_cells():
        board[row][col] = computer
        if is_winner(computer):
            draw_symbol(col, row, computer)
            if is_winner(computer):
                show_game_over("The computer wins!", "info", "retrycancel")
                return
        board[row][col] = ""

    # Check for a blocking move (if player can win)
    for row, col in get_empty_cells():
        board[row][col] = player
        if is_winner(player):
            draw_symbol(col, row, computer)
            return
        board[row][col] = ""

    # If no win or block, choose a random move
    empty_cells = get_empty_cells()
    if empty_cells:
        row, col = random.choice(empty_cells)
        draw_symbol(col, row, computer)
        if is_winner(computer):
            show_game_over("The computer wins!", "info", "retrycancel")
        elif check_tie():
            return

def click_handler(x, y):
    row = int((1.5 * cell_size - y) // cell_size)
    col = int((x + 1.5 * cell_size) // cell_size)

    if row not in range(3) or col not in range(3) or board[row][col] != "":
        return

    draw_symbol(col, row, player)
    if is_winner(player):
        show_game_over("You win!", "info", "retrycancel")
    elif check_tie():
        return
    else:
        computer_move()

def show_game_over(message, icon_type="info", button_type="ok"):
    # Check the platform (Windows or Linux)
    if sys.platform == "win32":
        # Windows-specific code using win32api
        icon_flags = {
            "info": 0x00000040,
            "warning": 0x00000030,
            "error": 0x00000010,
        }

        button_flags = {
            "ok": 0x00000000,
            "okcancel": 0x00000001,
            "retrycancel": 0x00000005,
            "yesno": 0x00000004,
        }

        icon_flag = icon_flags.get(icon_type, 0x00000040)
        button_flag = button_flags.get(button_type, 0x00000000)

        # Show the message box using win32api
        result = win32api.MessageBox(0, message, "Game Over", icon_flag | button_flag)

        if result == 4:  # "Retry" button
            restart_game()
        else:
            screen.bye()  # Close the turtle window

    elif sys.platform == "linux" or sys.platform == "linux2":  # For Linux (Debian 12)
        # Linux-specific code using tkinter's messagebox
        root = tk.Tk()
        root.withdraw()  # Hide the main tkinter window

        # Define the message box type for tkinter
        icon_map = {
            "info": messagebox.INFO,
            "warning": messagebox.WARNING,
            "error": messagebox.ERROR,
        }

        button_map = {
            "ok": messagebox.OK,
            "okcancel": messagebox.OKCANCEL,
            "retrycancel": messagebox.RETRYCANCEL,
            "yesno": messagebox.YESNO,
        }

        icon = icon_map.get(icon_type, messagebox.INFO)
        buttons = button_map.get(button_type, messagebox.OK)

        # Show the message box using tkinter
        result = messagebox.askyesno("Game Over", message) if button_type == "yesno" else messagebox.showinfo("Game Over", message)

        # Restart the game if "Retry" is selected
        if result:
            restart_game()
        else:
            screen.bye()  # Close the turtle window

def restart_game():
    """Reset the game board and restart the game."""
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    turtle.clear()
    draw_grid()

# Set up the game
draw_grid()
screen.onclick(click_handler)

# Keep the screen open
turtle.done()
