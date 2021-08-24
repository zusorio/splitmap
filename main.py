import keyboard
from inputs import get_gamepad

print("Started up")

while True:
    events = get_gamepad()
    for event in events:
        if event.code == "BTN_TR":
            if event.state == 1:
                keyboard.press("e")
            else:
                keyboard.release("e")
        elif event.code == "BTN_TL":
            if event.state == 1:
                keyboard.press("q")
            else:
                keyboard.release("q")
