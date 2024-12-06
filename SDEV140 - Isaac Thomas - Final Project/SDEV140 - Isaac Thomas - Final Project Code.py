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
        # Initialize the main window with a title
        EasyFrame.__init__(self, title="Game Vault Collector")
        self.setSize(400, 500)

        # Add welcome and instruction labels
        self.addLabel(text="Welcome to Game Vault Collector", row=0, column=0, columnspan=2, sticky="NSEW")
        self.addLabel(text="Please select an option below:", row=1, column=0, columnspan=2, sticky="NSEW")

        # Add buttons for different functionalities
        self.addButton(text="Add Console", row=2, column=0, command=self.addConsole)
        self.addButton(text="View Collection", row=2, column=1, command=self.viewCollection)
        self.addButton(text="Generate Reports", row=3, column=0, command=self.generateReports)
        self.addButton(text="Set Goals", row=3, column=1, command=self.setGoals)
        self.addButton(text="Exit", row=4, column=0, columnspan=2, command=self.quit)
        
        # Determine the path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Add logo and icons (placeholders for now)
        imageLabel = self.addLabel(text="", row=0, column=0, columnspan=2)
        self.logo = PhotoImage(file=os.path.join(script_dir, "logo.png"))
        imageLabel["image"] = self.logo
        # self.consoleIcon = PhotoImage(file="console.png")
        # self.addLabel("", row=1, column=2).addImage(self.consoleIcon)

        # Initialize the collection list
        self.consoleCollection = []
        # Load the collection from file
        self.loadCollection()

    def addConsole(self):
        # Open the add console window
        AddConsoleWindow(self, self.consoleCollection)

    def viewCollection(self):
        # Open the view collection window
        CollectionViewWindow(self, self.consoleCollection)

    def generateReports(self):
        # Open the generate reports window
        ReportsWindow(self)

    def setGoals(self):
        # Open the set goals window
        GoalsWindow(self)

    def updateCollection(self): 
        # Save the collection to file after updates
        self.saveCollection() 
        
    def saveCollection(self): 
        # Get the path to the user's home directory
        homedir = os.path.expanduser("~") 
        # Define the path to the file where the collection will be saved
        filepath = os.path.join(homedir, "Downloads", "console_collection.txt") 
        with open(filepath, 'w') as file: 
            # Write each console's details to the file in the specified format
            for console in self.consoleCollection: 
                file.write(f"{console['name']}|{console['storage']}|{console['manufacturer']}|{console['release_year']}|{console['color']}|{console['condition']}|{console['purchase_date']}|{console['purchase_price']}\n") 
                
    def loadCollection(self): 
        # Get the path to the user's home directory
        homedir = os.path.expanduser("~") 
        # Define the path to the file where the collection will be loaded from
        filepath = os.path.join(homedir, "Downloads", "console_collection.txt") 
        try: 
            # Open the file and read its contents
            with open(filepath, 'r') as file: 
                for line in file: 
                    # Split each line into the respective console attributes
                    name, storage, manufacturer, release_year, color, condition, purchase_date, purchase_price = line.strip().split('|') 
                    # Create a dictionary for each console
                    console = {
                        "name": name, 
                        "storage": storage, 
                        "manufacturer": manufacturer, 
                        "release_year": release_year,
                        "color": color,
                        "condition": condition,
                        "purchase_date": purchase_date, 
                        "purchase_price": purchase_price 
                    } 
                    # Add the console to the collection list
                    self.consoleCollection.append(console) 
        except FileNotFoundError: 
            # If the file doesn't exist, start with an empty collection
            self.consoleCollection = []

class AddConsoleWindow(EasyDialog):

    def __init__(self, parent, collection, console=None, index=None):
        # Store the collection being edited
        self.collection = collection 
        # Store the console being edited (if any)
        self.console = console
        # Store the index of the console being edited
        self.index = index 
        # Initialize the dialog window with the title "Add Gaming Console"
        EasyDialog.__init__(self, parent, "Add Gaming Console")
        

    def body(self, master):
        # Add label and dropdown for console name
        self.addLabel(master, text="Console Name:", row=0, column=0)
        self.consoleOptions = [
            "PlayStation 5", "Xbox Series X", "Nintendo Switch", 
            "PlayStation 4", "Xbox One", "Wii", "NES", 
            "SNES", "Nintendo 64", "GameCube", "PlayStation 3", 
            "Xbox 360", "Wii U", "PlayStation 2", "Xbox", 
            "Sega Genesis", "Dreamcast", "Sega Saturn", 
            "PlayStation", "Atari 2600", "Atari 5200", 
            "Atari 7800", "ColecoVision", "Intellivision", 
            "Neo Geo", "TurboGrafx-16", "Game Boy", 
            "Game Boy Color", "Game Boy Advance", "PSP", 
            "PS Vita", "Nintendo DS", "Nintendo 3DS", "Other"
        ]
        self.consoleName = ttk.Combobox(master, values=self.consoleOptions, state='readonly')
        self.consoleName.grid(row=0, column=1, sticky="NSEW")

        # Add label and dropdown for storage options
        self.addLabel(master, text="Storage on device:", row=1, column=0)
        self.storageOptions = [
            "None", "128MB", "256MB", "512MB", 
            "1GB", "2GB", "4GB", "8GB", "16GB", 
            "32GB", "64GB", "128GB", "256GB", 
            "500GB", "1TB", "2TB", "4TB", "Other"
        ]
        self.storage = ttk.Combobox(master, values=self.storageOptions, state='readonly')
        self.storage.grid(row=1, column=1, sticky="NSEW")

        # Add label and dropdown for manufacturer options
        self.addLabel(master, text="Manufacturer:", row=2, column=0)
        self.manufacturerOptions = [
            "Sony", "Microsoft", "Nintendo", "Sega", 
            "Atari", "Coleco", "Mattel", "SNK", 
            "NEC", "Bandai", "Commodore", "Other"
        ]
        self.manufacturer = ttk.Combobox(master, values=self.manufacturerOptions, state='readonly')
        self.manufacturer.grid(row=2, column=1, sticky="NSEW")

        # Add label and dropdown for release year options
        self.addLabel(master, text="Release Year:", row=3, column=0)
        self.releaseYearOptions = [str(madeyear) for madeyear in reversed(range(1972, 2026))]
        self.releaseYear = ttk.Combobox(master, values=self.releaseYearOptions, state='readonly')
        self.releaseYear.grid(row=3, column=1, sticky="NSEW")

        # Add label and dropdown for color options
        self.addLabel(master, text="Color:", row=4, column=0)
        self.colorOptions = [
            "Black", "White", "Red", "Blue", "Green", "Yellow", "Pink", 
            "Purple", "Orange", "Brown", "Gray", "Silver", "Gold", 
            "Cyan", "Magenta", "Maroon", "Olive", "Navy", "Teal", 
            "Lavender", "Turquoise", "Beige", "Coral", "Crimson", 
            "Dark Blue", "Light Blue", "Dark Green", "Light Green", 
            "Dark Red", "Light Red", "Violet", "Indigo", "Mint", "Peach", 
            "Burgundy", "Sky Blue", "Lime", "Aquamarine", "Amber", 
            "Chocolate", "Plum", "Mauve", "Other"
        ]
        self.color = ttk.Combobox(master, values=self.colorOptions, state='readonly')
        self.color.grid(row=4, column=1, sticky="NSEW")

        # Add label and dropdown for condition options
        self.addLabel(master, text="Condition:", row=5, column=0)
        self.conditionOptions = ["New", "Like New", "Used - Good", "Used - Acceptable", "Other"]
        self.condition = ttk.Combobox(master, values=self.conditionOptions, state='readonly')
        self.condition.grid(row=5, column=1, sticky="NSEW")

        # Add label and dropdowns for purchase date (month, day, year)
        self.addLabel(master, text="Purchase Date:", row=6, column=0)
        self.monthOptions = [f"{month:02}" for month in range(1, 13)]
        self.dayOptions = [f"{day:02}" for day in range(1, 32)]
        self.yearOptions = [str(year) for year in reversed(range(1972, 2026))]
        self.purchaseMonth = ttk.Combobox(master, values=self.monthOptions, state='readonly')
        self.purchaseMonth.grid(row=6, column=1, sticky="NSEW")
        self.purchaseDay = ttk.Combobox(master, values=self.dayOptions, state='readonly', width=3)
        self.purchaseDay.grid(row=6, column=2, sticky="NSEW")
        self.purchaseYear = ttk.Combobox(master, values=self.yearOptions, state='readonly', width=5)
        self.purchaseYear.grid(row=6, column=3, sticky="NSEW")

        # Add label and entry for purchase price
        self.addLabel(master, text="Purchase Price:", row=7, column=0)
        self.purchasePrice = ttk.Entry(master)
        self.purchasePrice.grid(row=7, column=1, sticky="NSEW")
        
        if self.console:
            # Populate fields with existing console data if editing an existing entry
            self.consoleName.set(self.console["name"])
            self.storage.set(self.console["storage"])
            self.manufacturer.set(self.console["manufacturer"])
            self.releaseYear.set(self.console["release_year"])
            self.color.set(self.console["color"])
            self.condition.set(self.console["condition"])
            purchase_date = self.console["purchase_date"].split("-")
            self.purchaseMonth.set(purchase_date[0])
            self.purchaseDay.set(purchase_date[1])
            self.purchaseYear.set(purchase_date[2])
            self.purchasePrice.insert(0, self.console["purchase_price"])

        # Add Save and Cancel buttons
        self.addButton(master, text="Save", row=9, column=0, command=self.saveConsole)
        self.addButton(master, text="Cancel", row=9, column=1, command=self.cancel)

    def buttonbox(self):
        """Override this method to prevent the default OK/Cancel buttons from appearing.""" 
        pass

    def saveConsole(self):
        # Validate inputs, ensure all fields are filled
        if not self.consoleName.get() or not self.storage.get() or not self.manufacturer.get() or not self.purchaseDay.get() or not self.purchaseMonth.get() or not self.purchaseYear.get() or not self.purchasePrice.get():
            messagebox.showerror("Error", "All fields are required.")
            return

        # Save the console details to the parent list
        console = {
            "name": self.consoleName.get(), 
            "storage": self.storage.get(), 
            "manufacturer": self.manufacturer.get(), 
            "release_year": self.releaseYear.get(), 
            "color": self.color.get(), 
            "condition": self.condition.get(), 
            "purchase_date": f"{self.purchaseMonth.get()}-{self.purchaseDay.get()}-{self.purchaseYear.get()}", 
            "purchase_price": self.purchasePrice.get()
        }
        if self.console: 
            # Update existing console 
            self.collection[self.index] = console    
        else:
            # Add new console 
            self.collection.append(console)

        # Save the collection to file after adding or editing a console
        self.parent.updateCollection() 

        # Refresh the listbox display in the parent window if applicable
        if isinstance(self.parent, CollectionViewWindow): 
            self.parent.refresh_listbox()

        self.parent.messageBox("Info", "Console saved successfully.")
        self.destroy()

    def cancel(self):
        # Close the window without saving
        self.destroy()

class CollectionViewWindow(EasyDialog):
    def __init__(self, parent, collection):
        self.collection = collection
        # Store the index of the selected console
        self.selected_console_index = None

        # Initialize the dialog window with the title "Console Collection"
        EasyDialog.__init__(self, parent, "Console Collection")
        

    def body(self, master):
        # Add label for the collection title
        self.addLabel(master, text="Console Collection", row=0, column=0, columnspan=2)
        # Add label for the list headers
        self.addLabel(master, text="Name - Storage - Manufacturer - Release Year - Color - Condition - Purchase Date - Purchase Price", row=1, column=0, columnspan=2)

        # Display the list of consoles
        self.console_list_var = StringVar(value=[f"{console['name']} - {console['storage']} - {console['manufacturer']} - {console['release_year']} - {console['color']} - {console['condition']} - {console['purchase_date']} - ${console['purchase_price']}" for console in self.collection])        
        self.consoleList = Listbox(master, listvariable=self.console_list_var, height=10, width=60) 
        self.consoleList.grid(row=2, column=0, columnspan=2, sticky="NSEW") 
        self.consoleList.bind('<<ListboxSelect>>', self.on_console_select)

        # Add buttons for search, edit, delete, and back
        self.addButton(master, text="Search", row=3, column=0, command=self.searchConsole)
        self.addButton(master,text="Edit", row=3, column=1, command=self.editConsole)
        self.addButton(master, text="Delete", row=3, column=2, command=self.deleteConsole)
        self.addButton(master, text="Back", row=4, column=1, command=self.destroy)

    def refresh_listbox(self): 
        # Update the listbox with the latest console collection
        self.console_list_var.set([f"{console['name']} - {console['storage']} - {console['manufacturer']} - {console['release_year']} - {console['color']} - {console['condition']} - {console['purchase_date']} - ${console['purchase_price']}" for console in self.collection])
    
    def buttonbox(self):
        """Override this method to prevent the default OK/Cancel buttons from appearing.""" 
        pass

    def on_console_select(self, event):
        # Capture the index of the selected console
        selection = event.widget.curselection()
        if selection:
            self.selected_console_index = selection[0]

    def searchConsole(self):
        # Open the search console window
        SearchWindow(self, self.collection)

    def editConsole(self):
        # Edit the selected console if one is selected
        if self.selected_console_index is None:
            messagebox.showerror("Error", "No console selected.")
            return

        selected_console = self.collection[self.selected_console_index]
        AddConsoleWindow(self, collection=self.collection, console=selected_console, index=self.selected_console_index)

    def deleteConsole(self):
        # Delete the selected console if one is selected
        if self.selected_console_index is None:
            messagebox.showerror("Error", "No console selected.")
            return
        del self.collection[self.selected_console_index]
        self.refresh_listbox()
        self.parent.updateCollection()

        # Reset the selection
        self.selected_console_index = None 
        self.parent.messageBox("Info", "Console deleted successfully.")
    
    def updateCollection(self): 
        # Save the updated collection to a file or perform other update actions 
        homedir = os.path.expanduser("~") 
        filepath = os.path.join(homedir, "Downloads", "console_collection.txt") 
        with open(filepath, 'w') as file: 
            for console in self.collection: 
                file.write(f"{console['name']}|{console['storage']}|{console['manufacturer']}|{console['release_year']}|{console['color']}|{console['condition']}|{console['purchase_date']}|{console['purchase_price']}\n")
                      

class SearchWindow(EasyDialog):

    def __init__(self, parent, collection):
        # Store the collection to search
        self.collection = collection
        # Initialize the dialog window with the title "Search Collection"
        EasyDialog.__init__(self, parent, "Search Collection")

    def body(self, master):
        # Add label and dropdown for console name search
        self.addLabel(master, text="Search by Console Name:", row=0, column=0) 
        self.consoleOptions = ["PlayStation 5", "Xbox Series X", "Nintendo Switch", 
            "PlayStation 4", "Xbox One", "Wii", "NES", 
            "SNES", "Nintendo 64", "GameCube", "PlayStation 3", 
            "Xbox 360", "Wii U", "PlayStation 2", "Xbox", 
            "Sega Genesis", "Dreamcast", "Sega Saturn", 
            "PlayStation", "Atari 2600", "Atari 5200", 
            "Atari 7800", "ColecoVision", "Intellivision", 
            "Neo Geo", "TurboGrafx-16", "Game Boy", 
            "Game Boy Color", "Game Boy Advance", "PSP", 
            "PS Vita", "Nintendo DS", "Nintendo 3DS", "Other", ""] 
        self.consoleName = ttk.Combobox(master, values=self.consoleOptions, state='readonly') 
        self.consoleName.grid(row=0, column=1, sticky="NSEW") 

        # Add label and dropdown for manufacturer search
        self.addLabel(master, text="Manufacturer:", row=1, column=0) 
        self.manufacturerOptions = ["Sony", "Microsoft", "Nintendo", "Sega", 
            "Atari", "Coleco", "Mattel", "SNK", 
            "NEC", "Bandai", "Commodore", "Other", ""] 
        self.manufacturer = ttk.Combobox(master, values=self.manufacturerOptions, state='readonly') 
        self.manufacturer.grid(row=1, column=1, sticky="NSEW")
        
        # Add buttons for search and back
        self.addButton(master, text="Search", row=2, column=0, command=self.performSearch)
        self.addButton(master, text="Back", row=2, column=1, command=self.destroy)
        
        # Add text area for displaying search results
        self.results = self.addTextArea(master, text="", row=3, column=0, columnspan=2)
        # Disable editing 
        self.results.configure(state='disabled')

    def buttonbox(self):
        """Override this method to prevent the default OK/Cancel buttons from appearing.""" 
        pass

    def performSearch(self):
        # Perform search based on selected console name and/or manufacturer
        search_name = self.consoleName.get().lower()
        search_manufacturer = self.manufacturer.get().lower()

        if not search_name and not search_manufacturer:
            # If no search criteria are provided, return the entire collection
            results = self.collection

        elif search_name and search_manufacturer:
            # If both console name and manufacturer are provided, filter by both
            results = [console for console in self.collection if search_name == console['name'].lower() and search_manufacturer == console['manufacturer'].lower()]
        
        elif search_name:
            # If only console name is provided, filter by console name
            results = [console for console in self.collection if search_name == console['name'].lower()]
        
        elif search_manufacturer:
            # If only manufacturer is provided, filter by manufacturer
            results = [console for console in self.collection if search_manufacturer == console['manufacturer'].lower()]

        # Format the search results for display
        result_text = "\n".join([f"{console['name']} - {console['storage']} - {console['manufacturer']} - {console['release_year']} - {console['color']} - {console['condition']} - {console['purchase_date']} - ${console['purchase_price']}" for console in results])
        
        # Enable editing to update text 
        self.results.configure(state='normal') 

        # Clear current content 
        self.results.delete(1.0, 'end') 

        # Insert new content 
        self.results.insert('end', result_text if result_text else "No results found.") 

        # Disable editing again
        self.results.configure(state='disabled')
        
# Define a class called ReportsWindow that inherits from EasyDialog
class ReportsWindow(EasyDialog):

    # Initialize the ReportsWindow with a parent
    def __init__(self, parent):
        EasyDialog.__init__(self, parent, "Collection Reports")

    # Define the body of the ReportsWindow
    def body(self, master):
        # Add a label for "Report Type" at the specified grid position
        self.addLabel(master, text="Report Type:", row=0, column=0) 
        # Options for report type
        self.reportOptions = ["Yearly", "Monthly", "Weekly", "Custom"] 
        # Create a combobox for selecting report type
        self.reportType = ttk.Combobox(master, values=self.reportOptions, state='readonly') 
        self.reportType.grid(row=0, column=1, sticky="NSEW") 

        # Add a label for "Time Period" at the specified grid position
        self.addLabel(master, text="Time Period:", row=1, column=0) 
        # Options for time period
        self.timePeriodOptions = ["2020", "2021", "2022", "2023", "2024", "Other"] 
        # Create a combobox for selecting time period
        self.timePeriod = ttk.Combobox(master, values=self.timePeriodOptions, state='readonly') 
        self.timePeriod.grid(row=1, column=1, sticky="NSEW")
        
        # Add buttons for generating report and going back
        self.addButton(master, text="Generate Report", row=2, column=0, command=self.generateReport)
        self.addButton(master, text="Back", row=2, column=1, command=self.destroy)
        
        # Add a text area to display the report
        self.reportArea = self.addTextArea(master, text="", row=3, column=0, columnspan=2)

    # Override the buttonbox method to prevent default OK/Cancel buttons from appearing
    def buttonbox(self):
        pass

    # Define the function to generate report
    def generateReport(self):

        # Validate inputs to ensure all fields are filled
        if not self.reportType.get() or not self.timePeriod.get(): 
            messagebox.showerror("Error", "All fields are required.") 
            return

        # Placeholder for generating and displaying the report
        self.reportArea.setText("Report placeholder.")

# Define a class called GoalsWindow that inherits from EasyDialog
class GoalsWindow(EasyDialog):

    # Initialize the GoalsWindow with a parent
    def __init__(self, parent):
        EasyDialog.__init__(self, parent, "Set Collection Goals")

    # Define the body of the GoalsWindow
    def body(self, master):
        # Add a label for "Goal Name" at the specified grid position
        self.addLabel(master, text="Goal Name:", row=0, column=0)
        # Options for goal name
        self.goalOptions = ["Complete Collection", "Specific Console", "Limited Edition", "Other"] 
        # Create a combobox for selecting goal name
        self.goalName = ttk.Combobox(master, values=self.goalOptions, state='readonly') 
        self.goalName.grid(row=0, column=1, sticky="NSEW") 

        # Add a label for "Console/Accessory" at the specified grid position
        self.addLabel(master, text="Console/Accessory:", row=1, column=0) 
        # Options for console/accessory
        self.consoleOptions = [
            "PlayStation 5", "Xbox Series X", "Nintendo Switch", "PlayStation 4", "Xbox One", 
            "Wii", "NES", "SNES", "Nintendo 64", "GameCube", "PlayStation 3", "Xbox 360", 
            "Wii U", "PlayStation 2", "Xbox", "Sega Genesis", "Dreamcast", "Sega Saturn", 
            "PlayStation", "Atari 2600", "Atari 5200", "Atari 7800", "ColecoVision", 
            "Intellivision", "Neo Geo", "TurboGrafx-16", "Game Boy", "Game Boy Color", 
            "Game Boy Advance", "PSP", "PS Vita", "Nintendo DS", "Nintendo 3DS", "Other"
        ] 
        # Create a combobox for selecting console/accessory
        self.consoleAccessory = ttk.Combobox(master, values=self.consoleOptions, state='readonly') 
        self.consoleAccessory.grid(row=1, column=1, sticky="NSEW") 

        # Add a label for "Target Acquisition Date" at the specified grid position
        self.addLabel(master, text="Target Acquisition Date:", row=2, column=0) 
        # Options for target acquisition date
        self.targetDateOptions = ["2020", "2021", "2022", "2023", "2024", "Other"] 
        # Create a combobox for selecting target acquisition date
        self.targetDate = ttk.Combobox(master, values=self.targetDateOptions, state='readonly') 
        self.targetDate.grid(row=2, column=1, sticky="NSEW")
        
        # Add buttons for editing, saving, and going back
        self.addButton(master, text="Edit", row=3, column=0, command=self.editGoal)
        self.addButton(master, text="Save", row=3, column=1, command=self.saveGoal)
        self.addButton(master, text="Back", row=3, column=2, command=self.destroy)

    # Override the buttonbox method to prevent default OK/Cancel buttons from appearing
    def buttonbox(self):
        pass

    # Define the function to edit a goal
    def editGoal(self):
        # Placeholder for editing a goal
        self.parent.messageBox("Info", "Edit goal function.")

    # Define the function to save a goal
    def saveGoal(self):
        # Validate inputs to ensure all fields are filled
        if not self.goalName.get() or not self.consoleAccessory.get() or not self.targetDate.get():
            messagebox.showerror("Error", "All fields are required.")
            return

        # Placeholder for saving a goal
        self.parent.messageBox("Info", "Goal saved successfully.")
        self.destroy()

# Run the main loop of the main window
MainWindow().mainloop()