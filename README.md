# AI Privacy Guardian

AI Privacy Guardian is a desktop security system that automatically protects your screen when another person is detected behind you. The application uses computer vision to detect human faces through an external camera and triggers a privacy action to hide your desktop.

This project is designed for students, developers, and privacy-focused users who want to prevent shoulder-surfing or accidental exposure of sensitive information while working on a computer.

---

## Features

• Real-time face detection using OpenCV
• Automatic desktop privacy mode when a face is detected
• Cooldown timer to prevent repeated triggers
• Adjustable detection settings
• Graphical User Interface (GUI) for easy control
• Background system tray mode
• Ignore zone support for filtering specific areas
• External USB camera compatibility
• Works as a standalone `.exe` application

---

## How It Works

The system continuously monitors a camera feed and analyzes each frame using a face detection model. When a face is detected outside the defined ignore zone, the program activates privacy mode by hiding the desktop.

Typical workflow:

1. Start detection from the GUI
2. Camera feed begins scanning for faces
3. If another person appears behind the user
4. Privacy mode activates (desktop is minimized)
5. Cooldown timer prevents repeated triggering

---

## Project Structure

AI-Privacy-Guardian

main.py – Main application logic
haarcascade_frontalface_default.xml – Face detection model
README.md – Project documentation
requirements.txt – Python dependencies

---

## Installation

Clone the repository:

git clone https://github.com/yourusername/AI-Privacy-Guardian.git

Move into the project folder:

cd AI-Privacy-Guardian

Install required dependencies:

pip install -r requirements.txt

---

## Running the Application

Run the main script:

python main.py

The GUI will open where you can start or stop the detection system.

---

## Creating the EXE File

Install PyInstaller:

pip install pyinstaller

Build the executable:

pyinstaller --onefile --noconsole --add-data "haarcascade_frontalface_default.xml;." main.py

The executable will be generated in the `dist` folder.

---

## Requirements

Python 3.8+

Required libraries:

OpenCV
PyAutoGUI
PyStray
Pillow

---

## Future Improvements

Possible upgrades for the project:

• Human detection using deep learning models
• Face recognition to ignore the primary user
• Screen blur instead of minimizing applications
• Mobile notification when someone is detected
• Multi-camera support

---

## Use Cases

• Privacy protection in public workspaces
• Secure work environments
• Content creators protecting sensitive information
• Demonstration project for computer vision courses

---

## License

This project is open source and available for educational and research purposes.

---

## Author

Anand Arya
B.Tech Computer Science Engineering
