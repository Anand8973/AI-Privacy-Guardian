import cv2
import pyautogui
import tkinter as tk
from tkinter import ttk
import threading
import time
import os
import pystray
from PIL import Image, ImageDraw

# ---------------- SETTINGS ----------------
camera_index = 0   # Change if needed
cooldown_time = 5
last_trigger_time = 0
detection_running = False
privacy_mode = "Minimize"

# Define Ignore Zone (Adjust After Testing)
ignore_zone = (300, 100, 760, 450)

# ---------------- PRIVACY FUNCTION ----------------
def activate_privacy():
    if privacy_mode == "Minimize":
        pyautogui.hotkey('win', 'd')
    elif privacy_mode == "Lock":
        pyautogui.hotkey('win', 'l')
    elif privacy_mode == "Notepad":
        os.startfile("notepad.exe")

# ---------------- DETECTION FUNCTION ----------------
def start_detection():
    global detection_running, last_trigger_time
    
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    while detection_running:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5), 0)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=7,
            minSize=(60, 60)
            )

        trigger = False

        for (x, y, w, h) in faces:
            face_center_x = x + w // 2
            face_center_y = y + h // 2

            x1, y1, x2, y2 = ignore_zone

            # Draw face box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Ignore zone check
            if not (x1 < face_center_x < x2 and y1 < face_center_y < y2):
                trigger = True
                break

        # Draw Ignore Zone
        x1, y1, x2, y2 = ignore_zone
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        if trigger:
            status_label.config(text="HUMAN DETECTED", fg="red")
            current_time = time.time()
            if current_time - last_trigger_time > cooldown_time:
                activate_privacy()
                last_trigger_time = current_time
        else:
            status_label.config(text="SAFE", fg="green")

        cv2.imshow("Camera View", frame)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()

# ---------------- GUI FUNCTIONS ----------------
def start_button():
    global detection_running
    detection_running = True
    thread = threading.Thread(target=start_detection)
    thread.daemon = True
    thread.start()

def stop_button():
    global detection_running
    detection_running = False

def update_cooldown(val):
    global cooldown_time
    cooldown_time = int(val)

def update_privacy_mode(event):
    global privacy_mode
    privacy_mode = dropdown.get()

# ---------------APP TRAY DESIGN ----------------
def create_tray_icon():

    image = Image.new('RGB', (64, 64), color='black')
    draw = ImageDraw.Draw(image)
    draw.rectangle((16,16,48,48), fill='white')

    menu = pystray.Menu(
        pystray.MenuItem('Show', show_window),
        pystray.MenuItem('Exit', quit_app)
    )

    icon = pystray.Icon("PrivacySystem", image, "Privacy System", menu)
    icon.run()
def show_window(icon, item):
    root.after(0, root.deiconify)
def quit_app(icon, item):
    icon.stop()
    root.destroy()
def minimize_to_tray():
    root.withdraw()
    threading.Thread(target=create_tray_icon).start()
# ---------------- GUI DESIGN ----------------
root = tk.Tk()
root.title("AI Privacy Protection System")
root.geometry("400x350")

title = tk.Label(root, text="Face Detection Privacy System", font=("Arial", 14))
title.pack(pady=10)

status_label = tk.Label(root, text="SAFE", font=("Arial", 16), fg="green")
status_label.pack(pady=10)

start_btn = tk.Button(root, text="Start Detection", command=start_button)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop Detection", command=stop_button)
stop_btn.pack(pady=5)

tray_btn = tk.Button(root, text="Minimize to Tray", command=minimize_to_tray)
tray_btn.pack(pady=5)

cooldown_label = tk.Label(root, text="Cooldown (seconds)")
cooldown_label.pack()

cooldown_slider = tk.Scale(root, from_=5, to=60, orient="horizontal",
                           command=update_cooldown)
cooldown_slider.set(15)
cooldown_slider.pack()

dropdown = ttk.Combobox(root, values=["Minimize", "Lock", "Notepad"])
dropdown.current(0)
dropdown.bind("<<ComboboxSelected>>", update_privacy_mode)
dropdown.pack(pady=10)

root.mainloop()