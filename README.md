# Grimoire-Dargent-deininger-pythonproject-Int1

---

## 1. Presentation

# Hogwarts Adventure

A text-based Python adventure inspired by a magical school. Create a character, attend classes, learn spells, brew potions, and defend the school in duels and Quidditch matches.

## Features
- Character creation with attribute distribution
- House sorting and house points system
- Spell learning and quizzes
- Potion brewing minigame
- Duels and boss encounters
- Quidditch match simulation

## Requirements
- Python 3.10 or newer
- No external dependencies (standard library only)

## Installation
1. Clone the repository:
  - git clone `https://github.com/Smoothy909/Grimoire-Dargent-deininger-pythonproject-Int1.git`
2. Enter the project folder:
  - cd `Grimoire-Dargent-deininger-pythonproject-Int1`

### Running the game
- Launch application from the root of the project :
  - `python -m hogwarts.main`
  - ou `python hogwarts\main.py`
- debug/test Mode :
  - At the start, choose `test mode` to execute a specific chapter (useful for fast tests).
- Usage exemple :
  - Start -> create character -> follow chapters.

## Project structure (important files)
- `hogwarts/main.py` — entry point and game loop
- `hogwarts/menus.py` — menu and chapter dispatcher
- `hogwarts/chapters/` — chapter logic and gameplay events
- `hogwarts/universe/` — character and house utilities
- `hogwarts/data/` — JSON data for spells, potions, quizzes, houses

### Key functionalities
- Character creation and display (attributes, inventory, money).
- Sorting ceremony (house assignment).
- Spell learning (spell repertoire management).
- Mini-games: magic quiz, potion brewing, Quidditch match.
- House points system and score updates.
- Duels against enemies (attack/defence system).
- Implicit saving of decisions via the character's status in memory.

---

## 2. Logbook

### Project timeline (examples)
- 22/11/2025: Initialise the project, basic folder structure.
- 23/11/2025: Implement character creation and display.
- 28 November 2025: Add chapters 1 to 3 (division, spells, quiz).
- 2025-12-06: Addition of Quidditch and potions (chapters 4 and 5).
- 2025-12-13: Implementation of duels and end of the game (chapter 6).
- 2026-01-02: Manual testing, corrections and preparation of final submission.
- 2026-01-06: Final submission

### Task distribution
- Grégoire d'Argent: Project architecture, chapters 1, 4, 5 and 6, testing, corrections and final README.
- Gabrielle Deininger: Chapters 2 and 3, user interfaces, JSON data integration.

---

## 3. Control, testing, and validation

### Input and error handling
- Input functions use centralised utilities in `hogwarts/utils/input_utils.py` (`ask_text`, `ask_choice`, `ask_number`) to validate and normalise user responses.
- Manual validation in `create_character()`:
  - Attributes are forced to be within the expected range (0–10) and the sum does not exceed 30.
- Protection against negative money: `modify_money()` prevents `money` from being negative.
- List of main validations:
  - Choice via restrictive menus (`ask_choice`) → avoids invalid responses.
  - Callbacks for out-of-range numerical entries.

### Known bugs
- None

### Testing strategies
- Manual tests (procedure):
  1. Create a character with varying attributes (sum ≤ 30). Expected: acceptance.
  2. Attempt to enter an invalid value for an attribute (e.g. -1 or 11). Expected: re-prompt until valid value is entered.
  3. Launch `test mode` in `main` and run each chapter separately.
  4. Chapter 3: verify that spell learning adds names to `character[“spells_learned”]` (no exceptions).
  5. Chapter 4: simulate a Quidditch match and verify that points are updated via `display_winning_house`.
6. Chapter 5: verify the count of successful potions and financial gains/points.
7. Chapter 6: execute duels and verify changes to attributes, inventory, and money.
- Specific test cases (examples):
  - Test A (attributes): Enter 10,10,10,0 → sum 30 → character created.
  - Test B (potions): Validate that no `IndexError` occurs when randomly selecting potions.
  - Test C (spells): Ensure that `learn_spells()` does not raise a `NameError` and that `character[“spells_learned”]` contains the listed spells.
  - Test D (money floor): Force `modify_money(character, -10000)` → `money` must remain ≥ 0.

### Expected results
- All interactive functions must complete without raising any unhandled exceptions.
- House scores must change and the winner must be displayed.

---

## Final notes

- Thank you for this project :D ! — it was very enjoyable to develop.
