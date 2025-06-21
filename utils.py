import os
import json
from datetime import datetime

log_file = r'log.txt'
CONFIG_FILE = r'config.json'

def create_clean_log_file():
    with open(log_file, 'w') as log:
        log.write("")

def log(message):
    print(message)
    with open(log_file, 'a') as log:
        log.write(f'{datetime.now()} --- {message}\n')

def is_first_time_run():
    return not os.path.exists(CONFIG_FILE)

def create_settings_file():
    open_tablet_driver = input("What is the full path to the OpenTabletDriver shortcut? Leave open if you don't have this.\n")
    stream_companion = input("What is the full path to the StreamCompanion shortcut? Leave open if you don't have this.\n")
    key_overlay = input("What is the full path to the KeyOverlay shortcut? Leave open if you don't have this.\n")
    obs = input("What is the full path to the OBS shortcut? Leave open if you don't have this.\n")

    config = {
        "OpenTabletDriver": open_tablet_driver,
        "StreamCompanion": stream_companion,
        "KeyOverlay": key_overlay,
        "OBS": obs
    }

    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file, indent=4)

def load_config():
    with open(CONFIG_FILE, 'r') as settings:
        global config
        config = json.load(settings)

    global applications
    applications = [value for value in config.values() if value]
    log("Loaded settings~~")

