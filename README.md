
# Tic-Tac-Toe Console Simulator

This is a simple in-console Tic-Tac-Toe game implemented in Python. It supports several modes of play, including **Player vs. Player**, **Player vs. AI**, and **AI vs. AI**. The game provides a text-based board interface and allows users to interact with the game through the command line.

## Features

### 1. **Game Modes**
   - **Player vs. Player**: Two human players can take turns playing the game on the same machine.
   - **Player vs. AI**: A human player competes against an AI opponent, where the AI can have different levels of difficulty.
   - **AI vs. AI**: Two AI players (with configurable difficulty) can play against each other automatically, showcasing different AI algorithms.

### 2. **AI Algorithms**
   - **Random AI**: The AI randomly selects one of the available legal moves.
   - **Winning AI**: The AI looks for a move that would lead it to victory and plays that move if available.
   - **Best AI**: This AI is a more strategic player that first tries to win, then blocks the opponent's winning moves, and lastly makes random moves if no winning or blocking move is found.

### 3. **Interactive Gameplay**
   - The board is displayed after every move, and the current state of the game is visible in the console.
   - The user can enter coordinates for their move, and the game will validate whether the move is legal (i.e., the cell is not already occupied).
   - The game continues until there's a winner or the board is full, resulting in a draw.

### 4. **Game Flow**
   - Players or AI are alternately prompted for moves, with the board updated after each move.
   - The game automatically detects a winner or a draw and announces the result.
   - In **AI vs. AI** mode, there is a 3-second delay between AI moves to simulate a more natural gameplay experience.

### 5. **Customizable AI Difficulty**
   - The **Player vs. AI** mode allows users to choose between three difficulty levels for the AI: `random`, `winning`, and `best`.
   - In **AI vs. AI** mode, users can select different difficulty levels for both AI players, allowing for a more dynamic match.

### 6. **Error Handling**
   - The game ensures that only valid inputs are accepted, prompting the player to re-enter the coordinates if they are outside the valid range or if the cell is already occupied.

## How to Play

1. **Start the Game**: When running the program, you'll be asked to choose a game mode:
   - Type `AI` for Player vs. AI.
   - Type `Player` for Player vs. Player.
   - Type `AIvAI` for AI vs. AI.

2. **Player vs. Player**: The two players take turns entering their moves by providing the X and Y coordinates (from 0 to 2) for the cell they want to place their mark in.

3. **Player vs. AI**: The human player plays as either 'X' or 'O', and the AI will play as the other symbol. You will be prompted to choose the AI's difficulty level before starting.

4. **AI vs. AI**: In this mode, you select difficulty levels for both AI players, and the game will automatically play itself with a 3-second delay between AI turns.

5. **End of Game**: The game announces the winner if there is one or declares a draw if the board is full and no winner is found.

## How to Run

1. Make sure you have Python installed on your machine.
2. Save the code in a `.py` file, for example, `tic_tac_toe.py`.
3. Open your terminal or command prompt and navigate to the directory where the file is located.
4. Run the script by typing:
``bash
python tic_tac_toe.py
``
 5. Follow the in-console prompts to play the game.
