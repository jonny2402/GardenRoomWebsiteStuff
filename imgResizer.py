import os
from tkinter import *
from PIL import Image, ImageTk
import gzip
import os
from tkinter import *
from PIL import Image, ImageTk


"""
This script contains two classes: GardenRoomResizer and GardenRoomApp.

The GardenRoomResizer class is used to resize and save images for a specific garden room, and create related text files. It has the following methods:
- __init__(): initializes the class attributes.
- set_garden_room(gr_number): sets the garden room number and image files for the class instance.
- set_favourite_image(fav_position): sets the favourite image position for the class instance.
- set_location(location): sets the location for the class instance.
- set_dimensions(dimensions): sets the dimensions for the class instance.
- resize_images(): resizes the garden room images and saves them to the appropriate directories.

The GardenRoomApp class is used to create a GUI that interacts with the GardenRoomResizer class. It has the following methods:
- __init__(master): initializes the GUI window and its widgets.
- get_garden_room_folders(): returns a list of garden room numbers found in the current directory.
- load_images(): loads the images for the selected garden room number.
- create_image_grid(): creates a grid of thumbnail images for the selected garden room.
- select_favourite_image(fav_position): selects the favourite image for the garden room.
- resize_images(): resizes the garden room images and updates the appropriate directories.
"""


class GardenRoomResizer:
    def __init__(self):
        self.gr_number = None
        self.fav_position = None
        self.image_files = []
        self.location = ""
        self.dimensions = ""

    def set_garden_room(self, gr_number):
        self.gr_number = gr_number
        gr_folder = f"GardenRoom{gr_number}"
        self.image_files = [f for f in os.listdir(gr_folder) if f.lower().endswith(".jpg")]

    def set_favourite_image(self, fav_position):
        self.fav_position = fav_position

    def set_location(self, location):
        self.location = location

    def set_dimensions(self, dimensions):
        self.dimensions = dimensions

    def resize_images(self):
        if self.gr_number is None or self.fav_position is None:
            return

        gr_folder = f"GardenRoom{self.gr_number}"
        os.makedirs("TestimonialsTODO", exist_ok=True)
        os.makedirs("Gallery", exist_ok=True)
        os.makedirs("Home", exist_ok=True)
        os.makedirs(f"Gallery/{gr_folder}", exist_ok=True)

        first_image_path = os.path.join(gr_folder, self.image_files[self.fav_position])
        resized_image_500 = self.resize_image(first_image_path, 500)
        resized_image_1366 = self.resize_image(first_image_path, 1366)
        new_image_file = f"GardenRoom{self.gr_number}.jpg"
        new_text_file = os.path.splitext(new_image_file)[0] + ".txt"

        with open(os.path.join("TestimonialsTODO", new_text_file), 'w') as f:
            f.write("<h4></h4>\n<br/><br/>\n<p>\nWrite\n<br/>\nText\n<br/>\nHere\n<br/>\n</p>\n")


        with open(os.path.join("Gallery", gr_folder, "title.txt"), "w") as f:
            f.write(f"<h2>{self.location} - {self.dimensions} Garden Room</h2>")


        with open(os.path.join("Gallery", new_text_file), "w") as f:
            f.write("<p></p>")

        resized_image_500.save(os.path.join("TestimonialsTODO", new_image_file))
        resized_image_500.save(os.path.join("Gallery", new_image_file))
        #resized_image_500.save(os.path.join("Gallery", gr_folder, f"GardenRoom{self.gr_number}.jpg"))
        resized_image_1366.save(os.path.join("Home", new_image_file))
        
        for i, image_file in enumerate(self.image_files):
            image_path = os.path.join(gr_folder, image_file)
            resized_image = self.resize_image(image_path, 1080)
            new_image_file = f"GardenRoom{i+1:02d}.jpg"
            resized_image.save(os.path.join(f"Gallery/{gr_folder}", new_image_file))
        

    def resize_image(self, image_path, width):
        with Image.open(image_path) as image:
            height = int((float(width) / image.size[0]) * image.size[1])
            return image.resize((width, height), Image.LANCZOS)

class GardenRoomApp:
    def __init__(self, master):
        self.master = master
        master.title("Garden Room Image Resizer")

        self.resizer = GardenRoomResizer()

        # Create input field for Garden Room Location
        Label(master, text="Location:").grid(row=0, sticky=E)
        self.location_entry = Entry(master)
        self.location_entry.grid(row=0, column=1)

        # Create input field for Garden Room Dimensions
        Label(master, text="Dimensions:").grid(row=1, sticky=E)
        self.dimensions_entry = Entry(master)
        self.dimensions_entry.grid(row=1, column=1)

        # Create input field for Garden Room Number
        Label(master, text="Garden Room Number:").grid(row=2, sticky=E)
        self.gr_number_var = StringVar(value=self.get_garden_room_folders()[0])
        self.gr_number_dropdown = OptionMenu(master, self.gr_number_var, *self.get_garden_room_folders())
        self.gr_number_dropdown.grid(row=2, column=1)

        # Create a button to load images for the given Garden Room Number
        self.load_images_button = Button(master, text="Load Images", command=self.load_images)
        self.load_images_button.grid(row=2, column=2)

        # Create a grid of all images in the Garden Room directory
        self.image_grid = Frame(master)
        self.image_grid.grid(row=3, column=0, columnspan=3)

        # Create a button to initiate image resizing
        self.resize_button = Button(master, text="Resize Images", command=self.resize_images)
        self.resize_button.grid(row=4, column=1)

    def get_garden_room_folders(self):
        garden_room_folders = [f for f in os.listdir() if os.path.isdir(f) and f.startswith("GardenRoom")]
        garden_room_numbers = [f.replace("GardenRoom", "") for f in garden_room_folders]
        garden_room_numbers.sort()
        return garden_room_numbers

    def load_images(self):
        gr_number = self.gr_number_var.get()
        self.resizer.set_garden_room(gr_number)

        if self.resizer.image_files:
            self.create_image_grid()

    def create_image_grid(self):
        # Destroy the current image grid if it exists
        for child in self.image_grid.winfo_children():
            child.destroy()

        # Create a grid of all images in the Garden Room directory
        for i, image_file in enumerate(self.resizer.image_files):
            image_path = os.path.join(f"GardenRoom{self.resizer.gr_number}", image_file)
            image = Image.open(image_path)
            image.thumbnail((150, 150))
            photo = ImageTk.PhotoImage(image)
            label = Label(self.image_grid, image=photo)
            label.photo = photo
            label.grid(row=i // 4, column=i % 4)

            # Bind image click event to select favourite image
            label.bind("<Button-1>", lambda e, i=i: self.select_favourite_image(i))

    def select_favourite_image(self, fav_position):
        self.resizer.set_favourite_image(fav_position)

        # Deselect all other images in the grid
        for label in self.image_grid.winfo_children():
            label.configure(bg=self.image_grid.cget("bg"))

        # Highlight the selected image in the grid
        selected_label = self.image_grid.winfo_children()[fav_position]
        selected_label.configure(bg="lightblue")

    def resize_images(self):
        self.resizer.set_location(self.location_entry.get())
        self.resizer.set_dimensions(self.dimensions_entry.get())
        self.resizer.resize_images()

if __name__ == "__main__":
    root = Tk()
    GardenRoomApp(root)
    root.mainloop()
