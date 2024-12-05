from breezypythongui import EasyFrame, EasyDialog
from tkinter import PhotoImage
import os

#testing

class MainWindow(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Game Vault Collector")
        self.setSize(400,500)

        self.addLabel(text="Welcome to Game Vault Collector", row=0, column=0, columnspan=2, sticky="NSEW")
        self.addLabel(text="Please select an option below:", row=1, column=0, columnspan=2, sticky="NSEW")

        self.addButton(text="Add Console", row=2, column=0, command=self.addConsole)
        self.addButton(text="View Collection", row=2, column=1, command=self.viewCollection)
        self.addButton(text="Generate Reports", row=3, column=0, command=self.generateReports)
        self.addButton(text="Set Goals", row=3, column=1, command=self.setGoals)
        self.addButton(text="Exit", row=4, column=0, columnspan=2, command=self.quit)
        
        # Determine the path of the current script 
        script_dir = os.path.dirname(os.path.abspath(__file__))

        imageLabel = self.addLabel(text="", row=0, column=0, columnspan=2)
        # Add logo and icons (placeholders for now)
        self.logo = PhotoImage(file=os.path.join(script_dir, "logo.png"))
        imageLabel["image"] = self.logo
        ##self.consoleIcon = PhotoImage(file="console.png")
        ##self.addLabel("", row=1, column=2).addImage(self.consoleIcon)

        # Initialize the collection list
        self.consoleCollection = []

    def addConsole(self):
        AddConsoleWindow(self)

    def viewCollection(self):
        CollectionViewWindow(self, self.consoleCollection)

    def generateReports(self):
        ReportsWindow(self)

    def setGoals(self):
        GoalsWindow(self)

class AddConsoleWindow(EasyDialog):

    def __init__(self, parent):
        EasyDialog.__init__(self, parent, "Add Gaming Console")

    def body(self, master):
        self.addLabel(master, text="Console Name:", row=0, column=0)
        self.consoleName = self.addTextField(master, text="", row=0, column=1)
        self.addLabel(master, text="Storage on device:", row=1, column=0)
        self.storage = self.addTextField(master, text="", row=1, column=1)
        self.addLabel(master, text="Manufacturer:", row=2, column=0)
        self.manufacturer = self.addTextField(master, text="", row=2, column=1)
        self.addLabel(master, text="Purchase Date:", row=3, column=0)
        self.purchaseDate = self.addTextField(master, text="", row=3, column=1)
        self.addLabel(master, text="Purchase Price:", row=4, column=0)
        self.purchasePrice = self.addTextField(master, text="", row=4, column=1)
        
        self.addButton(master, text="Save", row=5, column=0, command=self.saveConsole)
        self.addButton(master, text="Cancel", row=5, column=1, command=self.cancel)

    def saveConsole(self):
        # Save the console details to the parent list
        console = {
            "name": self.consoleName.getText(),
            "storage": self.storage.getText(),
            "manufacturer": self.manufacturer.getText(),
            "purchase_date": self.purchaseDate.getText(),
            "purchase_price": self.purchasePrice.getText()
        }
        self.parent.consoleCollection.append(console)
        self.parent.messageBox("Info", "Console saved successfully.")
        self.destroy()

    def cancel(self):
        self.destroy()

class CollectionViewWindow(EasyDialog):

    def __init__(self, parent, collection):
        EasyDialog.__init__(self, parent, "Console Collection")
        self.collection = collection

    def body(self, master):
        self.addLabel(master, text="Console Collection", row=0, column=0, columnspan=2)

        # Display the list of consoles
        console_list = "\n".join([f"{console['name']} - {console['storage']} - {console['manufacturer']} - {console['purchase_date']} - ${console['purchase_price']}" for console in self.collection])
        self.consoleList = self.addTextArea(master, text=console_list, row=1, column=0, columnspan=2)
        
        self.addButton(master, text="Search", row=2, column=0, command=self.searchConsole)
        self.addButton(master,text="Edit", row=2, column=1, command=self.editConsole)
        self.addButton(master, text="Delete", row=2, column=2, command=self.deleteConsole)
        self.addButton(master, text="Back", row=3, column=1, command=self.destroy)

    def searchConsole(self):
        SearchWindow(self, self.collection)

    def editConsole(self):
        # Add code to edit a selected console
        self.parent.messageBox("Info", "Edit console function.")

    def deleteConsole(self):
        # Add code to delete a selected console
        self.parent.messageBox("Info", "Delete console function.")

class SearchWindow(EasyDialog):

    def __init__(self, parent, collection):
        EasyDialog.__init__(self, parent, "Search Collection")
        self.collection = collection

    def body(self, master):
        self.addLabel(master, text="Search by Console Name:", row=0, column=0)
        self.consoleName = self.addTextField(master, text="", row=0, column=1)
        self.addLabel(master, text="Manufacturer:", row=1, column=0)
        self.manufacturer = self.addTextField(master, text="", row=1, column=1)
        
        self.addButton(master, text="Search", row=2, column=0, command=self.performSearch)
        self.addButton(master, text="Back", row=2, column=1, command=self.destroy)
        
        self.results = self.addTextArea(master, text="", row=3, column=0, columnspan=2)

    def performSearch(self):
        # Perform search and display results
        search_name = self.consoleName.getText().lower()
        search_manufacturer = self.manufacturer.getText().lower()
        
        results = [console for console in self.collection if search_name in console['name'].lower() or search_manufacturer in console['manufacturer'].lower()]
        result_text = "\n".join([f"{console['name']} - {console['storage']} - {console['manufacturer']} - {console['purchase_date']} - ${console['purchase_price']}" for console in results])
        
        self.results.setText(result_text if result_text else "No results found.")

class ReportsWindow(EasyDialog):

    def __init__(self, parent):
        EasyDialog.__init__(self, parent, "Collection Reports")

    def body(self, master):
        self.addLabel(master, text="Report Type:", row=0, column=0)
        self.reportType = self.addTextField(master, text="", row=0, column=1)
        self.addLabel(master, text="Time Period:", row=1, column=0)
        self.timePeriod = self.addTextField(master, text="", row=1, column=1)
        
        self.addButton(master, text="Generate Report", row=2, column=0, command=self.generateReport)
        self.addButton(master, text="Back", row=2, column=1, command=self.destroy)
        
        self.reportArea = self.addTextArea(master, text="", row=3, column=0, columnspan=2)

    def generateReport(self):
        # Add code to generate report and display it
        self.reportArea.setText("Report placeholder.")

class GoalsWindow(EasyDialog):

    def __init__(self, parent):
        EasyDialog.__init__(self, parent, "Set Collection Goals")

    def body(self, master):
        self.addLabel(master, text="Goal Name:", row=0, column=0)
        self.goalName = self.addTextField(master, text="", row=0, column=1)
        self.addLabel(master, text="Console/Accessory:", row=1, column=0)
        self.consoleAccessory = self.addTextField(master, text="", row=1, column=1)
        self.addLabel(master, text="Target Acquisition Date:", row=2, column=0)
        self.targetDate = self.addTextField(master, text="", row=2, column=1)
        
        self.addButton(master, text="Edit", row=3, column=0, command=self.editGoal)
        self.addButton(master, text="Save", row=3, column=1, command=self.saveGoal)
        self.addButton(master, text="Back", row=3, column=2, command=self.destroy)

    def editGoal(self):
        # Add code to edit a goal
        self.parent.messageBox("Info", "Edit goal function.")

    def saveGoal(self):
        # Add code to save a goal
        self.parent.messageBox("Info", "Goal saved successfully.")
        self.destroy()

MainWindow().mainloop()
