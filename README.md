# osuUtils!

## Functionality

### Configure file paths

If it's the first time you run the program, this will be the first thing you will be confronted with. It will ask you for the file paths of OpenTabletDriver, StreamCompanion, KeyOverlay and OBS. **IMPORTANT**: These have to be the **shortcuts** of the programs, not the actual `.exe` themselves. Also, just provide the raw file address, not with the `""` around it. These quotation marks will automatically be added to the path if you copy them from your file explorer. If you don't have one of the apps that it asks you to add, or you simply don't want to add them in the program, just leave the field empty and press Enter.

If you want to change these paths (maybe because you've moved the shortcuts), you can simply go into the `config.json` that has been made in the same directory as the `.exe` and change the file paths.

### Copy files

If you choose for this option, the program will ask you for the **full** path to the file you want to copy (1). After that, it will ask you to enter the **full** path and the **base name** of the copied file (2). With this version, you can now choose what file type you're copying as well (3). After providing the app how many copies you want (4), it will generate copies of the file for the amount you requested. If you only wanted one file, the copied file's name should be the same as your original file.

Example:

1. `C:\Users\User\Documents\file.png`
2. `C:\Users\User\Documents\copied_files\base_name`
3. `png`
4. 100
5. `C:\Users\User\Documents\copied_files\base_name-0.png` all the way to `C:\Users\User\Documents\copied_files\base_name-99.png`

### Start Stream Tools

This will try to start all the applications you provided in the configuration. It will also tell you what application it's trying to start up, so you can keep track of what's happening.

### Close Stream Tools

This will check if any of the previously mentioned applications are running, and try to close them. Attention with OBS: a close with this program goes through Task Manager. This means OBS will close and detect it as a crash, so next time you start up it will probably say it didn't close correctly. This should normally not be a problem and you should just let it run normally, but if you're scared of losing anything, simply don't use this feature.
