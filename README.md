# Calculator Application

This project is a command-line-based **Calculator Application** implemented in Python. It provides basic arithmetic operations along with a persistent history feature, making it convenient for users to review past calculations or manage their history.

---

## Features

1. **Basic Arithmetic Operations**
   - Addition (`+`)
   - Subtraction (`-`)
   - Multiplication (`*`)
   - Division (`/`)

2. **Persistent History**
   - All calculations are stored in a `history.txt` file for future reference.

3. **History Management**
   - View history.
   - Clear history.

4. **Command Interface**
   - Interactive and easy-to-use terminal interface with multiple commands.

---

## How to Use

### Commands Overview
Upon running the application, you will see the available commands:

| Command | Description                           |
|---------|---------------------------------------|
| `0`     | Exit the program                     |
| `1`     | Perform addition                     |
| `2`     | Perform subtraction                  |
| `3`     | Perform multiplication               |
| `4`     | Perform division                     |
| `5`     | Show calculation history             |
| `6`     | Clear calculation history            |
| `7`     | Display the main menu again          |

### Running the Application
1. Launch the program by running the script:
   ```bash
   python <filename>.py
   ```

2. Follow the prompts to input commands and perform calculations.

### Example Workflow
1. Select a command (e.g., `1` for addition).
2. Input the two numbers for the operation when prompted.
3. View the result.
4. Check the history (`5`) or perform another operation.

---

## File Structure

- **`history.txt`**: A file created automatically to store calculation history.
  - Each entry is stored in the format: `<number1>;<operator>;<number2>;<result>`.

---

## Example Usage

### Initial Menu
```plaintext
Calculator
0 calculations stored in history
Commands:
0 - end program
1 - calculate addition (+)
2 - calculate subtraction (-)
3 - calculate multiplication (*)
4 - calculate division (/)
5 - show history
6 - empty history
7 - show commands
```

### Performing Addition
```plaintext
Select command: 1
Input number: 5
Input number: 3
Result: 8.0
```

### Viewing History
```plaintext
Select command: 5
1 calculations in history:
5.0;+;3.0;8.0
```

### Clearing History
```plaintext
Select command: 6
History cleared.
```

---

## Future Enhancements
- Add support for more advanced operations (e.g., square root, exponentiation).
- Implement input validation to handle invalid or non-numeric inputs gracefully.
- Introduce a graphical user interface (GUI) for better user experience.
- Allow history export to external files (e.g., CSV or JSON).

---

## How to Contribute
Feel free to fork this repository and submit pull requests to improve functionality or fix any issues.

---

## Author
This Calculator Application was created to demonstrate the use of Python for simple command-line tools with file I/O capabilities. Enjoy using it for your calculations!

