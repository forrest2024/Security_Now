import os
import requests
from bs4 import BeautifulSoup
import re

# URL of the webpage containing the names in <b> tags
webpage_url = "https://www.grc.com/sn/past/2005.htm"

# Directory containing the downloaded MP3 files
folder = os.path.expanduser("~/Desktop/SecurityNow")

# Fetch and parse the webpage
response = requests.get(webpage_url)
response.raise_for_status()  # Ensure the request was successful
soup = BeautifulSoup(response.text, "html.parser")

# Extract names from <b> tags (adjust selector if needed)
names = []
for td_tag in soup.find_all("td", colspan="6"):
    font_size_1 = td_tag.find("font", size="1")
    if font_size_1:
        font_size_2 = font_size_1.find("font", size="2")
        if font_size_2:
            b_tags = font_size_2.find_all("b")
            names.extend([b_tag.get_text(strip=True) for b_tag in b_tags])
names.reverse()

# Function to sanitize file names by removing invalid characters
def sanitize_filename(filename):
    # Invalid characters for Windows filenames
    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'
    return re.sub(invalid_chars, "", filename)

# Rename MP3 files in the directory
for filename in os.listdir(folder):
    if filename.endswith(".mp3"):
        # Extract episode number from the filename (e.g., "sn-0001.mp3")
        episode_number = filename.split("-")[1].split(".")[0]

        # Ensure we have a name corresponding to the episode
        try:
            episode_index = int(episode_number) - 1  # Assuming episode numbers start from 1
            new_name = f"sn-{episode_number} - {names[episode_index]}.mp3"
        except (IndexError, ValueError):
            print(f"No name found for {filename}. Skipping...")
            continue

        # Sanitize the new file name to avoid invalid characters
        sanitized_name = sanitize_filename(new_name)

        # Rename the file
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, sanitized_name)
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {sanitized_name}")
        except Exception as e:
            print(f"Failed to rename {filename}: {e}")

print("Renaming complete!")
