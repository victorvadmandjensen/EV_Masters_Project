from openpyxl import Workbook
import event

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
        self.ws.cell(column=2,row=1).value = "Energy sent to battery by players"
        self.ws.cell(column=3,row=1).value = "Event ID"
        self.workbook.save(filename = self.filename)

    def add_energy_sent_to_battery(self, energy_sent):
        self.counter = self.counter + 1
        self.ws.cell(column=1,row=self.counter).value = self.counter - 1
        self.ws.cell(column=2,row=self.counter).value = energy_sent
        self.workbook.save(filename = self.filename)

    def add_event(self, event):
        self.ws.cell(column=3,row=self.counter).value = event.id
        self.workbook.save(filename = self.filename)