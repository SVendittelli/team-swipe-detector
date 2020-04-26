import sys
from pynput.keyboard import Key, KeyCode, Listener

listen = False

def on_press(key):
    if key == Key.esc:
        sys.exit()
    if matches_character(key, 'l'):
        toggle_listening()
    if listen:
        print(f'recorded: {key}')

def matches_character(key, character):
    return key == KeyCode.from_char(character)

def exit():
    sys.exit()

def toggle_listening():
    global listen
    listen = not listen
    print(f'listening: {listen}')

def start_detector(start_listening=False):
    global listen
    listen = start_listening
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    start_detector()
