import tkinter as tk
from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename(title='Open file', filetypes=[('All Files', '*.*')])

    if file_path:
        print(f'Selected file {file_path}')
    else:
        print('No file selected')
        return None

# Create window
root = tk.Tk()
root.withdraw() # Hide root window

selected_file_path = select_file()

if selected_file_path: # Check if a file was selected
    print(f'The file path is stored in the variable: {selected_file_path}')

    try:
        with open(selected_file_path, 'r') as test_file:
            for line in test_file:
                print(line.strip())
    except Exception as e:
        print(f"Error reading the file: {e}")

    else:
        print('No file was selected')



