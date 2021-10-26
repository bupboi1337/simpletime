# This is a GplV3 licenced program

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M")
def time():
    print('The time is:', current_time)
