import tkinter as tk
from tkinter import ttk
import pyautogui
import keyboard

def on_key_press(event):
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt'):
        x, y = pyautogui.position()
        label.config(text=f'Mouse position: x={x}, y={y}')

def monitor_mouse_position():
    root = tk.Tk()
    root.title("Mouse Position Tracker")
    root.geometry("300x100")

    style = ttk.Style()
    style.theme_use('arc')

    global label
    label = ttk.Label(root, text="Press Ctrl + Alt to get mouse position")
    label.pack(pady=10)

    keyboard.on_press(on_key_press)

    root.mainloop()

if __name__ == "__main__":
    monitor_mouse_position()