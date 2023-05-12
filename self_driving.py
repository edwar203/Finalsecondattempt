"""
    Name: self_driving.py
    Author: Bill Edwards
    Created: 05/12/2023
    Description: Creating a program for a self driving console ran car with speed cap and random events
"""
import math
import random
from rich.console import Console
from rich.panel import Panel

console = Console()

#Create Class
class StantonAI():

#Create Methods
    def __init__(self):
        self.speed = 0
        self.running = 0

    def start(self):
        self.running = 1
        self.speed = 5
        console.print(
                Panel.fit(f"Starting Moving Speed Increased to {self.speed} MPH"
                          , style = "italic dark_red")
            )
        

    def stop(self):
        self.speed = 0
        console.print(
                Panel.fit("Now Stopping And Parking Vehicle"
                          , style = "italic dark_red")
            )

    def speedup(self):
        addspeed = console.input(
                Panel.fit(f"You are currently going {self.speed}MPH \nHow Many MPH would yo like to add to your speed?"
                          , style = "italic dark_red")
            )
        self.incspeed = self.speed + addspeed

    def slowdown(self):
        print("works")

    def decide(self):
        if self.speed < 141:
            self.display_console()
        else:
            self.random_event()

    def random_event(self):
        pass


    def display_console(self):
        console.print(
                Panel.fit("To Start Moving Please Input 1 \nTo Speed Up Please Input 2 \nTo Slow Down Please Input 3 \nTo Stop And Park Please Input 4 \n To Quit Please Input 5"
                          , style = "italic dark_red")
            )
        choice = console.input(Panel.fit("What would you like to do? (1, 2, 3, 4, or 5): ", style = "italic dark_red"))

        if choice == "1":
            self.start()
            self.decide()
        elif choice == "2":
            self.speedup()
            self.decide()
        elif choice == "3":
            self.slowdown()
            self.decide()
        elif choice == "4":
            self.stop()
            self.decide()
        elif choice == "5":
            quit

#Create Main
def main():
    #Create Nice Title
    console.print(
                Panel.fit(" --  StantonAI's Self Driving Car  --  ", style = "bold dark_red", subtitle="By: Bill Edwards")
            )
    #run anything not in class

    #run class
    self_drive = StantonAI()

    self_drive.display_console()

#run Main
if __name__ == "__main__":
    main()