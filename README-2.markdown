# Keylogger Program

This is a simple keylogger program that logs keystrokes to a file (`keytext.txt`) and uploads it to Google Drive.

## Requirements
- Python 3.x
- `pynput` library (`pip install pynput`)
- `pydrive` library (`pip install pydrive`)
- Google Drive API credentials (set up via Google Cloud Console)

## Setup
1. Install required libraries:
   ```bash
   pip install pynput pydrive
   ```
2. Configure Google Drive API:
   - Create a project in Google Cloud Console.
   - Enable the Google Drive API.
   - Download the credentials JSON file and place it in the project directory.
   - Update `pydrive` settings to use the credentials file (refer to PyDrive documentation).

## Usage
1. Run the program:
   ```bash
   python keylogger.py
   ```
2. The program will log all keystrokes to `keytext.txt`.
3. Press `Enter` to stop the keylogger and upload `keytext.txt` to Google Drive.

## Features
- Logs all key presses, including special keys (e.g., Shift, Ctrl).
- Saves logs to `keytext.txt` in the project directory.
- Uploads the log file to Google Drive upon stopping the program.

## Notes
- Ensure you have proper permissions for Google Drive API access.
- Use responsibly and only with explicit consent from users whose keystrokes are being logged.