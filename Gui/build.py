import subprocess
import os
import sys
import time
import datetime

print("Start Builder")
while True:

    try:
        os.system("pyuic6 -o main_window_ui.py Main.ui")
        os.system("pyuic6 -o make_config_dia.py config.ui")
        os.system("pyuic6 -o alarm_task.py alarm_task.ui")
        print("Aktualisiert um "+time.strftime("%H:%M:%S"))
        time.sleep(120)
    except KeyboardInterrupt:
        print("Stop builder")
        sys.exit(0)
