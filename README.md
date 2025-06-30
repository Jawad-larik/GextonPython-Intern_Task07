# GextonPython-Intern_Task07
Develop a program that allows players to interact with a 2D maze game. The game should provide a user-friendly interface for navigation and display the maze, player position, obstacles, and goal. The maze layout should be randomly generated for each session, offering a unique experience to players.

# 2D Maze Game in Pygame
A simple and fun 2D maze game built with Python and Pygame. The player starts at the top-left corner of a randomly generated maze and must navigate to a randomly selected goal cell using the arrow keys.

---

## 🚀 Features

* ✅ Randomly generated maze each time you play
* ✅ Smooth player movement using arrow keys
* ✅ Dynamic UI showing time and move count
* ✅ Dotted path hint to assist in solving
* ✅ Restart and quit options

---

## 🎮 How to Play

* Use **Arrow Keys** to move:

  * `↑` Move Up
  * `↓` Move Down
  * `←` Move Left
  * `→` Move Right

* Press **`R`** to restart the game with a new maze

* Press **`Q`** to quit the game

---

## 📂 Project Structure

```
maze-game/
├── main.py               # Main game loop and display logic
├── maze_generator.py     # Maze generation and path-finding logic
├── README.md             # This file
```

---

## 🛠 Requirements

* Python 3.x
* Pygame

### Install Requirements:

```bash
pip install pygame
```

---

## 🧠 How It Works

* The maze is carved using a depth-first search algorithm.
* The solution path is shown as dotted light-blue dots.
* A random cell along the valid path is selected as the goal.
* The player cannot move through walls.

---

## 📝 To-Do / Ideas

*

---

## 👨‍💻 Author

Made with ❤️ by Jawad Larik

---

## 📃 License

This project is open-source and free to use for educational or personal purposes.

Wishing you the best! 

Regards, Jawad Larik
