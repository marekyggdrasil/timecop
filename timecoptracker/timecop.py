import time
import sys

from watchdog.observers import Observer
from pynput.keyboard import Key, Listener

def show(key):
    if key == Key.esc:
        sys.stdout.write((b'\x08' * 1).decode())
        print('a')

def backline():
    print('\r', end='')

def main():
    observer = Observer()
    try:
        with Listener(on_press = show) as listener:
            observer.start()
            for i in range(10):
                text = 'timecop ' + str(i)
                print(text, end='', flush=True)
                time.sleep(1)
                backline()
            print(text, end='', flush=True)
            print()
    except KeyboardInterrupt:
        print('you interrupted!')
        observer.stop()
