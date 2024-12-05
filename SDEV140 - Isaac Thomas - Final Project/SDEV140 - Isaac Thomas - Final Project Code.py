from breezypythongui import EasyFrame, EasyDialog
from tkinter import PhotoImage
from tkinter import messagebox

# Adding a drop-down menu using the ttk.Combobox widget from the tkinter module. 
from tkinter import ttk
import os

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

        self.addLabel(master, text="Console Name:", row=0, column=0) 
        self.consoleOptions = ["PlayStation 5", "Xbox Series X", "Nintendo Switch", "PlayStation 4", "Xbox One", "Other"] 
        self.consoleName = ttk.Combobox(master, values=self.consoleOptions) 
        self.consoleName.grid(row=0, column=1, sticky="NSEW") 

        self.addLabel(master, text="Storage on device:", row=1, column=0) 
        self.storageOptions = ["500GB", "1TB", "2TB", "Other"] 
        self.storage = ttk.Combobox(master, values=self.storageOptions) 
        self.storage.grid(row=1, column=1, sticky="NSEW")
        
        self.addLabel(master, text="Manufacturer:", row=2, column=0) 
        self.manufacturerOptions = ["Sony", "Microsoft", "Nintendo", "Other"] 
        self.manufacturer = ttk.Combobox(master, values=self.manufacturerOptions) 
        self.manufacturer.grid(row=2, column=1, sticky="NSEW") 

        self.addLabel(master, text="Purchase Date:", row=3, column=0) 
        self.purchaseDateOptions = ["2020", "2021", "2022", "2023", "2024", "Other"] 
        self.purchaseDate = ttk.Combobox(master, values=self.purchaseDateOptions) 
        self.purchaseDate.grid(row=3, column=1, sticky="NSEW")
        
        self.addLabel(master, text="Purchase Price:", row=4, column=0) 
        self.purchasePriceOptions = ["<$300", "$300-$500", ">$500", "Other"] 
        self.purchasePrice = ttk.Combobox(master, values=self.purchasePriceOptions) 
        self.purchasePrice.grid(row=4, column=1, sticky="NSEW")
        
        self.addButton(master, text="Save", row=5, column=0, command=self.saveConsole)
        self.addButton(master, text="Cancel", row=5, column=1, command=self.cancel)

    def saveConsole(self):
        # Validate inputs
        if not self.consoleName.get() or not self.storage.get() or not self.manufacturer.get() or not self.purchaseDate.get() or not self.purchasePrice.get():
            messagebox.showerror("Error", "All fields are required.")
            return

        # Save the console details to the parent list
        console = {
            "name": self.consoleName.get(),
            "storage": self.storage.get(),
            "manufacturer": self.manufacturer.get(),
            "purchase_date": self.purchaseDate.get(),
            "purchase_price": self.purchasePrice.get()
        }
        self.parent.consoleCollection.append(console)
        self.parent.messageBox("Info", "Console saved successfully.")
        self.destroy()

    def cancel(self):
        self.destroy()

class CollectionViewWindow(EasyDialog):

    def __init__(self, parent, collection):
        self.collection = collection
        EasyDialog.__init__(self, parent, "Console Collection")
        

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
        self.collection = collection
        EasyDialog.__init__(self, parent, "Search Collection")

    def body(self, master):
        self.addLabel(master, text="Search by Console Name:", row=0, column=0) 
        self.consoleOptions = ["PlayStation 5", "Xbox Series X", "Nintendo Switch", "PlayStation 4", "Xbox One", "Other"] 
        self.consoleName = ttk.Combobox(master, values=self.consoleOptions) 
        self.consoleName.grid(row=0, column=1, sticky="NSEW") 

        self.addLabel(master, text="Manufacturer:", row=1, column=0) 
        self.manufacturerOptions = ["Sony", "Microsoft", "Nintendo", "Other"] 
        self.manufacturer = ttk.Combobox(master, values=self.manufacturerOptions) 
        self.manufacturer.grid(row=1, column=1, sticky="NSEW")
        
        self.addButton(master, text="Search", row=2, column=0, command=self.performSearch)
        self.addButton(master, text="Back", row=2, column=1, command=self.destroy)
        
        self.results = self.addTextArea(master, text="", row=3, column=0, columnspan=2)

    def performSearch(self):
        # Perform search and display results
        search_name = self.consoleName.get().lower()
        search_manufacturer = self.manufacturer.get().lower()

        if not search_name and not search_manufacturer:
            results = self.collection

        elif search_name and search_manufacturer:
            results = [console for console in self.collection if search_name == console['name'].lower() and search_manufacturer == console['manufacturer'].lower()]
        
        elif search_name:
            results = [console for console in self.collection if search_name == console['name'].lower()]
        
        elif search_manufacturer:
            results = [console for console in self.collection if search_manufacturer == console['manufacturer'].lower()]


        #results = [console for console in self.collection if search_name in console['name'].lower() or search_manufacturer in console['manufacturer'].lower()]
        result_text = "\n".join([f"{console['name']} - {console['storage']} - {console['manufacturer']} - {console['purchase_date']} - ${console['purchase_price']}" for console in results])
        
        self.results.setText(result_text if result_text else "No results found.")

class ReportsWindow(EasyDialog):

    def __init__(self, parent):
        EasyDialog.__init__(self, parent, "Collection Reports")

    def body(self, master):
        self.addLabel(master, text="Report Type:", row=0, column=0) 
        self.reportOptions = ["Yearly", "Monthly", "Weekly", "Custom"] 
        self.reportType = ttk.Combobox(master, values=self.reportOptions) 
        self.reportType.grid(row=0, column=1, sticky="NSEW") 

        self.addLabel(master, text="Time Period:", row=1, column=0) 
        self.timePeriodOptions = ["2020", "2021", "2022", "2023", "2024", "Other"] 
        self.timePeriod = ttk.Combobox(master, values=self.timePeriodOptions) 
        self.timePeriod.grid(row=1, column=1, sticky="NSEW")
        
        self.addButton(master, text="Generate Report", row=2, column=0, command=self.generateReport)
        self.addButton(master, text="Back", row=2, column=1, command=self.destroy)
        
        self.reportArea = self.addTextArea(master, text="", row=3, column=0, columnspan=2)

    def generateReport(self):

        # Validate inputs 
        if not self.reportType.getText() or not self.timePeriod.getText(): 
            messagebox.showerror("Error", "All fields are required.") 
            return

        # Add code to generate report and display it
        self.reportArea.setText("Report placeholder.")

class GoalsWindow(EasyDialog):

    def __init__(self, parent):
        EasyDialog.__init__(self, parent, "Set Collection Goals")

    def body(self, master):
        self.addLabel(master, text="Goal Name:", row=0, column=0)
        self.goalOptions = ["Complete Collection", "Specific Console", "Limited Edition", "Other"] 
        self.goalName = ttk.Combobox(master, values=self.goalOptions) 
        self.goalName.grid(row=0, column=1, sticky="NSEW") 

        self.addLabel(master, text="Console/Accessory:", row=1, column=0) 
        self.consoleOptions = ["PlayStation 5", "Xbox Series X", "Nintendo Switch", "PlayStation 4", "Xbox One", "Other"] 
        self.consoleAccessory = ttk.Combobox(master, values=self.consoleOptions) 
        self.consoleAccessory.grid(row=1, column=1, sticky="NSEW") 

        self.addLabel(master, text="Target Acquisition Date:", row=2, column=0) 
        self.targetDateOptions = ["2020", "2021", "2022", "2023", "2024", "Other"] 
        self.targetDate = ttk.Combobox(master, values=self.targetDateOptions) 
        self.targetDate.grid(row=2, column=1, sticky="NSEW")
        
        self.addButton(master, text="Edit", row=3, column=0, command=self.editGoal)
        self.addButton(master, text="Save", row=3, column=1, command=self.saveGoal)
        self.addButton(master, text="Back", row=3, column=2, command=self.destroy)

    def editGoal(self):
        # Add code to edit a goal
        self.parent.messageBox("Info", "Edit goal function.")

    def saveGoal(self):
        # Validate inputs
        if not self.goalName.getText() or not self.consoleAccessory.getText() or not self.targetDate.getText():
            messagebox.showerror("Error", "All fields are required.")
            return

        # Add code to save a goal
        self.parent.messageBox("Info", "Goal saved successfully.")
        self.destroy()


MainWindow().mainloop()
