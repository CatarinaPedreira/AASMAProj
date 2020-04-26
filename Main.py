import tkinter
import sys
import time
from threading import Thread

from Agent import Agent
from Emergency import Emergency
from Hospital import Hospital
from MedicalVehicle import MedicalVehicle

zones = []
agents = [None, None, None, None]
hospital_groups = [[None], [None], [None], [None]]


def create_board():
    board = tkinter.Tk()
    canvas = tkinter.Canvas(board, width=500, height=500)
    canvas.create_line(250, 0, 250, 500, fill="black")
    canvas.create_line(0, 250, 500, 250, fill="black")
    #TODO create shapes for agent in each zone, hospitals around them
    # Check how to draw cool baby ambulances!
    canvas.pack()
    board.mainloop()


def setup():
    global zones
    zones = [[(0,0), (250, 0), (0,250), (250,250)], [(250,0), (500, 0), (250,250), (500,250)], [(0,250), (250, 250), (0,500), (250,500)], [(250,250), (500, 250), (250,500), (500,500)]]
    for i in range(4):
        # Hardcoded hospitals, we can change it later
        hospital_groups[i] = [Hospital(None, 100, 10), Hospital(None, 150, 10), Hospital(None, 95, 10)]
        agents[i] = Agent(zones[i], zones, hospital_groups[i], None)

    for i in range(4):
        for group in hospital_groups:
            for hosp in group:
                hosp.set_control_tower(agents[i])
                medical_vehicles = [MedicalVehicle(100, 100, "available", hosp)] * 5  # enough?
                hosp.set_medical_vehicles(medical_vehicles)


def create_emergency():
    # TODO, create emergency in random coordinates (x,y)
    return Emergency(None, None, None, None, None, None, None)


def allocate_emergency(emer):
    emer.get_control_tower().allocate_emergency(emer)


#######################################################################################################################

create_board()
setup()

# while True:
#     emergency = create_emergency()
#     time.sleep(3)
#     thread = Thread(target=allocate_emergency, args=(emergency,))
#     thread.start()
#     thread.join()
