
# Password Generator

This project provides a simple and versatile password generator with both Command-Line Interface (CLI) and Graphical User Interface (GUI) options. You can generate strong and random passwords based on user-defined criteria such as length, and the inclusion of letters, numbers, and symbols.

## Features

- **CLI Mode**: A text-based interface that prompts the user for password criteria.
- **GUI Mode**: A graphical interface built with Tkinter for easy use.
- **Customizable**: Choose the length of the password and whether to include letters, numbers, and symbols.

## Installation

Ensure you have Python installed on your system. This project requires Python 3.x.

### Dependencies

This project requires the following Python libraries:
- `tkinter` (included with standard Python installations)
- `random`
- `string`

You can install additional required packages using `pip`:

```bash
pip install tk
pip install matplotlib
```

## Usage

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/repositoryname.git
cd Addres_to_project_folder
```

Run the main Python script and choose between CLI and GUI modes:

```bash
python Fle_name.py
```

### CLI Mode

In CLI mode, follow the prompts to enter the desired password length and whether to include letters, numbers, and symbols.

### GUI Mode

In GUI mode, use the graphical interface to enter the desired password length and select whether to include letters, numbers, and symbols. Click the "Generate Password" button to create the password, which will be copied to your clipboard.

## Functions

### `generate_password(length, use_letters=True, use_numbers=True, use_symbols=True)`

Generates a random password based on specified criteria.

- `length`: The length of the password.
- `use_letters`: Whether to include letters in the password.
- `use_numbers`: Whether to include numbers in the password.
- `use_symbols`: Whether to include symbols in the password.

### `cli_main()`

Runs the CLI version of the password generator.

### `generate_and_copy_password()`

Generates a password and copies it to the clipboard (used in GUI mode).

### `gui_main()`

Runs the GUI version of the password generator.

## Advanced Features

### Data Storage (For BMI Tracker Project)

If you are integrating this password generator into a project like a BMI tracker that stores data, you might want to store the generated passwords securely in a database. Make sure to follow best practices for password storage, such as hashing passwords before saving them to a database.



## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Contact

For any questions or feedback, please contact [Chidanand] at [chidananda1412@gmail.com].
```

