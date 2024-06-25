import random
import string
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# BEGINNER: Command-Line Interface (CLI) Password Generator
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """Generate a random password based on specified criteria."""
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

# BEGINNER: CLI Main Function
def cli_main():
    """Run the CLI version of the password generator."""
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the length of the password: "))
        use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
    except ValueError:
        print("Error: Length must be a positive integer.")
        return

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("Generated Password:", password)
    else:
        print("Error: At least one character type (letters, numbers, symbols) must be selected.")

# ADVANCED: GUI Password Generator
def generate_and_copy_password():
    """Generate a password and copy it to the clipboard."""
    length = length_var.get()
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    if length <= 0:
        messagebox.showerror("Error", "Length must be a positive integer.")
        return

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Password Generated", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "At least one character type (letters, numbers, symbols) must be selected.")

# ADVANCED: GUI Main Function
def gui_main():
    """Run the GUI version of the password generator."""
    global root, length_var, letters_var, numbers_var, symbols_var

    root = tk.Tk()
    root.title("Password Generator")

    main_frame = ttk.Frame(root, padding="20")
    main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(main_frame, text="Length:").grid(column=0, row=0, sticky=tk.W)
    length_var = tk.IntVar(value=8)
    length_entry = ttk.Entry(main_frame, textvariable=length_var)
    length_entry.grid(column=1, row=0)
    length_entry.focus()

    letters_var = tk.BooleanVar(value=True)
    letters_checkbox = ttk.Checkbutton(main_frame, text="Include letters", variable=letters_var)
    letters_checkbox.grid(column=0, row=1, columnspan=2, sticky=tk.W)

    numbers_var = tk.BooleanVar(value=True)
    numbers_checkbox = ttk.Checkbutton(main_frame, text="Include numbers", variable=numbers_var)
    numbers_checkbox.grid(column=0, row=2, columnspan=2, sticky=tk.W)

    symbols_var = tk.BooleanVar(value=True)
    symbols_checkbox = ttk.Checkbutton(main_frame, text="Include symbols", variable=symbols_var)
    symbols_checkbox.grid(column=0, row=3, columnspan=2, sticky=tk.W)

    generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_and_copy_password)
    generate_button.grid(column=0, row=4, columnspan=2, pady=10)

    root.mainloop()

# Entry Point for the Program
def main():
    """Entry point for the password generator program."""
    choice = input("Choose mode (CLI or GUI): ").strip().lower()

    if choice == "cli":
        cli_main()
    elif choice == "gui":
        gui_main()
    else:
        print("Invalid choice. Please choose either 'CLI' or 'GUI'.")

if __name__ == "__main__":
    main()
