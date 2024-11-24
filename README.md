# Python Aim Trainer 

## Overview
This **Aim Trainer** is a lightweight Python-based application designed to help users enhance their mouse accuracy and reflexes. The game features a growing target that the player must hit before it grows too large, with performance statistics tracked and saved for post-game review.

## Features
- **Dynamic Target**: A target appears on the screen, growing gradually in size. The player's goal is to click it before it exceeds the maximum size.
- **Scoring System**: Tracks the player's hits and clicks to calculate accuracy and total score.
- **Game Over Mechanism**: The game ends if the target exceeds its maximum size, displaying a "Game Over" message.
- **High-Performance**: Runs at 144 FPS for smooth gameplay.
- **Score Saving**: Automatically saves the player's session details to a text file, including score, clicks, accuracy, and timestamp.
- **Reset Mechanism**: Automatically resets the game after 3 seconds of the "Game Over" screen.

## Prerequisites
To run the Aim Trainer, you need:
1. Python 3.8 or newer.
2. The `pygame` library installed. Install it using:
   ```bash
   pip install pygame
   ```

## How to Play
1. Launch the application by running the Python script:
   ```bash
   python aim_trainer.py
   ```
   Or, if you want it to be an exe file
   1. Install pyinstall
      ```bash
      pip install pyinstall
      ```
    2. Build using pyinstall    
       ```bash
      pyinstaller --add-data "imgs/icon.jpg;imgs" --hidden-import=pygame --windowed --onefile aimtrainer.py
      ```
3. A red target will appear on a gray background. Click on the target to score points before it grows too large.
4. Each successful hit will increase your score and spawn a new target with a random size and position.
5. If the target grows beyond its maximum size, the game ends.

## Game Controls
- **Mouse Click**: Hit the target to score points.
- **Close Window**: Quit the game.

## Statistics
- **Score**: Total successful hits.
- **Clicks**: Number of clicks made during the session.
- **Accuracy**: Calculated as:
  \[
  	ext{Accuracy (\%)} = \left( rac{	ext{Score}}{	ext{Clicks}} 
ight) 	imes 100
  \]
- **Saved Details**: Includes the date, score, number of clicks, and accuracy percentage.

## Code Highlights
- **Dynamic Target Behavior**: The target grows at a steady rate (`growthspeed`) and resets upon successful hits.
- **Game Over Logic**: Triggered when the target exceeds its maximum size, with a timed reset.
- **Score Saving**: Ensures the session data is saved even if the player quits mid-game.

## Customization
- **Target Growth Speed**: Modify the `growthspeed` variable to adjust difficulty.
- **Maximum Target Size**: Change the `maxballsize` variable for game balancing.
- **Window Size**: Update the resolution in the `pygame.display.set_mode` function for different screen sizes.

## Troubleshooting
1. **Missing `pygame` Library**: Install it with `pip install pygame`.
2. **Game Runs Slowly**: Lower the frame rate (`clock.tick`) or close other applications to free resources.
3. **Score Not Saving**: Ensure the script has write permissions in the current directory.

---

Enjoy improving your aim and reflexes with this **Aim Trainer**!
