import time, sys

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

typewriter("My name is Simon Claw... \n")


from ascii_magic import AsciiArt
from PIL import Image

Claw = Image.open("/workspaces/Computer-Programming-2/simonclaw.jpeg")

# Convert to ASCII and print to terminal
ascii_art = AsciiArt.from_pillow_image(Claw)
ascii_art.to_terminal()

#Blurb /workspaces/Computer-Programming-2/image copy.png
#Zoe /workspaces/Computer-Programming-2/image.png


