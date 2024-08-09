from lib.habits import Tracker
import os
import subprocess

def clear():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

clear()
track = Tracker()
while True:
    track.load_data()
    print("Welcome to my habit tracker. What would you like to do?\n")
    print("1. View habits and completion status\n")
    print("2. Add or remove habits\n")
    print("3. View habit streaks\n")
    print("4. View habit calender\n")
    option = int(input("Enter the number corresponding to your desired option: "))
    if option == 1:
        print(track.completion())
        print("Press any button to go back to the options menu...")
        input()
        clear()
    elif option == 2:
        while True:
            habitdata = ""
            for name, _ in track.habits.items():
                habitdata = habitdata + name + "\n"
            print("These are the currently stored habits:\n"+habitdata)
            print("1. Add habit\n")
            print("2. Remove habit\n")
            print("3. Go back")
            option = int(input("Enter the number corresponding to your desired option: "))
            if option == 1:
                name = input("Enter name of the new habit: ")
                stat = track.add_habit(name)
                if stat == 0:
                    print(f"{name} already exists.\n")
            elif option == 2:
                name = input("Enter name of the habit to be removed: ")
                stat = track.remove_habit(name)
                if stat == 0:
                    print(f"{name} doesn't exist.\n")
            elif option == 3:
                break
            else:
                print("Option not recognized, please try again.\n")
        clear()
    else:
        track.save_data()
        break