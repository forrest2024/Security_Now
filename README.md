Tools to scrape old SN episodes and add descriptive names to each. MP3 title metadata is a bit spotty from Twit, so I found it cleaner to scrape the names from the HTML on the page for each year of podcasts. I couldn't figure out how to do all episodes unfortunately, but hopfully this will help you save a lot of time anyways. 

Use sn_downloader.py to grab episodes on each page and store appropriately named directories. 

After you've downloaded desired episodes, run sn_renamer.py, changing the webpage_url to the appropriate path for the year of the folder you're trying to rename. You'll also want to modify the folder variable obviously. 

Shoutout to Recovery9787 who did this with wget. For some reason I couldn't get wget to work. ChatGPT suggested the requests library, so we kinda of went from there. 

