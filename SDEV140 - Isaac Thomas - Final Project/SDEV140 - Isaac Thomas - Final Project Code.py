# Import the EasyFrame and EasyDialog classes from the breezypythongui module.
from breezypythongui import EasyFrame, EasyDialog

# Import the PhotoImage class from the tkinter module for handling images.
from tkinter import PhotoImage

# Import the Listbox class from the tkinter module to create listbox widgets.
from tkinter import Listbox

# Import the StringVar class from the tkinter module to create string variables that can be used to manage the values of widgets.
from tkinter import StringVar

# Import the font module from tkinter to handle font settings for widgets.
from tkinter import font

# Import the messagebox module from tkinter to display message boxes.
from tkinter import messagebox

# Import the simpledialog module from tkinter to create simple dialog boxes.
from tkinter import simpledialog

# Import the ttk (themed tkinter) module from tkinter to create themed widgets, such as Combobox.
from tkinter import ttk

# Import the os module to interact with the operating system, such as file handling.
import os

class MainWindow(EasyFrame):

    def __init__(self):
        # Initialize the main window with a title
        EasyFrame.__init__(self, title="Game Vault Collector")
        self.setSize(500, 700)
        self.button_font = font.Font(size=14, weight='bold')

        # Set the background color of the window 
        self["background"] = "#3c507a"

        # Add welcome and instruction labels
        self.addLabel(text="Welcome to Game Vault Collector", row=0, column=0, columnspan=2, sticky="NSEW", font=self.button_font)
        self.addLabel(text="Please select an option below:", row=2, column=0, columnspan=2, sticky="NSEW", font=self.button_font)

        # Add buttons for different functionalities
        self.addConsoleButton = self.addButton(text="Add Console", row=4, column=0, command=self.addConsole)
        self.viewCollectionButton = self.addButton(text="View Collection", row=4, column=1, command=self.viewCollection)
        self.exitButton = self.addButton(text="Exit", row=5, column=0, columnspan=2, command=self.quit)

        self.addConsoleButton.configure(width=20, height=2, font=self.button_font)
        self.viewCollectionButton.configure(width=20, height=2, font=self.button_font)
        self.exitButton.configure(width=20, height=2, font=self.button_font)


        
        # Determine the path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Add logo and icons (placeholders for now)
        imageLabel = self.addLabel(text="", row=1, column=0, columnspan=2)
        self.logo = PhotoImage(file=os.path.join(script_dir, "logo.png"))
        imageLabel["image"] = self.logo

        try:
            imageGameIcon = self.addLabel(text="Console Icon", row=3, column=0)
            self.gameIcon = PhotoImage(file=os.path.join(script_dir, "gameIcon.png"))
            self.resizedGameImage = self.gameIcon.subsample(5, 5)  # Adjust the subsample factors as needed
            imageGameIcon["image"] = self.resizedGameImage
        except:
            return

        try:
            imageSearchIcon = self.addLabel(text="Search Icon", row=3, column=1)
            self.searchIcon = PhotoImage(file=os.path.join(script_dir, "SearchIcon.png"))
            self.resizedImageSearchIcon = self.searchIcon.subsample(5, 5)  # Adjust the subsample factors as needed
            imageSearchIcon["image"] = self.resizedImageSearchIcon
        except:
            return

        # Set the images with alternate text 
        imageGameIcon["image"] = self.resizedGameImage
        imageGameIcon["text"] = "Game Icon"
        imageSearchIcon["image"] = self.resizedImageSearchIcon
        imageSearchIcon["text"] = "Search Image"

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
        # Define a bold font for buttons
        self.button_font = font.Font(size=14, weight='bold')

        # Define the mapping of console details (name, manufacturer, and release year)
        self.consoleDetails = {
            "PlayStation 5": {"manufacturer": "Sony", "release_year": "2020"},
            "Xbox Series X": {"manufacturer": "Microsoft", "release_year": "2020"},
            "Nintendo Switch": {"manufacturer": "Nintendo", "release_year": "2017"},
            "PlayStation 4": {"manufacturer": "Sony", "release_year": "2013"},
            "Xbox One": {"manufacturer": "Microsoft", "release_year": "2013"},
            "Wii": {"manufacturer": "Nintendo", "release_year": "2006"},
            "NES": {"manufacturer": "Nintendo", "release_year": "1983"},
            "SNES": {"manufacturer": "Nintendo", "release_year": "1990"},
            "Nintendo 64": {"manufacturer": "Nintendo", "release_year": "1996"},
            "GameCube": {"manufacturer": "Nintendo", "release_year": "2001"},
            "PlayStation 3": {"manufacturer": "Sony", "release_year": "2006"},
            "Xbox 360": {"manufacturer": "Microsoft", "release_year": "2005"},
            "Wii U": {"manufacturer": "Nintendo", "release_year": "2012"},
            "PlayStation 2": {"manufacturer": "Sony", "release_year": "2000"},
            "Xbox": {"manufacturer": "Microsoft", "release_year": "2001"},
            "Sega Genesis": {"manufacturer": "Sega", "release_year": "1988"},
            "Dreamcast": {"manufacturer": "Sega", "release_year": "1999"},
            "Sega Saturn": {"manufacturer": "Sega", "release_year": "1994"},
            "PlayStation": {"manufacturer": "Sony", "release_year": "1994"},
            "Atari 2600": {"manufacturer": "Atari", "release_year": "1977"},
            "Atari 5200": {"manufacturer": "Atari", "release_year": "1982"},
            "Atari 7800": {"manufacturer": "Atari", "release_year": "1986"},
            "ColecoVision": {"manufacturer": "Coleco", "release_year": "1982"},
            "Intellivision": {"manufacturer": "Mattel", "release_year": "1979"},
            "Neo Geo": {"manufacturer": "SNK", "release_year": "1990"},
            "TurboGrafx-16": {"manufacturer": "NEC", "release_year": "1987"},
            "Game Boy": {"manufacturer": "Nintendo", "release_year": "1989"},
            "Game Boy Color": {"manufacturer": "Nintendo", "release_year": "1998"},
            "Game Boy Advance": {"manufacturer": "Nintendo", "release_year": "2001"},
            "PSP": {"manufacturer": "Sony", "release_year": "2004"},
            "PS Vita": {"manufacturer": "Sony", "release_year": "2011"},
            "Nintendo DS": {"manufacturer": "Nintendo", "release_year": "2004"},
            "Nintendo 3DS": {"manufacturer": "Nintendo", "release_year": "2011"},
        }

        self.previous_manufacturer = ""  # Store the previous selected manufacturer
        self.previous_release_year = ""  # Store the previous selected release year
 
        # Initialize the dialog window with the title based on whether it's an edit or add operation
        title = "Edit Gaming Console" if console else "Add Gaming Console"
        EasyDialog.__init__(self, parent, title)
        

    def body(self, master):
        # Add label and dropdown for console name
        self.addLabel(master, text="Console Name:", row=0, column=0, font=self.button_font)
        self.consoleOptions = list(self.consoleDetails.keys()) + ["Other"]
        self.consoleName = ttk.Combobox(master, values=self.consoleOptions, state='readonly', font=self.button_font)
        self.consoleName.grid(row=0, column=1, sticky="NSEW")
        self.consoleName.bind("<<ComboboxSelected>>", self.onConsoleSelected)

        # Add label and dropdown for storage options
        self.addLabel(master, text="Storage on device:", row=1, column=0, font=self.button_font)
        self.storageOptions = ["",
            "None", "128MB", "256MB", "512MB", 
            "1GB", "2GB", "4GB", "8GB", "16GB", 
            "32GB", "64GB", "128GB", "256GB", 
            "500GB", "1TB", "2TB", "4TB", "Other"
        ]
        self.storage = ttk.Combobox(master, values=self.storageOptions, state='readonly', font=self.button_font)
        self.storage.grid(row=1, column=1, sticky="NSEW")

        # Add label and dropdown for manufacturer options
        self.addLabel(master, text="Manufacturer:", row=2, column=0, font=self.button_font)
        self.manufacturerOptions = [
            "Sony", "Microsoft", "Nintendo", "Sega", 
            "Atari", "Coleco", "Mattel", "SNK", 
            "NEC", "Commodore", "Other"
        ]
        self.manufacturer = ttk.Combobox(master, values=self.manufacturerOptions, state='readonly', font=self.button_font)
        self.manufacturer.grid(row=2, column=1, sticky="NSEW")
        self.manufacturer.bind("<<ComboboxSelected>>", self.onManufacturerSelected)

        # Add label and dropdown for release year options
        self.addLabel(master, text="Release Year:", row=3, column=0, font=self.button_font)
        self.releaseYearOptions = [""] + [str(madeyear) for madeyear in reversed(range(1972, 2026))]
        self.releaseYear = ttk.Combobox(master, values=self.releaseYearOptions, state='readonly', font=self.button_font)
        self.releaseYear.grid(row=3, column=1, sticky="NSEW")
        self.releaseYear.bind("<<ComboboxSelected>>", self.onReleaseYearSelected)

        # Add label and dropdown for color options
        self.addLabel(master, text="Color:", row=4, column=0, font=self.button_font)
        self.colorOptions = [ "",
            "Black", "White", "Red", "Blue", "Green", "Yellow", "Pink", 
            "Purple", "Orange", "Brown", "Gray", "Silver", "Gold", 
            "Cyan", "Magenta", "Maroon", "Olive", "Navy", "Teal", 
            "Lavender", "Turquoise", "Beige", "Coral", "Crimson", 
            "Dark Blue", "Light Blue", "Dark Green", "Light Green", 
            "Dark Red", "Light Red", "Violet", "Indigo", "Mint", "Peach", 
            "Burgundy", "Sky Blue", "Lime", "Aquamarine", "Amber", 
            "Chocolate", "Plum", "Mauve", "Other"
        ]
        self.color = ttk.Combobox(master, values=self.colorOptions, state='readonly', font=self.button_font)
        self.color.grid(row=4, column=1, sticky="NSEW")

        # Add label and dropdown for condition options
        self.addLabel(master, text="Condition:", row=5, column=0, font=self.button_font)
        self.conditionOptions = ["","New", "Like New", "Used - Good", "Used - Acceptable", "Other"]
        self.condition = ttk.Combobox(master, values=self.conditionOptions, state='readonly', font=self.button_font)
        self.condition.grid(row=5, column=1, sticky="NSEW")

        # Add label and dropdowns for purchase date (month, day, year)
        self.addLabel(master, text="Purchase Date:", row=6, column=0, font=self.button_font)
        self.monthOptions = [""] + [f"{month:02}" for month in range(1, 13)]
        self.dayOptions = [""] + [f"{day:02}" for day in range(1, 32)]
        self.yearOptions = [""] + [str(year) for year in reversed(range(1972, 2026))]
        self.purchaseMonth = ttk.Combobox(master, values=self.monthOptions, state='readonly', width=3, font=self.button_font)
        self.purchaseMonth.grid(row=6, column=1, sticky="NSEW")
        self.purchaseDay = ttk.Combobox(master, values=self.dayOptions, state='readonly', width=3, font=self.button_font)
        self.purchaseDay.grid(row=6, column=2, sticky="NSEW")
        self.purchaseYear = ttk.Combobox(master, values=self.yearOptions, state='readonly', width=5, font=self.button_font)
        self

    def buttonbox(self):
        # Override this method to prevent the default OK/Cancel buttons from appearing.
        pass

    def onConsoleSelected(self, event):
        # Get the selected console name from the dropdown
        console_name = self.consoleName.get()
        if console_name == "Other":
            # If "Other" is selected, show all valid manufacturers for the selected release year
            valid_manufacturers = set(
                details["manufacturer"] for name, details in self.consoleDetails.items()
                if details["release_year"] == self.releaseYear.get()
            )
            self.manufacturer["values"] = list(valid_manufacturers) + ["Other"]
        elif console_name in self.consoleDetails:
            # If a known console is selected, update manufacturer and release year based on console details
            details = self.consoleDetails[console_name]
            if self.manufacturer.get() != details["manufacturer"]:
                self.manufacturer.set(details["manufacturer"])
                self.previous_manufacturer = details["manufacturer"]
            if self.releaseYear.get() != details["release_year"]:
                self.releaseYear.set(details["release_year"])

            # Show only the valid manufacturer
            manufacturers = {details["manufacturer"]}
            self.manufacturer["values"] = list(manufacturers) + ["Other"]
        else:
            # If no console or an unknown console is selected, clear manufacturer and release year
            self.manufacturer.set("")
            self.releaseYear.set("")
            self.updateManufacturerOptions(self.releaseYear.get())

    def onManufacturerSelected(self, event):
        # Get the selected manufacturer from the dropdown
        manufacturer = self.manufacturer.get()
        if manufacturer == "Other":
            # If "Other" is selected, show all valid consoles for the selected release year
            valid_consoles = [
                name for name, details in self.consoleDetails.items()
                if details["release_year"] == self.releaseYear.get()
            ]
            self.consoleName.set("Other")
            self.consoleName["values"] = valid_consoles + ["Other"]
        else:
            # Show only the consoles from the selected manufacturer for the selected release year
            valid_consoles = [
                name for name, details in self.consoleDetails.items()
                if details["manufacturer"] == manufacturer and (self.releaseYear.get() == "" or details["release_year"] == self.releaseYear.get())
            ]
            self.consoleName.set("")
            self.consoleName["values"] = valid_consoles + ["Other"]
            self.previous_manufacturer = manufacturer

    def onReleaseYearSelected(self, event):
        # Get the selected release year from the dropdown
        selected_year = self.releaseYear.get()
        if selected_year == "":
            # If no release year is selected, reset console and manufacturer options
            self.consoleName["values"] = list(self.consoleDetails.keys()) + ["Other"]
            self.manufacturer["values"] = list(self.manufacturerOptions)
            self.consoleName.set("")
            self.manufacturer.set("")
            self.previous_release_year = ""
            self.previous_manufacturer = ""
            return
        # Show only the consoles and manufacturers for the selected release year
        valid_consoles = [
            name for name, details in self.consoleDetails.items()
            if details["release_year"] == selected_year
        ]
        self.consoleName["values"] = valid_consoles + ["Other"]

        # Update manufacturers to include all valid options for the selected year
        manufacturers = set(
            details["manufacturer"] for name, details in self.consoleDetails.items()
            if details["release_year"] == selected_year
        )
        self.manufacturer["values"] = list(manufacturers) + ["Other"]

        self.previous_release_year = selected_year

    def updateConsoleOptions(self, year):
        # Update console options based on the selected release year
        valid_consoles = [
            name for name, details in self.consoleDetails.items()
            if details["release_year"] == year
        ]
        self.consoleName["values"] = valid_consoles + ["Other"]

    def updateManufacturerOptions(self, year):
        # Update manufacturer options based on the selected release year
        manufacturers = set(
            details["manufacturer"] for name, details in self.consoleDetails.items()
            if details["release_year"] == year
        )
        self.manufacturer["values"] = list(manufacturers) + ["Other"]

    def saveConsole(self):
        # Validate inputs, ensure all fields are filled 
        missing_fields = [] 
        if not self.consoleName.get(): 
            missing_fields.append("Console Name") 
        if not self.storage.get(): 
            missing_fields.append("Storage on device") 
        if not self.manufacturer.get(): 
            missing_fields.append("Manufacturer") 
        if not self.releaseYear.get(): 
            missing_fields.append("Release Year") 
        if not self.color.get(): 
            missing_fields.append("Color") 
        if not self.condition.get(): 
            missing_fields.append("Condition") 
        if not self.purchaseMonth.get() or not self.purchaseDay.get() or not self.purchaseYear.get():
            missing_fields.append("Purchase Date") 
        if not self.purchasePrice.get(): 
            missing_fields.append("Purchase Price") 
        
        # If there are missing fields, show an error message and stop
        if missing_fields: 
            messagebox.showerror("Error", f"The following fields are required:\n- " + "\n- ".join(missing_fields)) 
            return 
        
        # Additional validation: Ensure purchase price is a valid number 
        try: 
            # Try to convert purchase price to a float
            purchase_price = float(self.purchasePrice.get()) 
            # Check if purchase price is a valid number greater than or equal to 0
            if purchase_price < 0:
                raise ValueError("Purchase Price must be a number greater than or equal to 0.")
        except ValueError: 
            # Show an error message if conversion fails
            messagebox.showerror("Error", "Purchase Price must be a number greater than or equal to 0.") 
            return
        
        # Create a dictionary with the console details
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
        
        # If updating an existing console, replace it in the collection
        if self.console: 
            self.collection[self.index] = console    
        else:
            # If adding a new console, append it to the collection
            self.collection.append(console)

        # Save the updated collection to file
        self.parent.updateCollection() 

        # Refresh the listbox display in the parent window if applicable
        if isinstance(self.parent, CollectionViewWindow): 
            self.parent.refresh_listbox()

        # Show a success message and close the window
        self.parent.messageBox("Info", "Console saved successfully.")
        self.destroy()

    def cancel(self):
        # Close the window without saving
        self.destroy()

    def clearFields(self):
        # Method to reset all fields to their default states.
        self.consoleName.set("") 
        self.consoleName["values"] = list(self.consoleDetails.keys()) + ["Other"] 
        self.storage.set("") 
        self.manufacturer.set("") 
        self.manufacturer["values"] = self.manufacturerOptions 
        self.releaseYear.set("") 
        self.color.set("") 
        self.condition.set("") 
        self.purchaseMonth.set("") 
        self.purchaseDay.set("") 
        self.purchaseYear.set("") 
        self.purchasePrice.delete(0, 'end')


class CollectionViewWindow(EasyDialog):
    def __init__(self, parent, collection):
        # Initialize the CollectionViewWindow with the parent and collection of consoles
        self.collection = collection
        self.selected_console_index = None  # Track the selected console's index
        self.undo = None  # Store the last deleted console for undo functionality
        self.tree_font = font.Font(family="Helvetica", size=12)  # Define font for tree view
        self.button_font = font.Font(size=14, weight='bold')  # Define bold font for buttons

        # Initialize the EasyDialog with the title "Console Collection"
        EasyDialog.__init__(self, parent, "Console Collection")

    def body(self, master):
        # Add a label for the window title
        self.addLabel(master, text="Console Collection", row=0, column=0, columnspan=2, font=self.button_font)
        # Add a label for the console data section
        self.addLabel(master, text="Console Data", row=1, column=0, columnspan=2, font=self.button_font)

        # Configure styles for the tree view headings and content
        style = ttk.Style() 
        style.configure("Treeview.Heading", font=self.tree_font) 
        style.configure("Treeview", font=self.tree_font)
        
        # Create a tree view widget to display console data in columns
        self.tree = ttk.Treeview(master, columns=("Name", "Storage", "Manufacturer", "Release Year", "Color", "Condition", "Purchase Date", "Purchase Price"), show='headings')
        self.tree.heading("Name", text="Name")
        self.tree.heading("Storage", text="Storage")
        self.tree.heading("Manufacturer", text="Manufacturer")
        self.tree.heading("Release Year", text="Release Year")
        self.tree.heading("Color", text="Color")
        self.tree.heading("Condition", text="Condition")
        self.tree.heading("Purchase Date", text="Purchase Date")
        self.tree.heading("Purchase Price", text="Purchase Price")

        # Set column properties (alignment and width)
        self.tree.column("Name", anchor="center", width=150)
        self.tree.column("Storage", anchor="center", width=150)
        self.tree.column("Manufacturer", anchor="center", width=150)
        self.tree.column("Release Year", anchor="center", width=150)
        self.tree.column("Color", anchor="center", width=150)
        self.tree.column("Condition", anchor="center", width=150)
        self.tree.column("Purchase Date", anchor="center", width=150)
        self.tree.column("Purchase Price", anchor="center", width=150)

        # Insert each console's data into the tree view
        for console in self.collection:
            self.tree.insert("", "end", values=(
                console['name'], console['storage'], console['manufacturer'],
                console['release_year'], console['color'], console['condition'],
                console['purchase_date'], f"${console['purchase_price']}"
            ))

        # Add the tree view to the grid
        self.tree.grid(row=2, column=0, columnspan=6, sticky="NSEW")

        # Bind the selection event to the on_console_select method
        self.tree.bind('<<TreeviewSelect>>', self.on_console_select)

        # Add buttons for various actions and configure their properties
        self.searchConsoleButton = self.addButton(master, text="Search", row=3, column=1, command=self.searchConsole)
        self.editConsoleButton = self.addButton(master, text="Edit", row=3, column=2, command=self.editConsole)
        self.deleteConsoleButton = self.addButton(master, text="Delete", row=3, column=3, command=self.deleteConsole)
        self.undoButton = self.addButton(master, text="Undo Previous Action", row=3, column=4, command=self.undoDelete)
        self.backButton = self.addButton(master, text="Back", row=3, column=5, command=self.destroy)

        for button in [self.searchConsoleButton, self.editConsoleButton, self.deleteConsoleButton, self.undoButton, self.backButton]:
            button.configure(width=20, height=2, font=self.button_font)

    def refresh_listbox(self):
        # Sort the collection by console name
        self.sorted_collection = sorted(self.collection, key=lambda console: console['name'].lower())
        # Clear the current items in the tree view
        for i in self.tree.get_children():
            self.tree.delete(i)
        # Insert the sorted items into the tree view
        for console in self.sorted_collection:
            self.tree.insert("", "end", values=(
                console['name'], console['storage'], console['manufacturer'],
                console['release_year'], console['color'], console['condition'],
                console['purchase_date'], f"${console['purchase_price']}"
            ))

    def buttonbox(self):
        # Override this method to prevent default OK/Cancel buttons from appearing
        pass

    def on_console_select(self, event):
        # Capture the index of the selected console
        selected_item = self.tree.selection()
        if selected_item:
            self.selected_console_index = int(self.tree.index(selected_item[0]))

    def searchConsole(self):
        # Open the search window
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
        # Confirm the deletion
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this console?"):
            self.undo = self.collection[self.selected_console_index]
            del self.collection[self.selected_console_index]
            self.refresh_listbox()
            self.parent.updateCollection()
            self.selected_console_index = None 
            self.parent.messageBox("Info", "Console deleted successfully.")
    
    def undoDelete(self):
        # Undo the deletion of the last deleted console
        if self.undo:
            self.collection.append(self.undo)
            self.sorted_collection = sorted(self.collection, key=lambda console: console['name'].lower())
            self.refresh_listbox()
            self.parent.updateCollection()
            self.undo = None
            self.parent.messageBox("Info", "Deletion undone.")
    
    def updateCollection(self):
        # Sort the collection by console name before writing to the file
        self.sorted_collection = sorted(self.collection, key=lambda console: console['name'].lower())
    
        # Write the sorted collection to the file
        homedir = os.path.expanduser("~") 
        filepath = os.path.join(homedir, "Downloads", "console_collection.txt")
        with open(filepath, 'w') as file:
            for console in self.sorted_collection:
                file.write(f"{console['name']}|{console['storage']}|{console['manufacturer']}|{console['release_year']}|{console['color']}|{console['condition']}|{console['purchase_date']}|{console['purchase_price']}\n")

class SearchWindow(EasyDialog):

    def __init__(self, parent, collection):
        # Initialize the search window with a parent and a collection of consoles
        self.collection = collection
        # Define a bold font for buttons
        self.button_font = font.Font(size=14, weight='bold')
        # Initialize the EasyDialog with the title "Search Collection"
        EasyDialog.__init__(self, parent, "Search Collection")

    def body(self, master):
        # Add a label for searching by console name
        self.addLabel(master, text="Search by Console Name:", row=0, column=0, font=self.button_font)
        # List of console options for the dropdown menu
        self.consoleOptions = ["", "PlayStation 5", "Xbox Series X", "Nintendo Switch",
            "PlayStation 4", "Xbox One", "Wii", "NES",
            "SNES", "Nintendo 64", "GameCube", "PlayStation 3",
            "Xbox 360", "Wii U", "PlayStation 2", "Xbox",
            "Sega Genesis", "Dreamcast", "Sega Saturn",
            "PlayStation", "Atari 2600", "Atari 5200",
            "Atari 7800", "ColecoVision", "Intellivision",
            "Neo Geo", "TurboGrafx-16", "Game Boy",
            "Game Boy Color", "Game Boy Advance", "PSP",
            "PS Vita", "Nintendo DS", "Nintendo 3DS", "Other"]
        # Create a dropdown menu for selecting a console name
        self.consoleName = ttk.Combobox(master, values=self.consoleOptions, state='readonly', font=self.button_font)
        self.consoleName.grid(row=0, column=1, sticky="NSEW")

        # Add a label for selecting the manufacturer
        self.addLabel(master, text="Manufacturer:", row=1, column=0, font=self.button_font)
        # List of manufacturer options for the dropdown menu
        self.manufacturerOptions = ["", "Sony", "Microsoft", "Nintendo", "Sega",
            "Atari", "Coleco", "Mattel", "SNK",
            "NEC", "Commodore", "Other"]
        # Create a dropdown menu for selecting the manufacturer
        self.manufacturer = ttk.Combobox(master, values=self.manufacturerOptions, state='readonly', font=self.button_font)
        self.manufacturer.grid(row=1, column=1, sticky="NSEW")

        # Add a "Search" button and a "Back" button
        self.perfromSearchButton = self.addButton(master, text="Search", row=2, column=0, command=self.performSearch)
        self.destroyButton = self.addButton(master, text="Back", row=2, column=1, command=self.destroy)

        # Configure button size and font
        for button in [self.perfromSearchButton, self.destroyButton]:
            button.configure(width=20, height=2, font=self.button_font)

        # Create a tree view to display search results in a grid format
        self.tree = ttk.Treeview(master, columns=("Name", "Storage", "Manufacturer", "Release Year", "Color", "Condition", "Purchase Date", "Purchase Price"), show='headings')
        self.tree.heading("Name", text="Name")
        self.tree.heading("Storage", text="Storage")
        self.tree.heading("Manufacturer", text="Manufacturer")
        self.tree.heading("Release Year", text="Release Year")
        self.tree.heading("Color", text="Color")
        self.tree.heading("Condition", text="Condition")
        self.tree.heading("Purchase Date", text="Purchase Date")
        self.tree.heading("Purchase Price", text="Purchase Price")

        # Set column properties
        self.tree.column("Name", anchor="center", width=150)
        self.tree.column("Storage", anchor="center", width=150)
        self.tree.column("Manufacturer", anchor="center", width=150)
        self.tree.column("Release Year", anchor="center", width=150)
        self.tree.column("Color", anchor="center", width=150)
        self.tree.column("Condition", anchor="center", width=150)
        self.tree.column("Purchase Date", anchor="center", width=150)
        self.tree.column("Purchase Price", anchor="center", width=150)

        # Display the tree view on the grid
        self.tree.grid(row=3, column=0, columnspan=2, sticky="NSEW")

    def buttonbox(self):
        # Override this method to prevent default OK/Cancel buttons from appearing
        pass

    def performSearch(self):
        # Get search criteria from the dropdown menus
        search_name = self.consoleName.get().lower()
        search_manufacturer = self.manufacturer.get().lower()

        # Determine the search results based on criteria
        if not search_name and not search_manufacturer:
            results = self.collection
        elif search_name and search_manufacturer:
            results = [console for console in self.collection if search_name == console['name'].lower() and search_manufacturer == console['manufacturer'].lower()]
        elif search_name:
            results = [console for console in self.collection if search_name == console['name'].lower()]
        elif search_manufacturer:
            results = [console for console in self.collection if search_manufacturer == console['manufacturer'].lower()]

        # Clear the current content in the tree view
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        # Insert the search results into the tree view
        for console in results:
            self.tree.insert("", "end", values=(
                console['name'], console['storage'], console['manufacturer'],
                console['release_year'], console['color'], console['condition'],
                console['purchase_date'], f"${console['purchase_price']}"
            ))

# Run the main loop of the main window
MainWindow().mainloop()