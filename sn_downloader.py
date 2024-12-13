import os
import requests

# Prompt the user for the starting and ending episode numbers
s = input("Episode Start Number (4 digits): ")
e = input("Episode End Number (4 digits): ")

# Create a folder to store the downloaded files (on the desktop)
folder = os.path.expanduser("~/Desktop/SecurityNow") # UPDATE TO YEAR
os.makedirs(folder, exist_ok=True)

# Download the files
current = int(s)
while current <= int(e):
    current_string = f"{current:04d}"
    episode_url = f"https://media.grc.com/sn/sn-{current_string}.mp3"
    try:
        # Follow redirects and download file
        response = requests.get(episode_url, stream=True, allow_redirects=True)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Save the file
        file_path = os.path.join(folder, f"sn-{current_string}.mp3")
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Episode {current_string} downloaded successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download Episode {current_string}: {e}")
    current += 1

# Show a message that the download is complete
print("\nDownload complete. Please check your desktop for a directory named 'SecurityNow' containing the downloaded episodes.")

input("Press enter to exit")
