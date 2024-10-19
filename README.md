# QueryIDExtractor

QueryIDExtractor is a Python script that uses the Telegram API to manage Telegram sessions and extract `query_id` from URLs.

# Watch Video Tutorial
[Click Here](https://youtu.be/JY0ER5FqHEc)

## Requirements

- Python 3.7 or higher
- `telethon` package

## Installation and Running

### Windows

1. **Install Python**:
   - Download and install Python from the [official Python website](https://www.python.org/downloads/).

2. **Install Required Packages**:
   - Open Command Prompt and run:
     ```bash
     pip install telethon
     ```

3. **Run the Script**:
   - Navigate to the script's directory and run:
     ```bash
     python Query.py
     ```

### Mac

1. **Install Python**:
   - Python usually comes pre-installed on macOS. If not, you can download it from the [official Python website](https://www.python.org/downloads/).

2. **Install Required Packages**:
   - Open Terminal and run:
     ```bash
     pip install telethon
     ```

3. **Run the Script**:
   - Navigate to the script's directory and run:
     ```bash
     python Query.py
     ```

### Linux

1. **Install Python**:
   - Install Python using your distribution's package manager. For example:
     ```bash
     sudo apt-get update
     sudo apt-get install python3 python3-pip
     ```

2. **Install Required Packages**:
   - Open Terminal and run:
     ```bash
     pip3 install telethon
     ```

3. **Run the Script**:
   - Navigate to the script's directory and run:
     ```bash
     python3 Query.py
     ```

### Termux

1. **Install Termux**:
   - Install [Termux](https://termux.com/) from the Google Play Store or F-Droid.

2. **Install Python**:
   - Open Termux and run:
     ```bash
     pkg update
     pkg install python
     ```

3. **Install Required Packages**:
   - Run the following command in Termux:
     ```bash
     pip install telethon
     ```

4. **Run the Script**:
   - Navigate to the script's directory and run:
     ```bash
     python Query.py
     ```

## Configuration

1. **Create `config.json`**:
   - Create a `config.json` file and add your `api_id` and `api_hash`:
     ```json
     {
       "api_id": "YOUR_API_ID",
       "api_hash": "YOUR_API_HASH"
     }
     ```

2. **Add a Session**:
   - Run the script and add a session using your phone number.

3. **Retrieve Data**:
   - Run the script to collect `query_id` from URLs using the Telegram bot.

## Contributing

If you encounter any issues or bugs, please open an issue or submit a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).
