# Ai-Arcade Game
A 2D PC game created using AI 

Welcome to the 2D Arcade Game! This classic arcade-style game features a player who must collect coins to level up, avoid walls, and manage a timer. The game increases in difficulty as you progress through levels, adding more obstacles. It also includes sound effects when coins are collected.

## Table of Contents
- [Features](#features)
- [Installation](#Installation)
- [Game Controls](#Game-Controls)
- [How to Play](#How-to-Play)

## Features
- Player Movement: Use the arrow keys to move the player character around the screen.
- Coin Collection: Collect coins to increase your score and level up.
- Walls & Obstacles: Avoid randomly generated walls that block your movement.
- Timer: Manage the time remaining while collecting coins.
- Level Progression: Each level requires more coins to level up, increasing the number of obstacles.
- Game Over: Once the timer runs out, the game will display your score, and you can choose to return to the main menu.
- Sound Effects: A sound plays when you collect a coin.
- Responsive Controls: The player moves in response to key presses, with adjustments for smoother gameplay.

## Installation
This game is written in Python, so please ensure you have Python installed on your computer. 

### Step 1: Install Python
- Go to the official Python website: https://www.python.org/downloads/

### Step 2: Install dependencies:
The game uses the `pygame` dependency, You can install the necessary dependencies using pip:

```bash
   pip install pygame
   ```
### Step 3: Clone this repository:

```bash
    git clone https://github.com/Hooba97/Ai-Arcade-Game.git
   ```

### Step 4: Run the game:

Navigate into the project directory:
```bash
    cd Ai-Arcade-Game
   ```
then Run 
```bash
    python game.py
   ```
## Game Controls
- Arrow Keys: Move the player character around the screen.
- ESC: Pause the game and bring up a confirmation screen to exit.
- Enter: Start the game from the main menu.
- Y: Confirm exit if you're in the "Are you sure you want to exit?" screen.
- N: Cancel exit if you're in the "Are you sure you want to exit?" screen.

## How to Play
- Start the Game: Press Enter on the main menu to start playing.
- Move the Player: Use the arrow keys (Up, Down, Left, Right) to move your player around the screen.
- Collect Coins: Move your player to collect coins scattered across the screen.
- Avoid Walls: Collide with walls to teleport back to the center of the screen (walls block your movement).
- Level Up: Collect enough coins to level up and face more obstacles in the next level.
- Manage Time: Keep an eye on the timer, and collect coins to extend it by 2 seconds with each coin collected.
- Game Over: When the time runs out, a game-over message appears showing your final score.
