import time, sys

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

typewriter("Bingo Bango Tralala... \n")


from ascii_magic import AsciiArt
from PIL import Image

Claw = Image.open("/workspaces/Computer-Programming-2/image copy 3.png")

ascii_art = AsciiArt.from_pillow_image(Claw)
ascii_art.to_terminal()

#Blurb /workspaces/Computer-Programming-2/image copy.png
#Zoe /workspaces/Computer-Programming-2/image.png
# Bobidilo /workspaces/Computer-Programming-2/image copy 2.png

