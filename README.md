# Python Design Patterns Practice

This is a practice project to become familiar with Object-Oriented Programming (OOP) and Design Patterns in Python.

## Examples

### 1. Board Game Example
Located in `Board-Game-Example/`

This example demonstrates a simple board game structure.
- **Board**: Represents the game board, composed of a grid of tiles.
- **Tile**: Represents a single position on the board, which can hold units.
- **Unit**: Represents a game unit with properties and weapons.

Usage:
Run `Board-Game-Example/Board.py` to see the board setup and unit placement.

### 2. Instrument Inventory Example
Located in `Instrument-Inventory-Example/`

This example simulates an inventory system for a musical instrument shop. It demonstrates how to decouple the search logic from the specific instrument types using a specification object.

- **Inventory**: Manages a collection of instruments.
- **InstrumentSpec**: Encapsulates the properties of an instrument (e.g., builder, model, wood type) to facilitate flexible searching.
- **FindGuitarTester.py**: A test script that initializes the inventory and performs a search.

Usage:
Run `Instrument-Inventory-Example/FindGuitarTester.py`.

### 3. Singleton Example
Located in `Singleton-Example/`

This example demonstrates the **Singleton Pattern**, ensuring a class has only one instance and providing a global point of access to it.

- **Logger**: A class that implements the Singleton pattern. It ensures only one logger instance exists throughout the application lifecycle.

Usage:
Run `Singleton-Example/TestSingleton.py` to verify that multiple instantiations return the same object.
