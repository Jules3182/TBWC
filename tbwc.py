from distutils import command
from operator import truediv
import subprocess
from subprocess import Popen, PIPE, call
from datetime import time, timedelta
from datetime import datetime
import os, random
from pathlib import Path


##### Main script for changing you wallpaper on Linux using Variety #####


### setting up variables

    #the "here and now" vars
HERE = Path(__file__).parent
NOW = datetime.now()
CURRENT_WP = ""

    #morning vars
morning_time = NOW.replace(hour=6, minute=0, second=0, microsecond=0)
morning_path = HERE / 'morning'
morning_files = list(morning_path.rglob("*.jpg"))
isMorning = False

    #day vars   
day_time = NOW.replace(hour=12, minute=0, second=0, microsecond=0)
day_path = HERE / 'day'
day_files = list(day_path.rglob("*.jpg"))
isDay = False

    #night vars
night_time = NOW.replace(hour=19, minute=0, second=0, microsecond=0)
night_path = HERE / 'night'
night_files = list(night_path.rglob("*.jpg"))
isNight = False


## Debug prints to test vars (ignore this if actually using it)
def debug():
    print("##### DEBUG INFO #####")
    print("Dirrectory: ", os.getcwd())
    print("Current Time: ", NOW)
    print("Morning Time: ", morning_time)
    print("Day Time: ", day_time)
    print("Night Time: ", night_time)
    print("Morning Path: ", morning_path)
    print("Day Path: ", day_path)
    print("Night Path: ", night_path)
    print("Random file from day path: ",  random.choice(day_files))


## check current time and set bools acordingly
def check_time():
    if NOW > morning_time and NOW < day_time:
        isMorning = True
        isNight = False
        print("It is morning")
    elif NOW > day_time and NOW < night_time:
        isDay = True
        isMorning = False
        print("It is day")
    else:
        isNight = True
        isDay = False
        print("It is night")

## updates all the wallpaper vars for each time of day
def update_wp():
    if isMorning:
        CURRENT_WP = random.choice(morning_files)    
    elif isDay:
        CURRENT_WP = random.choice(day_files)
    else:
        CURRENT_WP = random.choice(night_files)
    updatecmd = "variety " + str(CURRENT_WP) + " --next"
    ## set wallpaper with console command
    print("The Current WallPaper: ", CURRENT_WP)
    subprocess.run([updatecmd, "-c", "command -v yes"])
    #com = 'variety ' + CURRENT_WP + ' --next'
    #p = subprocess.Popen([updatecmd], shell=True)
    #os.popen(updatecmd).read()
    #call(updatecmd)
    #os.system(updatecmd)


check_time()
debug()
update_wp()