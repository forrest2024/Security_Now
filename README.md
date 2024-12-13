Tools to scrape old SN episodes and add descriptive names to each. MP3 title metadata is a bit spotty from Twit, so I found it cleaner to scrape the names from the HTML on the page for each year of podcasts. I couldn't figure out how to do all episodes at once unfortunately, but hopefully this will help you save a lot of time anyways. The renaming functionality will only work for an entire page as it's written so you'll have to download every episode for a given year to accurately title them. Feel free to modify, I'm sure there's a way to make it more selective. 

Use sn_downloader.py to grab episodes on each page and store in appropriately named directories. You'll be prompted to enter the start and end episode number as a four digit number. Make sure these selections line up with the numbers listed on the page for whatever year you want. For example, the episode numbers for the first year should line up with what's on this page: https://www.grc.com/sn/past/2005.htm. 

After you've downloaded desired episodes, run sn_renamer.py, changing the webpage_url variable to the appropriate path for the year of the folder containing the MP3s you're trying to rename. You'll also want to modify the folder variable to make sure you're modifying the names for only those episodes for the associated year. 




After this, you can load into whatever MP3 platform you wish. Should make it a lot easier to benefit from old episodes without having to constantly scroll to the very beginning on a tiny phone screen! 

Shoutout to Recovery9787 who did this with wget. For some reason I couldn't get wget to work. ChatGPT suggested the requests library, so I kinda went from there. 

**sn_renamer_practice.py doesn't work, as the name implies. sn_getter.py was an attempt with wget copied from Recovery9787. I wanted to preserve these anyways and was too lazy to make another branch ;). 

Thanks Steve and Leo for everything you do for the community!

