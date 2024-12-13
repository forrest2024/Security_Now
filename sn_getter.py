# Prompt the user for the starting and ending episode numbers
s = input("Episode Start Number (4 digits): ")
e = input("Episode End Number (4 digits): ")

# Create a folder to store the downloaded files (in the user's home directory)
import os
folder = os.path.expanduser("~/Desktop/SecurityNow")
os.makedirs(folder, exist_ok=True)

# Download the files and show a progress indicator
current = int(s)
while current <= int(e):
    current_string = f"{current:04d}"
    episode_url = f"https://media.grc.com/sn/sn-{current_string}.mp3"
    os.system(f"wget --no-check-certificate {episode_url} -P {folder}")
    print(f"Episode {current_string} downloaded")
    current += 1

# Show a message that the download is complete
print("\nDownload complete. Please check your desktop for a directory named 'SecurityNow' containing the downloaded episodes.")

input("Press enter to exit")