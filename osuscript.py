import os
import json
import time
import shutil
import psutil
import subprocess
from datetime import datetime

process_names = ['osu!StreamCompanion.exe', 'KeyOverlay.exe', 'OpenTabletDriver.UX.Wpf.exe', 'obs64.exe']

log_file = r'log.txt'
CONFIG_FILE = r'config.json'

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
        config = json.load(settings)

    global applications
    applications = [value for value in config.values() if value]
    log("Loaded settings~~")

def create_clean_log_file():
    with open(log_file, 'w') as log:
        log.write("")

def log(message):
    print(message)
    with open(log_file, 'a') as log:
        log.write(f'{datetime.now()} --- {message}\n')

def copy_files(source, destination, amount, file_type):
    src = source
    dest = destination
    
    if amount == 1:
        log(f'Copying file...')
        shutil.copy(src, dest + f".{file_type}")
        log(f'Copied file')
        return

    log(f'Copying files {amount} times...')
    for i in range(amount):
        shutil.copy(src, dest + f"-{i}.{file_type}")
    log('Copied files')

def run_stream_tools():
    log('Starting tools...')

    for app in applications:
        log(f'Starting {app}')
        subprocess.Popen(['explorer', app])
        time.sleep(1)
    
    log('Stream tools running.')

def close_stream_tools():    
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'] in process_names:
                log(f'Closing {process.info['name']}')
                process.terminate()
                process.wait(timeout=1)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            log(f"[Error: Couldn't close process. {process.info['name']} is either not running or access has been denied. Aborting further operations.")
            return
    
    log('Closed all processes')


def main():
    # create or clean log file for new session
    create_clean_log_file()
    log('Script running~~')

    if is_first_time_run():
        print("First time setup")
        create_settings_file()

    load_config()
            
    run = True
    while run:
        print("1. Copy files")
        print("2. Run osu!stream tools")
        print("3. Close osu!stream tools")
        print("0. Quit\n")
        choice = int(input("What operation do you want to do?\n"))

        if choice == 0:
            log('Quitting script~~')
            run = False
            
        elif choice == 1:
            src = input("File that needs to be copied [Full path]\n")
            dest = input("Location & file base name [Full path]\n")
            file_type = input("What type of file do you want to copy? (txt, png, jpg,...)\n")
            amount = int(input("Amount of copies\n"))

            copy_files(src, dest, amount, file_type)
            time.sleep(2)

        elif choice == 2:
            run_stream_tools()
            time.sleep(2)

        elif choice == 3:
            close_stream_tools()
            time.sleep(2)

        else:
            print("Invalid choice. Please try again.")

main()
