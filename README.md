# Little Devil

A lightweight desktop pet application developed with Python and PySide6.

<img width="655" height="222" alt="image" src="https://github.com/user-attachments/assets/5106fefb-76a0-4b79-bdb1-fa4ef19aa187" />


## Overview

**Little Devil** is a desktop pet application developed with Python and PySide6. The project focuses on implementing an interactive desktop character with modular movement, dialogue, and behavioral systems.

The current implementation provides basic desktop interaction, scripted startup animation, dialogue display, and randomized idle behaviors. The project is currently under active development.

## Features

* Draggable desktop character
* Transparent, frameless desktop window
* Scripted startup animation
* Dialogue display system
* Modular movement controller
* Modular dialogue controller
* Randomized idle behaviors
* Character rotation animation

## Technologies

* **Python**
* **PySide6**
* **Krita** — character artwork

## Project Structure

```text
little_devil/
├── assets/
│   └── mini_devil.png
├── codes/
│   ├── main.py
│   ├── movement.py
│   └── dialogue.py
├── README.md
└── .gitignore
```

## Architecture

The project separates the desktop pet's core components into independent modules.

* `main.py` — application entry point and desktop pet interface
* `movement.py` — movement and animation controller
* `dialogue.py` — dialogue display controller
* `assets/` — character and other visual resources

This modular structure is intended to make future behaviors and interaction systems easier to extend.

## Current Development Status

The current version implements the basic desktop pet framework and several initial behaviors.

Implemented:

* Basic desktop window
* Character rendering
* Mouse-based dragging
* Startup animation
* Startup dialogue
* Random idle behavior
* Rotation animation

## Planned Features

* Additional idle behaviors
* More natural movement
* Desktop boundary detection
* Window climbing
* Falling and physics-based movement
* User interaction
* Expanded dialogue system
* AI-powered conversation

## Installation

### Requirements

* Python 3.x
* PySide6

### Run

Clone the repository and install the required dependency:

```bash
pip install PySide6
```

Then run:

```bash
python codes/main.py
```

## License

License information will be added as the project develops.
