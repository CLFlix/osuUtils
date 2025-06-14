from utils import *
from osuscript import *

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