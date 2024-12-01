from pynput import keyboard
import popup

def on_press(key):
    try:
        if key == keyboard.Key.f7:
            result = popup.pop_up()
            print(f'Resultatul pop-up-ului: {result}')
    except AttributeError:
        pass

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
