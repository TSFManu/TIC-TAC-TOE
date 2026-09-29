# Tic-Tac-Toe Game

A simple command-line Tic-Tac-Toe game developed in Python. The game allows two players to compete on a 3x3 board, with automatic winner detection, draw detection, and replay functionality.

## Features

- Two-player gameplay
- Input validation
- Winner detection
- Draw detection
- Colored player symbols (if termcolor is installed)
- Replay option after game completion
- Simple and user-friendly interface

## Technologies Used

- Python 3
- termcolor (optional)

## Project Structure

```
tic-tac-toe/
│
├── main.py
├── README.md
├── statement.md
├── output.png
└── requirements.txt
```

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/tic-tac-toe.git
cd tic-tac-toe
```

### Install Dependencies

```bash
pip install termcolor
```

## Run Project

```bash
python main.py
```

## How to Play

1. Run the program.
2. Enter positions from 1 to 9.
3. Players take turns placing X and O.
4. First player to align three symbols wins.
5. If all cells are filled without a winner, the game ends in a draw.

## Output Screenshot

[View Output Screenshot](./output.png)

## Testing

- Tested for valid moves
- Tested for invalid inputs
- Tested for win conditions
- Tested for draw conditions

## Future Improvements

- Single-player mode with AI
- GUI version using Tkinter
- Online multiplayer support

## Author

Manu Singh
