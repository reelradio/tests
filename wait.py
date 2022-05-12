from time import sleep

#If in debug mode, pause execution until user hits enter
#else, wait for a small amount of time
def pause(opts, wait=2):
    if(len(opts) > 0):
        for opt, arg in opts:
            if opt in ('-d', '--debug'):
                input("Press Enter to continue...")
                return
    else:
        sleep(wait)