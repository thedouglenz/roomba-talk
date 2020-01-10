from gpiozero import Button
import pygame
from time import sleep

BUTTON_PIN_IN = 11

SOUNDS = [
    "ohno.wav",
    "ouch.wav",
    "help.wav",
    "excuseme.wav",
    "darnit.wav"
]

def main():

    # Create a gpiozero Button instance
    button = Button(BUTTON_PIN_IN, pull_up=False)

    # Initialize pygame audio lib
    pygame.mixer.init()

    i = 0

    # Wait indefinitely for a button press
    while True:
        if button.is_pressed:
            # Play a sound
            pygame.mixer.music.load(SOUNDS[i])
            pygame.mixer.music.play()
            i = i + 1

        # 2 second pause between button presses
        sleep(2)


if __name__ == "__main__":
    main()
