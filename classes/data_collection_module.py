from openpyxl import Workbook
import classes.event as event

class Data_Collection_Module:
    def __init__(self):
        self.counter = 1
        self.workbook = None
        self.ws = None
        self.filename = "energy_per_round.xlsx"
    
    def initialize_workbook(self):
        self.workbook = Workbook()
        self.ws = self.workbook.active
        self.ws.title = "Energy sent to battery"
        self.ws.cell(column=1,row=1).value = "Round"
        self.ws.cell(column=2,row=1).value = "Energy sent to battery by players in this round"
        self.ws.cell(column=3,row=1).value = "Event ID"
        self.ws.cell(column=4,row=1).value = "Event name"
        self.ws.cell(column=5,row=1).value = "Energy decision at end of this round"
        self.workbook.save(filename = self.filename)

    def add_energy_sent_to_battery(self, energy_sent):
        self.counter = self.counter + 1
        self.ws.cell(column=1,row=self.counter).value = self.counter - 1
        self.ws.cell(column=2,row=self.counter).value = energy_sent
        self.workbook.save(filename = self.filename)

    def add_event(self, event):
        self.ws.cell(column=3,row=self.counter).value = event.id
        self.ws.cell(column=4,row=self.counter).value = event.name
        self.workbook.save(filename = self.filename)
    
    def add_energy_decision(self, energy_decision):
        self.ws.cell(column=5,row=self.counter).value = energy_decision.flavor_text
        self.workbook.save(filename = self.filename)