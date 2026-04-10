import pyautogui
import time
import threading
from pynput import keyboard

# Configure key press interval (seconds)
click_interval = 16
clicking = False

# Function to press the 'R' key
def press_r_key():
    global clicking
    while clicking:
        pyautogui.press('r')
        time.sleep(click_interval)

# Function to start and stop key pressing
def toggle_clicking(key):
    global clicking
    if key == keyboard.Key.f6:
        if not clicking:
            clicking = True
            click_thread = threading.Thread(target=press_r_key)
            click_thread.start()
        else:
            clicking = False
    elif key == keyboard.Key.esc:
        return False  # Stop listener

# Setting up key listener
with keyboard.Listener(on_press=toggle_clicking) as listener:
    listener.join()
