# Little Devil

A lightweight desktop pet application developed with Python and PySide6.

<img width="655" height="222" alt="image" src="https://github.com/user-attachments/assets/5106fefb-76a0-4b79-bdb1-fa4ef19aa187" />

## Overview

**Little Devil** is a desktop pet application developed with Python and PySide6. The project focuses on implementing an interactive desktop character with modular movement, dialogue, behavioral, and LLM-based conversation systems.

The current implementation provides basic desktop interaction, scripted startup animation, randomized idle behaviors, dialogue display, and multi-turn AI conversation.

The project is currently under active development.

## Features

* Draggable desktop character
* Transparent, frameless desktop window
* Scripted startup animation
* Dialogue display system
* Modular movement controller
* Modular dialogue controller
* Randomized idle behaviors
* Character rotation animation
* LLM-powered conversation
* Multi-turn conversation with conversation history
* External system prompt for character personality

## Technologies

* **Python**
* **PySide6**
* **OpenAI Python SDK**
* **DeepSeek API**
* **Krita** — character artwork

## Project Structure

```text
little_devil/

├── assets/
│   └── mini_devil.png
│
├── codes/
│   ├── main.py
│   ├── movement.py
│   ├── dialogue.py
│   ├── llm.py
│   └── test_llm.py
│
├── docs/
│   ├── peanut_butter_personality.md
│   ├── peanut_butter_prompt_notes.md
│   └── peanut_butter_system_prompt.md
│
├── README.md
└── .gitignore
```

## Architecture

The project separates the desktop pet's core components into independent modules.

* `main.py` — application entry point and desktop pet interface
* `movement.py` — movement and animation controller
* `dialogue.py` — dialogue display and chat window controller
* `llm.py` — LLM API interface and conversation management
* `test_llm.py` — terminal-based LLM conversation test
* `docs/` — character personality and system prompt documentation
* `assets/` — character and other visual resources

The current architecture separates the desktop pet interface from the LLM interaction layer, allowing the conversation system to be developed independently from the character's visual and behavioral components.

## Conversation Architecture

```text
Little Devil
      │
      ▼
DialogueController
      │
      ▼
   ChatWindow
      │
      ▼
     llm.py
      │
      ▼
  DeepSeek API
      │
      ▼
 Character System Prompt
```

The character personality is stored separately from the application code and loaded as a system prompt at runtime.

Conversation history is maintained during the current application session to support multi-turn dialogue.

## Current Development Status

The current version implements the basic desktop pet framework, initial character behaviors, and an LLM-powered conversation system.

Implemented:

* Basic desktop window
* Character rendering
* Mouse-based dragging
* Startup animation
* Startup dialogue
* Random idle behavior
* Rotation animation
* Interactive chat window
* DeepSeek API integration
* Multi-turn conversation
* External character system prompt

## Planned Features

* Additional idle behaviors
* More natural movement
* Desktop boundary detection
* Window climbing
* Falling and physics-based movement
* Expanded user interaction
* Voice interaction
* Additional LLM providers
* Configurable model and API settings

## Installation

### Requirements

* Python 3.13.3
* PySide6
* OpenAI Python SDK

### Install Dependencies

Clone the repository and install the required packages:

```bash
pip install PySide6 openai
```

### API Key

Little Devil currently uses the DeepSeek API for LLM-powered conversation.

Set the following environment variable before running the application:

```text
DEEPSEEK_API_KEY
```

Do not place your API key directly in the source code or commit it to the repository.

### Run

Start the desktop pet with:

```bash
python codes/main.py
```

The terminal-based LLM test can be run with:

```bash
python codes/test_llm.py
```

## License

License information will be added as the project develops.
