# AI Privacy Guardian 🛡️

A desktop security application that automatically protects your screen when another person is detected behind you. Uses computer vision to detect human faces via camera and triggers a privacy action to hide your desktop — preventing shoulder-surfing and accidental exposure of sensitive information.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-Educational-orange)

Built for students, developers, and privacy-focused users who want to prevent unauthorized viewing of their screen while working.

## 📸 Demo
<img width="397" height="402" alt="image" src="https://github.com/user-attachments/assets/99099c03-5cbd-4e11-b090-a3f680978861" />


## 🔥 Features

- 👁️ **Real-time face detection** using OpenCV
- 🔒 **Automatic desktop privacy mode** when an unauthorized face is detected
- ⏱️ **Cooldown timer** to prevent repeated triggers
- ⚙️ **Adjustable detection settings**
- 🖥️ **Graphical User Interface (GUI)** for easy control
- 📌 **Background system tray mode**
- 🚫 **Ignore zone support** to filter out specific areas of the frame
- 🎥 **External USB camera compatibility**
- 📦 **Standalone `.exe`** build support (no Python install needed to run)

## 🎯 How It Works

The system continuously monitors a camera feed and analyzes each frame using a Haar Cascade face detection model. When a face is detected outside the defined ignore zone, the program activates privacy mode.

**Workflow:**
1. Start detection from the GUI
2. Camera feed begins scanning for faces in real time
3. If a face is detected outside the ignore zone (i.e., a second person behind the user)
4. Privacy mode activates — desktop is minimized
5. A cooldown timer prevents the action from re-triggering immediately

## 🛠 Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.8+ |
| Computer Vision | OpenCV (Haar Cascade classifier) |
| Automation | PyAutoGUI |
| System Tray Integration | PyStray, Pillow |
| Packaging | PyInstaller |

## 📁 Project Structure


## 🚀 Installation & Usage

### Prerequisites
- Python 3.8+
- A webcam or external USB camera

### Setup

```bash
# Clone the repository
git clone https://github.com/Anand8973/AI-Privacy-Guardian.git
cd AI-Privacy-Guardian

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

The GUI will open, where you can start or stop the detection system.

### Building a Standalone `.exe`

```bash
pip install pyinstaller

pyinstaller --onefile --noconsole --add-data "haarcascade_frontalface_default.xml;." main.py
```

The executable will be generated in the `dist/` folder.

## 💡 Use Cases

- Privacy protection in shared or public workspaces
- Secure work environments handling sensitive data
- Content creators protecting on-screen information during recording
- Demonstration project for computer vision coursework

## 🔮 Future Improvements

- [ ] Replace Haar Cascade with a deep learning-based human detector for improved accuracy
- [ ] Add face recognition to distinguish and ignore the primary user
- [ ] Screen blur as an alternative to minimizing applications
- [ ] Mobile/desktop notification on detection
- [ ] Multi-camera support

## 📄 License

This project is open source and available for educational and research purposes.

## 👤 Author

**Anand Arya**
- GitHub: [@Anand8973](https://github.com/Anand8973)
- LinkedIn: [Anand Arya](https://www.linkedin.com/in/anand-arya-27b260368/)
