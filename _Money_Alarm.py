import subprocess
import time
import winsound
import random
from winotify import Notification, audio


def is_vscode_running():
    output = subprocess.run(["tasklist"], capture_output=True, text=True)
    return "Code.exe" in output.stdout


def show_prompt():
    toast = Notification(
        app_id="Annoying Alarm by Bobby",
        title="Your Hourly Reminder to Code",
        msg="You need MONEY, now CODE",
        duration="long"
    )

    toast.show()
    audio_file = r"C:\Users\Juno\Documents\Python\Scripts\money_alarm.wav"
    winsound.PlaySound(audio_file, winsound.SND_FILENAME)


def get_random_time():
    HOUR = 3600
    return random.randint(HOUR/2, 2*HOUR)


while True:
    if not is_vscode_running():
        show_prompt()

    time.sleep(get_random_time())
