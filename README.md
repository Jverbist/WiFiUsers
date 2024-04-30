# WiFiUsers

# User and Password Generator Script

This Python script allows you to generate a specified number of user accounts, each with a unique, secure random password. The script outputs the usernames and passwords to a CSV file, making it easy to handle large numbers of user credentials securely and efficiently.

## Features

- **User Input for Quantity**: Allows the user to specify the number of accounts to be generated.
- **Random Password Generation**: Generates strong passwords containing letters, numbers, and special characters.
- **CSV Output**: Exports usernames and passwords to a CSV file for easy use and integration with other systems.

## Prerequisites

To run this script, you will need Python installed on your system. The script is compatible with Python 3.6 and newer versions. No external Python packages are required as it uses built-in libraries only.

## Installation

No installation is necessary. Just ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Download the Script**: Download the `user_generator.py` script to your local machine.
2. **Open a Terminal**: Open a terminal window or command prompt.
3. **Navigate to the Script Location**: Use the `cd` command to change the directory to where you have saved `user_generator.py`.
4. **Run the Script**: Type the following command and press Enter:
```bash
python user_generator.py

```
5. **Enter the Number of Users**: When prompted, enter the number of users you wish to generate and press Enter.
6. **Check the Output**: After the script runs, it will generate a file named `users.csv` in the same directory containing the usernames and passwords.

## Output Format

The generated CSV file will have the following format:

Username,Password
user1,Abcd!2349@#$
user2,XYZ!9876#$%
...


## Customization

You can customize the script to change the password length or the naming scheme of the users by modifying the `generate_password` and `create_users` functions.

## Troubleshooting

- **Invalid Number Input**: Ensure you enter a valid integer when prompted for the number of users.
- **Permission Issues**: If the script cannot write the CSV file, check the directory permissions.

## License

This script is provided "as is", without warranty of any kind. Feel free to modify and use it as needed.

