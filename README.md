# Discord React Bot

## Prerequisites
[Python 3](https://www.python.org/) is needed to run the script.

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

## Running the software
After the set up is done, type in:
```python
python main.py
```

## Remarks and limitations

### First
While the script is running do not interact with the opened browser window 
in any way. The only exception is that you can minimize the browser window.
Any other interaction (including mouse movements) may cause errors.

### Second
Extensions and improvements: Check the TODOs.

### Third
To somehow bypass discord antispam systems the script uses time.sleep() 
together with randomly selected times to wait. Current precision level for 
time is 0.5 seconds. Current step is 1.0 seconds.
