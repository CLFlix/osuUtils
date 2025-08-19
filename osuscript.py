import time
import shutil
import psutil
import subprocess

import utils
from utils import log

process_names = ['osu!StreamCompanion.exe', 'KeyOverlay.exe', 'OpenTabletDriver.UX.Wpf.exe', 'obs64.exe', 'osuTwitchBot.exe']

def copy_files(source, destination, amount, file_type):
    src = source
    dest = destination
    
    if amount == 1:
        log(f'Copying file...')
        shutil.copy(src, f"{dest}.{file_type}")
        log(f'Copied file')
        return

    log(f'Copying files {amount} times...')
    for i in range(amount):
        shutil.copy(src, f"{dest}-{i}.{file_type}")
    log('Copied files')

def run_stream_tools():
    log('Starting tools...')

    for app in utils.applications:
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

def show_config():
    result = ""
    for app, path, in utils.config.items():
        result += f'{app}: {path}\n'
    
    return result