from rich.console import Console

console = Console()
state = True

while state == True:
    console.print("Welcome to the weather app! Enter a command to get started.", style="bold white underline")

    console.print("1. [white]Daily Forecast[/white]")
    console.print("2. [white]Tracked Locations[/white]")
    console.print("3. [white]Add a Location[/white]")
    console.print("4. [red]Advanced Options[/red]:warning-emoji:")

    choice = input()
    #print(choice)
    if int(choice) == 1:  
      console.print("Nice:cloud_with_rain:")
    elif int(choice) == 2:
      console.print("BOO:ghost:")
    else:
      state = False
      