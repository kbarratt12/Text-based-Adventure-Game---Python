# Text-Based Adventure Game – Python

## Project Overview
This project is a collaborative text-based adventure game developed using Python. It features a branching storyline, multiple character classes, randomized combat outcomes, and multiple endings based on player decisions. The game was built during an introductory programming course, demonstrating practical skills in structured code organization, conditional logic, and input handling.

## Contributors
- Steven Dang – sdang4@student.gsu.edu  
- Rachit Kowatra – rkowatra1@student.gsu.edu  
- Malachi Barratt – mbarratt2@student.gsu.edu

## Game Features
- Multiple character archetypes (Warrior, Knight, Clown, Rogue)
- Custom character and weapon creation
- Turn-based combat system using random dice rolls
- Karma tracking that influences game ending
- Four main battle scenarios and three unique endings
- Modular architecture across two Python files

## File Descriptions
| File | Description |
|------|-------------|
| `scenariodup.py` | Main script containing the storyline, scenario progression, and battle logic |
| `commands.py` | File with character creation functions, damage logic, and utility features |

## How to Run the Game
Ensure you have Python 3.x as well as the commands.py file installed. Then from the terminal or your IDE, run:

```bash
python scenariodup.py 
```

## Sample Gameplay Logic
- Create a character and select a class.
- Progress through multiple combat scenarios.
- Make choices that influence your karma.
- Reach one of three possible endings based on karma and survival.

## Technical Highlights
- Use of random for dice rolls and dynamic outcomes
- Function decomposition for character generation and combat logic
- Dictionaries and lists for structured data storage
- Progressive game design through conditional branching
- Input validation and user interaction

## Future Improvements
- Add save/load functionality for session persistence
- Refactor into an object-oriented structure using Python classes
- Create a visual version using a basic GUI (e.g., Tkinter or PyGame)
- Improve balance mechanics and include more enemy types
