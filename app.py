#from unicodedata import name
from rich.console import Console

def main():
    console = Console()
    state = True
    locations = ["New York, NY", "Seattle, WA", "Houston, TX"]
    weather = ["[blue]41,:cloud_with_rain:, Wind 12 mph[/blue]", "[red]87, :sun:, Wind 5 mph[/red]", "[white]57, :cloud_with_rain:, Wind 9 mph[/white]"]
    tries = 0
    console.print("Welcome to the weather app! Enter a command to get started.", style="bold white underline")
    console.print("\n")
    console.print("New: Learn when sunrise and sunset are happening!", style="bold yellow")
    newFtShow = input("To learn more enter c to see list of commands\n")
    if newFtShow == 'c':
        showCmds(console)
        
    start_menu(console)
    
    while state == True:
        choice = input()

        if choice == 'q':
            state = False
            
        elif choice == 'm':
            start_menu(console)
            
        elif choice == 'f':  
            for i in range(len(locations)): 
                console.print(locations[i])
                console.print("  " + weather[i])
            console.print("\n")

            console.print("[white]To return to main menu enter m[/white]")
            console.print("To get weekly forecast enter w")
            console.print("To get sunrise and sunset times enter s")
            console.print("To quit enter q")
            
        elif choice == 'l':
            for i in range(len(locations)): 
                console.print(locations[i])
            console.print("\n")
            
            console.print("[white]To return to main menu enter m[/white]")
            console.print("To quit enter q")

        elif choice == 'n':
            console.print("[white]Enter a location to add with format <City>, <ST>[/white]")
            new_location = input()
            locations.append(new_location)
            console.print("\n")
            
            undo = input("To undo tracked loctaion, enter u\n")
            if undo == 'u':
                del locations[len(locations) - 1]
                
            start_menu(console)
            
        elif choice == 'a':
            advanced_options(console)
            
        elif choice =='d':
            deleteLocation(console)
            
        elif choice =='c':
            showCmds(console)
            
        elif choice == 's':
            pass
            
        else:
            tries += 1
 
        if tries == 4:
            showCmds(console)
            tries = 0
            
def start_menu(console):
    console.print("Main Menu", style="bold underline")
    console.print("[white]Daily Forecast --enter f[/white]")
    console.print("[white]Tracked Locations --enter l[/white]")
    console.print("[white]Add a Location --enter n[/white]")
    console.print("[red]Advanced Options --enter a[/red]:warning-emoji:")
    console.print("[white]---To quit the app enter q---[/white]")
    
    return 

def advanced_options(console):
    console.print("See commands --Enter c")
    console.print("Delete a tracked location --Enter d")
    console.print("To hide commands --Enter h")
    
    return

def deleteLocation(console):
    pass

def showCmds(console):
    console.print("q -- Enter to quit program")
    console.print("m -- Return to the main menu")
    console.print("f -- Get the daily forecast of tracked locations")
    console.print("l -- List all tracked locations")
    console.print("n -- Add a new location")
    console.print("a -- Advanced options")
    console.print("d -- Delete a tracked location")
    console.print("s -- Show sunrise and sunset times")
    console.print("c -- Show commands")
    console.print("\n")
    #start_menu(console)
    

if __name__ == '__main__':
     main()
