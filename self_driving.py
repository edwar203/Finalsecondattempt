"""
    Name: self_driving.py
    Author: Bill Edwards
    Created: 05/12/2023
    Description: Creating a program for a self driving console ran car with speed cap and random events
"""
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
        self.safespeed = 140

    def start(self):
        if self.running  == 0:
            self.running = 1
            self.speed = 5
            console.print(
                    Panel.fit(f"Starting Moving Speed Increased to {self.speed} MPH"
                              , style = "italic dark_red")
                )
        elif self.running == 1:
            console.print(
                Panel.fit(f"Your vehicle is already running please make a different selection!"
                          , style = "italic dark_red"))
        

    def stop(self):
        if self.running == 1:
            self.speed = 0
            self.running = 0
            console.print(
                    Panel.fit("Now Stopping And Parking Vehicle"
                          , style = "italic dark_red")
                )
        elif self.running == 0:
            console.print(
                Panel.fit(f"You are already parked please make a different selection!"
                          , style = "italic dark_red")
            )
    def speedup(self):
        if self.running == 0:
            console.print(
                Panel.fit(f"You are currently parked please start vehicle movement"
                          , style = "italic dark_red")
            )
            self.display_console()
        elif self.running == 1:
            addspeed = console.input(
                    Panel.fit(f"You are currently going {self.speed}MPH \nHow Many MPH would you like to add to your speed?"
                              , style = "italic dark_red")
                )
            self.chspeed = self.speed + addspeed
            console.print(
                    Panel.fit(f"You have increased your speed from {self.speed}MPH to {self.chspeed}MPH"
                              , style = "italic dark_red")
                )
            self.speed = self.chspeed

    def slowdown(self):
        respeed = console.input(
                Panel.fit(f"You are currently going {self.speed}MPH \nHow Many MPH would you like to remove from your speed?"
                          , style = "italic dark_red")
            )
        self.chspeed = self.speed - respeed
        console.print(
                Panel.fit(f"You have decreased your speed from {self.speed}MPH to {self.chspeed}MPH"
                          , style = "italic dark_red")
            )
        self.speed = self.chspeed

    def shutdown(self):
        if self.speed == 0:
            console.print(
                    Panel.fit("You have chosen to shutdown the vehicle Goodbye"
                            , style = "italic dark_red")
            )
            quit
        else:
            console.print(
                Panel.fit(f"ERROR: Your vehicle is still moving Please Stop Vehicle First!!!"
                          , style = "italic dark_red")
            )
            self.decide()
    def decide(self):
        if self.speed < 0:
            console.print(
                Panel.fit(f"You have attempted to go less then 0MPH which is impossible please increase to a real speed!"
                          , style = "italic dark_red")
            )
            self.speedup()
        elif self.speed < 141:
            self.display_console()
        else:
            self.random_event()

    def breakaway(self):
        self.break_event = random.randrange(1,10)
        if self.break_event in range(0,7):
            self.speed = self.safespeed
            console.print(
                Panel.fit(f"As you sped up your tires broke loose from the road! \nLuckinly I got our speed back down to the safe speed of {self.safespeed}MPH "
                          , style = "italic dark_red")
            )
        elif self.break_event in range(8,10):
            self.wreck()

    def wreck(self):
        console.print(
                Panel.fit(f"I'm afraid you have wrecked me because you were going {self.speed}MPH GOODBYE"
                          , style = "italic dark_red")
        )
        quit
        

    def random_event(self):
        self.event = random.randrange(0, 10)
        if self.event in range(0,5):
            self.display_console()
        elif self.event in range(6,7):
            self.breakaway()
        elif self.event in range(8,10):
            self.wreck()


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
            self.shutdown()

#Create Main
def main():
    #Create Nice Title
    console.print(
                Panel.fit(" --  StantonAI's Self Driving Car  --  ", style = "bold dark_red", subtitle="By: Bill Edwards")
            )
    console.print(
                Panel.fit("You are in a self driving car please increase or decrease speed as you like. Anything over 140MPH is not suggested as those are over safe speeds"
                          , style = "italic dark_red")
    )
    #run anything not in class

    #run class
    self_drive = StantonAI()

    self_drive.display_console()

#run Main
if __name__ == "__main__":
    main()