# Discord React Bot
Have you ever wanted to express how deeply you appreciate your friends? 
This tool helps you to do it in the original way! 
Imagine your friend waking up and seeing all of their messages 
covered with the selected emojis, just like this:

![alt text](https://github.com/savkorlev/discord_reactbot/blob/main/cutie.png?raw=true)

How cute! :3

## Prerequisites
This script uses the Chrome browser together with its driver.
The archive includes the driver but Chrome itself must be installed separately. 
The driver and Chrome versions must match in order for the script to run.
The script was tested on the attached driver version 100.0.4896.60 that supports Chrome version 100.
The newest driver can also be downloaded separately from the 
official website: [ChromeDriver](https://chromedriver.storage.googleapis.com/index.html).

[Python 3](https://www.python.org/) is required to run the script.

[Selenium](https://www.selenium.dev/) is the only additional module that is 
used in the script. If you have Selenium installed you can skip the setting 
up step.

## Setting up

### Installing the modules
Open the Windows Command Prompt and type in:
```python
cd "path/to/a/script/folder"
pip install -r requirements.txt
```

### Adding the required emojis to favourites
To insure that the script is running correctly you need to add all the 
emojis you want to put to favourites in discord. To do that right click 
the emoji and click "add to favourites".

## Running the script
After the set up is done, type in:
```python
python main.py
```

## Remarks and limitations

### First
Limitations, extensions and improvements potential: Check the TODOs.

### Second
Current precision level for sleeping time is 0.5 seconds. 
Current step is 1.5 seconds.
