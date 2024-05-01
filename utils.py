import sys

def quit_or_continue():                                                         # Allows player to quit game whenever
    stay_or_leave = ""
    stay_or_leave = input("Press z to continue, or type quit to quit: ")        # Receive input to determine if quit
    stay_or_leave = stay_or_leave.lower()
    if stay_or_leave == "z":
      print("Starting...")
    elif stay_or_leave == "quit":
        sys.exit("Goodbye.")                                                    # sys.exit() allows player to quit as cell is terminated
    else:                                                                       # In the case where people enter other stuff
        while stay_or_leave != "z" and stay_or_leave != "quit":                 # While loop used so that input is alway requested if input != z or input != quit
            stay_or_leave = ""
            stay_or_leave = input("Press z to start. \nType quit to quit. \n")
            stay_or_leave = stay_or_leave.lower()
            if stay_or_leave == "z":
                break                                                           # Break used, otherwise while loop will continue running
            elif stay_or_leave == "quit":
                sys.exit("Goodbye.")
