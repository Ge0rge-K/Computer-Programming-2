import os
import requests
import subprocess
import sys

def install_requirements():
    """Install required Python libraries."""
    print("Installing required libraries...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def download_image(image_url, image_path):
    """Download the image if it doesn't exist."""
    if not os.path.exists(image_path):
        print(f"Downloading image from {image_url}...")
        response = requests.get(image_url)
        with open(image_path, 'wb') as f:
            f.write(response.content)
        print(f"Image saved to {image_path}")
    else:
        print(f"Image already exists at {image_path}")

def run_program(image_path):
    """Run the main program (convert image to ASCII art)."""
    from ascii_magic import AsciiArt
    from PIL import Image as PILImage
    
    # Load the image
    img = PILImage.open(image_path)
    
    # Convert the image to ASCII art
    ascii_art = AsciiArt.from_pillow_image(img)
    
    # Print the ASCII art to the terminal
    ascii_art.to_terminal()

def main():
    image_url = "https://example.com/banana.png"  # Replace with actual image URL if needed
    image_path = "banana.png"  # Local path for the image

    # Step 1: Install required libraries
    install_requirements()

    # Step 2: Download the image if not exists
    download_image(image_url, image_path)

    # Step 3: Run the main program
    run_program(image_path)

if __name__ == "__main__":
    main()
