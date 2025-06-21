from utils import *
from osuscript import *

def main():
    # create or clean log file for new session
    create_clean_log_file()
    log('Script running~~')

    if is_first_time_run():
        log("First time setup")
        create_settings_file()

    load_config()
    
    run = True
    while run:
        print("----------------------------------------")
        print("1. Copy files")
        print("2. Run osu!stream tools")
        print("3. Close osu!stream tools")
        print("4. Show file paths for osu!stream tools")
        print("0. Quit")
        print("----------------------------------------")
    
        try:
            choice = int(input("What operation do you want to do?\n"))
            match choice:
                case 0:
                    log('Quitting script~~')
                    run = False
                case 1:
                    src = input("File that needs to be copied [Full path]\n")
                    dest = input("Location & file base name [Full path]\n")
                    file_type = input("What type of file do you want to copy? (txt, png, jpg,...)\n")
                    amount = int(input("Amount of copies\n"))
                    copy_files(src, dest, amount, file_type)
                    time.sleep(2)
                    log("Invalid input, please enter a number.")
                    time.sleep(1)

                case 2:
                    run_stream_tools()
                    time.sleep(2)
                case 3:
                    close_stream_tools()
                    time.sleep(2)
                case 4:
                    print(show_config())
                    print("Settings will be visible for 5 seconds.")
                    time.sleep(5)
                case _:
                    print('Invalid choice.')
                    time.sleep(2)
        except ValueError:
            print("Please enter a number.")
            time.sleep(1)
        

main()