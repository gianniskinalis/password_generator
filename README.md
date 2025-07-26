# Password Generator (Basic Version)

This is a simple password generator written in Python. It was created as my first beginner project.

## What It Does

- Asks the user to enter the desired length (between 1-100)
- Defines the character sets based on user input
- Ensures that at least one character type is included
- Guarantees that at least one character from each selected type is used
- Generates a random password based on the character sets
- Prints the generated password

## Technologies Used

- Python 3
- Built-in libraries: `random`, `string`

## Example Output

```
Enter the desired password length: 10
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): n
Generated Password: jyq1daZ0vE
```
## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository or copy the code to a `.py` file.
3. Run the script:

```bash
python password_generator.py
```

## Future Improvements

- Catch ValueError if user types a non-number for length
- Add GUI with tkinter
- Add password strength meter 

## Author

Created by Giannis Kinalis. This is my first project in Python as a part of learning the language.  Suggestions welcome!