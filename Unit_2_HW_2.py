import time, sys

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 

typewriter(n/"My name is luis yabadabadoo.")
time.sleep(2)
typewriter(n/"I will run sawyers fade...")
time.sleep(1)
typewriter(n/"He should have never cut his steak...")
time.sleep(2)
typewriter("Now he will pay the rizzy price..")


from ascii_magic import AsciiArt
from PIL import Image
Luis = Image.open("/workspaces/Computer-Programming-2/717CFA3F-B213-4ED5-8961-DA912997832A_1_105_c.jpeg")
ascii_art = AsciiArt.from_pillow_image(Luis)
ascii_art.to_terminal()
