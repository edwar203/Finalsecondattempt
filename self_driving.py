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

console = Console

#Create Class
class StantonAI():

#Create Methods
    def __init__(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def speedup(self):
        pass

    def slowdown(self):
        pass

#Create Main
def main():
    #Create Nice Title
    console.print(
                Panel.fit(" --  StantonAI's Self Driving Car  --  ", style = "bold dark_red", subtitle="By: Bill Edwards")
            )
    #run anything not in class

    #run class
    self_drive = StantonAI

    self_drive.display_console()

#run Main
if __name__ == "__main__":
    main()