import csv
import random
import string
import tkinter as tk
from tkinter import filedialog

def generate_password(length=12):
    """Generate a random password of specified length."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for i in range(length))

def create_users(num_users):
    """Create a list of users with unique passwords."""
    return [("user" + str(i + 1), generate_password()) for i in range(num_users)]

def export_to_csv(users, filename):
    """Export user data to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Password"])
        writer.writerows(users)

def save_file_gui():
    """Open a save file dialog."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    root.destroy()
    return file_path

def main():
    try:
        num_users = int(input("Enter the number of users to create: "))
        output_file = save_file_gui()
        if not output_file:  # Check if the user cancelled the save dialog
            print("File save cancelled.")
            return
        users = create_users(num_users)
        export_to_csv(users, output_file)
        print(f"Generated {num_users} users and exported to '{output_file}'.")
    except ValueError:
        print("Please enter a valid integer for the number of users.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
