from breezypythongui import EasyFrame, EasyDialog
from tkinter import PhotoImage
from tkinter import Listbox
from tkinter import StringVar
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
        # Load the collection from file
        self.loadCollection()

    def addConsole(self):
        AddConsoleWindow(self)

    def viewCollection(self):
        CollectionViewWindow(self, self.consoleCollection)

    def generateReports(self):
        ReportsWindow(self)

    def setGoals(self):
        GoalsWindow(self)

    def updateCollection(self): 
        # Save the collection to file after updates
        self.saveCollection() 
        
    def saveCollection(self): 
        homedir = os.path.expanduser("~") 
        filepath = os.path.join(homedir, "Downloads", "console_collection.txt") 
        with open(filepath, 'w') as file: 
            for console in self.consoleCollection: 
                file.write(f"{console['name']}|{console['storage']}|{console['manufacturer']}|{console['purchase_date']}|{console['purchase_price']}\n") 
    
    def loadCollection(self): 
        homedir = os.path.expanduser("~") 
        filepath = os.path.join(homedir, "Downloads", "console_collection.txt") 
        try: 
            with open(filepath, 'r') as file: 
                for line in file: 
                    name, storage, manufacturer, purchase_date, purchase_price = line.strip().split('|') 
                    console = {
                        "name": name, 
                        "storage": storage, 
                        "manufacturer": manufacturer, 
                        "purchase_date": purchase_date, 
                        "purchase_price": purchase_price 
                        } 
                    self.consoleCollection.append(console) 

        except FileNotFoundError: 
            # If the file doesn't exist, start with an empty collection 
            self.consoleCollection = []

class AddConsoleWindow(EasyDialog):

    def __init__(self, parent, console=None, index=None):
        # Store the console being edited (if any)
        self.console = console
        # Store the index of the console being edited
        self.index = index 
        EasyDialog.__init__(self, parent, "Add Gaming Console")
        

    def body(self, master):
        self.addLabel(master, text="Console Name:", row=0, column=0) 
        self.consoleOptions = ["PlayStation 5", "Xbox Series X", "Nintendo Switch", "PlayStation 4", "Xbox One", "Other"] 
        self.consoleName = ttk.Combobox(master, values=self.consoleOptions, state='readonly') 
        self.consoleName.grid(row=0, column=1, sticky="NSEW") 

        self.addLabel(master, text="Storage on device:", row=1, column=0) 
        self.storageOptions = ["500GB", "1TB", "2TB", "Other"] 
        self.storage = ttk.Combobox(master, values=self.storageOptions, state='readonly') 
        self.storage.grid(row=1, column=1, sticky="NSEW")
        
        self.addLabel(master, text="Manufacturer:", row=2, column=0) 
        self.manufacturerOptions = ["Sony", "Microsoft", "Nintendo", "Other"] 
        self.manufacturer = ttk.Combobox(master, values=self.manufacturerOptions, state='readonly') 
        self.manufacturer.grid(row=2, column=1, sticky="NSEW") 

        
        self.addLabel(master, text="Purchase Date:", row=3, column=0) 
        self.monthOptions = [f"{month:02}" for month in range(1, 13)] 
        self.dayOptions = [f"{day:02}" for day in range(1, 32)]
        self.yearOptions = [f"{year:02}" for year in reversed(range(1972, 2026))] 


        self.purchaseMonth = ttk.Combobox(master, values=self.monthOptions, state='readonly') 
        self.purchaseMonth.grid(row=3, column=1, sticky="NSEW") 
        self.purchaseDay = ttk.Combobox(master, values=self.dayOptions, state='readonly', width=3) 
        self.purchaseDay.grid(row=3, column=2, sticky="NSEW") 
        self.purchaseYear = ttk.Combobox(master, values=self.yearOptions, state='readonly', width=5) 
        self.purchaseYear.grid(row=3, column=3, sticky="NSEW")
        
        self.addLabel(master, text="Purchase Price:", row=4, column=0) 
        self.purchasePrice = ttk.Entry(master) 
        self.purchasePrice.grid(row=4, column=1, sticky="NSEW")
        
        if self.console: 
            # Populate fields with existing console data 
            self.consoleName.set(self.console["name"]) 
            self.storage.set(self.console["storage"]) 
            self.manufacturer.set(self.console["manufacturer"]) 
            purchase_date = self.console["purchase_date"].split("-") 
            self.purchaseMonth.set(purchase_date[0]) 
            self.purchaseDay.set(purchase_date[1]) 
            self.purchaseYear.set(purchase_date[2]) 
            self.purchasePrice.insert(0, self.console["purchase_price"])

        self.addButton(master, text="Save", row=5, column=0, command=self.saveConsole)
        self.addButton(master, text="Cancel", row=5, column=1, command=self.cancel)

    def buttonbox(self):
        """Override this method to prevent the default OK/Cancel buttons from appearing.""" 
        pass

    def saveConsole(self):
        # Validate inputs
        if not self.consoleName.get() or not self.storage.get() or not self.manufacturer.get() or not self.purchaseDay.get() or not self.purchaseMonth.get() or not self.purchaseYear.get() or not self.purchasePrice.get():
            messagebox.showerror("Error", "All fields are required.")
            return

        # Save the console details to the parent list
        console = {
            "name": self.consoleName.get(),
            "storage": self.storage.get(),
            "manufacturer": self.manufacturer.get(),
            "purchase_date": f"{self.purchaseMonth.get()}-{self.purchaseDay.get()}-{self.purchaseYear.get()}",
            "purchase_price": self.purchasePrice.get()
        }
        if self.console: 
            # Update existing console 
            self.parent.collection[self.index] = console 
        else:
            # Add new console 
            self.parent.consoleCollection.append(console) 
            
        # Save the collection to file after adding or editing a console self
        self.parent.updateCollection() 

        self.parent.messageBox("Info", "Console saved successfully.")
        self.destroy()

    def cancel(self):
        self.destroy()

class CollectionViewWindow(EasyDialog):
    def __init__(self, parent, collection):
        self.collection = collection
        # Store the index of the selected console
        self.selected_console_index = None

        EasyDialog.__init__(self, parent, "Console Collection")
        

    def body(self, master):
        self.addLabel(master, text="Console Collection", row=0, column=0, columnspan=2)
        self.addLabel(master, text="Name - Storage - Manufacturer - Purchase Date - Purchase Price", row=1, column=0, columnspan=2)

        # Display the list of consoles
        self.console_list_var = StringVar(value=[f"{console['name']} - {console['storage']} - {console['manufacturer']} - {console['purchase_date']} - ${console['purchase_price']}" for console in self.collection])        
        self.consoleList = Listbox(master, listvariable=self.console_list_var, height=10, width=60) 
        self.consoleList.grid(row=2, column=0, columnspan=2, sticky="NSEW") 
        self.consoleList.bind('<<ListboxSelect>>', self.on_console_select)

        self.addButton(master, text="Search", row=3, column=0, command=self.searchConsole)
        self.addButton(master,text="Edit", row=3, column=1, command=self.editConsole)
        self.addButton(master, text="Delete", row=3, column=2, command=self.deleteConsole)
        self.addButton(master, text="Back", row=4, column=1, command=self.destroy)

    def buttonbox(self):
        """Override this method to prevent the default OK/Cancel buttons from appearing.""" 
        pass

    def on_console_select(self, event): 
        selection = event.widget.curselection() 
        if selection: 
            self.selected_console_index = selection[0] 
            selected_console = self.collection[self.selected_console_index] 
            console_text = f"Name: {selected_console['name']}\nStorage: {selected_console['storage']}\nManufacturer: {selected_console['manufacturer']}\nPurchase Date: {selected_console['purchase_date']}\nPurchase Price: ${selected_console['purchase_price']}" 
            

    def searchConsole(self):
        SearchWindow(self, self.collection)

    def editConsole(self):
        if self.selected_console_index is None:
            messagebox.showerror("Error", "No console selected.")
            return

        selected_console = self.collection[self.selected_console_index]
        AddConsoleWindow(self.parent, console=selected_console, index=self.selected_console_index)


    def deleteConsole(self): 
        if self.selected_console_index is None: 
            messagebox.showerror("Error", "No console selected.") 
            return 
        del self.collection[self.selected_console_index] 
        self.parent.updateCollection()
        self.console_list_var.set([f"{console['name']} - {console['storage']} - {console['manufacturer']} - {console['purchase_date']} - ${console['purchase_price']}" for console in self.collection]) 
            
        # Reset the selection 
        self.selected_console_index = None 
        self.parent.messageBox("Info", "Console deleted successfully.")

class SearchWindow(EasyDialog):

    def __init__(self, parent, collection):
        self.collection = collection
        EasyDialog.__init__(self, parent, "Search Collection")

    def body(self, master):
        self.addLabel(master, text="Search by Console Name:", row=0, column=0) 
        self.consoleOptions = ["PlayStation 5", "Xbox Series X", "Nintendo Switch", "PlayStation 4", "Xbox One", "Other", ""] 
        self.consoleName = ttk.Combobox(master, values=self.consoleOptions, state='readonly') 
        self.consoleName.grid(row=0, column=1, sticky="NSEW") 

        self.addLabel(master, text="Manufacturer:", row=1, column=0) 
        self.manufacturerOptions = ["Sony", "Microsoft", "Nintendo", "Other", ""] 
        self.manufacturer = ttk.Combobox(master, values=self.manufacturerOptions, state='readonly') 
        self.manufacturer.grid(row=1, column=1, sticky="NSEW")
        
        self.addButton(master, text="Search", row=2, column=0, command=self.performSearch)
        self.addButton(master, text="Back", row=2, column=1, command=self.destroy)
        
        self.results = self.addTextArea(master, text="", row=3, column=0, columnspan=2)
        # Disable editing 
        self.results.configure(state='disabled')

    def buttonbox(self):
        """Override this method to prevent the default OK/Cancel buttons from appearing.""" 
        pass

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
        
        # Enable editing to update text 
        self.results.configure(state='normal') 

        # Clear current content 
        self.results.delete(1.0, 'end') 

        # Insert new content 
        self.results.insert('end', result_text if result_text else "No results found.") 

        # Disable editing again
        self.results.configure(state='disabled')
        
class ReportsWindow(EasyDialog):

    def __init__(self, parent):
        EasyDialog.__init__(self, parent, "Collection Reports")

    def body(self, master):
        self.addLabel(master, text="Report Type:", row=0, column=0) 
        self.reportOptions = ["Yearly", "Monthly", "Weekly", "Custom"] 
        self.reportType = ttk.Combobox(master, values=self.reportOptions, state='readonly') 
        self.reportType.grid(row=0, column=1, sticky="NSEW") 

        self.addLabel(master, text="Time Period:", row=1, column=0) 
        self.timePeriodOptions = ["2020", "2021", "2022", "2023", "2024", "Other"] 
        self.timePeriod = ttk.Combobox(master, values=self.timePeriodOptions, state='readonly') 
        self.timePeriod.grid(row=1, column=1, sticky="NSEW")
        
        self.addButton(master, text="Generate Report", row=2, column=0, command=self.generateReport)
        self.addButton(master, text="Back", row=2, column=1, command=self.destroy)
        
        self.reportArea = self.addTextArea(master, text="", row=3, column=0, columnspan=2)

    def buttonbox(self):
        """Override this method to prevent the default OK/Cancel buttons from appearing.""" 
        pass

    def generateReport(self):

        # Validate inputs 
        if not self.reportType.get() or not self.timePeriod.get(): 
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
        self.goalName = ttk.Combobox(master, values=self.goalOptions, state='readonly') 
        self.goalName.grid(row=0, column=1, sticky="NSEW") 

        self.addLabel(master, text="Console/Accessory:", row=1, column=0) 
        self.consoleOptions = ["PlayStation 5", "Xbox Series X", "Nintendo Switch", "PlayStation 4", "Xbox One", "Other"] 
        self.consoleAccessory = ttk.Combobox(master, values=self.consoleOptions, state='readonly') 
        self.consoleAccessory.grid(row=1, column=1, sticky="NSEW") 

        self.addLabel(master, text="Target Acquisition Date:", row=2, column=0) 
        self.targetDateOptions = ["2020", "2021", "2022", "2023", "2024", "Other"] 
        self.targetDate = ttk.Combobox(master, values=self.targetDateOptions, state='readonly') 
        self.targetDate.grid(row=2, column=1, sticky="NSEW")
        
        self.addButton(master, text="Edit", row=3, column=0, command=self.editGoal)
        self.addButton(master, text="Save", row=3, column=1, command=self.saveGoal)
        self.addButton(master, text="Back", row=3, column=2, command=self.destroy)

    def buttonbox(self):
        """Override this method to prevent the default OK/Cancel buttons from appearing.""" 
        pass

    def editGoal(self):
        # Add code to edit a goal
        self.parent.messageBox("Info", "Edit goal function.")

    def saveGoal(self):
        # Validate inputs
        if not self.goalName.get() or not self.consoleAccessory.get() or not self.targetDate.get():
            messagebox.showerror("Error", "All fields are required.")
            return

        # Add code to save a goal
        self.parent.messageBox("Info", "Goal saved successfully.")
        self.destroy()


MainWindow().mainloop()
