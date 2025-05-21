import requests
from ascii_magic import AsciiArt
from PIL import Image as PILImage

# URL of the banana file from gist
url = "https://gist.githubusercontent.com/Ge0rge-K/eef9e819cf48967af85f60de5b8ba5da/raw/"

# Fetch the raw content of the Gist
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the content as text
    data = response.text
    print("Running remote code from Gist...")
    
    # Execute the fetched code (caution: ensure this Gist is trusted)
    exec(data)
    
else:
    print(f"Failed to fetch Gist. Status code: {response.status_code}")
