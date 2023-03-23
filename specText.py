import tkinter as tk
from tkinter import filedialog

"""
This script generates a text file containing specifications for a garden room.
The user inputs various parameters such as dimensions, cladding type, and lighting options, and the script
generates a formatted text file containing the specifications.

To use this script, simply run the file and fill out the various input fields in the GUI. Then click
the "Save File" button to generate the text file with the specified parameters.

Required Packages:
- tkinter
- filedialog

Usage:
- Run this script in a Python environment
- Fill out the various input fields in the GUI
- Click the "Save File" button to generate the text file with the specified parameters.

Functions:
- add_windoor_entry: Adds a new entry field for a windoor option
- create_text_file: Generates the text file with the specified parameters
- main: Runs the GUI

Note:
This script requires the tkinter and filedialog packages, which are included in most Python distributions.
"""


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gallery Spec Generator")

    def add_windoor_entry():
        windoor_text_entries.append(tk.Entry(windoor_frame, width=30))
        windoor_text_entries[-1].pack()

    def create_text_file():
    # Open file dialog to select a file name and location
        default_file_name = garden_room_number_input.get() + ".txt"
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_file_name)
        if file_path:
            # Get user inputs for file contents

    # Get user inputs for file contents
            garden_room_number = garden_room_number_input.get()
            dimensions_x = dimensions_x_input.get()
            dimensions_y = dimensions_y_input.get()
            canopy_cube = "Canopy" if canopy_cube_var.get() else "Cube"
            cladding_option = cladding_option_var.get()
            trim_option = "Anthracite Grey" if trim_var.get() else "Western Red Cedar"
            trim_option += " Finishing Trims"
            windoor_options = "\n".join([f"{entry.get()}\n</br>" for entry in windoor_text_entries])
            n_int_down = n_int_down_input.get()
            ext_down_exist = ext_down_exist_var.get()
            n_ext_down = n_ext_down_input.get()
            n_ext_wall = n_ext_wall_input.get()
            decking_exists = decking_exists_var.get()
            decking_dimensions = decking_dimensions_input.get()
            decking_type = decking_type_input.get()
            lam_floor_exists = lam_floor_exists_var.get()
            ufh_exists = ufh_exists_var.get()
            skirting_exists = skirting_exists_var.get()
            aircon_exists = aircon_exists_var.get()
            screws_exist = screws_exist_var.get()
            
            # Create file contents string in HTML format
            file_content = "<p>\n"
            file_content += f"{dimensions_x}m x {dimensions_y}m {canopy_cube} Garden Room\n</br>\n"
            #file_content += "</br>\n"
            file_content += f"Timber Frame Construction\n</br>\n"
            file_content += "Single Pitched Roof\n</br>\n"
            file_content += f"{cladding_option} Cladding\n</br>\n"

            file_content += f"{trim_option}\n</br>\n"

            file_content += "Hidden Weather Proofing Layer\n</br>\n"
            file_content += f"{windoor_options}"
            file_content += f"\n{n_int_down} x Interior Down Lights\n</br>\n"
            if ext_down_exist:
                file_content += f"{n_ext_down} x Exterior Down Lights\n</br>\n"
            file_content += f"{n_ext_wall} x Exterior Wall Lights\n</br>\n"
            file_content += "1 x Outdoor Socket\n</br>\n"
            file_content += "Full Electrics Package inc Consumer Unit, Sockets, Lights and Switches\n</br>\n"
            file_content += "Wireless Light Switches\n</br>\n"
            file_content += "Interior Plaster Boarded and Skimmed\n</br>\n"
            file_content += "Insulated Floors, Walls and Roof - 100mm Thickness\n</br>\n"
            file_content += "1 Piece Rubber Roof, inc Stylish Kerb Fascia's and Guttering\n</br>\n"
            if lam_floor_exists:
                file_content += "Laminate Flooring\n</br>\n"
            if ufh_exists:
                file_content += "Under Floor Heating\n</br>\n"
            if skirting_exists:
                file_content += "Skirting Boards\n</br>\n"
            if decking_exists:
                file_content += f"{decking_dimensions} {decking_type} Composite Decking\n</br>\n"
            if screws_exist:
                file_content += "Ground Screw Foundations\n</br>\n"
            if aircon_exists:
                file_content += "Samsung/Panasonic Air Conditioning Unit\n</br>\n"
            file_content += "</p"

            # Create file and write contents
            with open(file_path, "w") as file:
                file.write(file_content)
            # Display success message
            success_label.config(text=f"File saved to {file_path}")
        else:
            # Display error message if no file path is selected
            success_label.config(text="Error: No file path selected")


    # Create input widgets
    garden_room_number_label = tk.Label(root, text="Garden Room Number")
    garden_room_number_label.pack()
    garden_room_number_input = tk.Entry(root)
    garden_room_number_input.pack()

    dimensions_label = tk.Label(root, text="Dimensions")
    dimensions_label.pack()
    dimensions_input_frame = tk.Frame(root)
    dimensions_input_frame.pack()
    dimensions_x_input = tk.Entry(dimensions_input_frame, width=5)
    dimensions_x_input.pack(side="left")
    dimensions_y_input = tk.Entry(dimensions_input_frame, width=5)
    dimensions_y_input.pack(side="left")
    dimensions_units_label = tk.Label(dimensions_input_frame, text="Units")
    dimensions_units_label.pack(side="left")
    dimensions_units_var = tk.StringVar(value="m")
    dimensions_units_checkbox = tk.Checkbutton(dimensions_input_frame, text="ft", variable=dimensions_units_var, onvalue="ft", offvalue="m")
    dimensions_units_checkbox.pack(side="left")


    canopy_cube_var = tk.BooleanVar()
    canopy_cube_checkbutton = tk.Checkbutton(root, text="Cube", variable=canopy_cube_var)
    canopy_cube_checkbutton.pack()

    cladding_options = ["Vertical Western Red Cedar", "Horizontal Western Red Cedar", "Vertical Composite", "Horizontal Composite",
    "Vertical Shadow Gap Composite", "Horizontal Shadow Gap Composite"]
    cladding_option_var = tk.StringVar(value=cladding_options[0])
    cladding_option_label = tk.Label(root, text="Cladding Option")
    cladding_option_label.pack()
    for option in cladding_options:
        option_radiobutton = tk.Radiobutton(root, text=option, variable=cladding_option_var, value=option)
        option_radiobutton.pack()

    trim_var = tk.BooleanVar()
    trim_checkbutton = tk.Checkbutton(root, text="Anthracite Trims", variable=trim_var)
    trim_checkbutton.pack()

    windoor_frame = tk.Frame(root)
    windoor_frame.pack()
    windoor_options_label = tk.Label(windoor_frame, text="Windoor Options")
    windoor_options_label.pack(side="left")
    add_windoor_button = tk.Button(windoor_frame, text="+", command=add_windoor_entry)
    add_windoor_button.pack(side="left")
    windoor_text_entries = [tk.Entry(windoor_frame, width=30)]
    windoor_text_entries[-1].pack()

    n_int_down_label = tk.Label(root, text="Number of Internal Downlights")
    n_int_down_label.pack()
    n_int_down_input = tk.Entry(root)
    n_int_down_input.pack()

    ext_down_exist_var = tk.BooleanVar()
    ext_down_exists_checkbutton = tk.Checkbutton(root, text="Exterior Down Lights", variable=ext_down_exist_var)
    ext_down_exists_checkbutton.pack()

    n_ext_down_label = tk.Label(root, text="Number of External Downlights")
    n_ext_down_label.pack()
    n_ext_down_input = tk.Entry(root)
    n_ext_down_input.pack()

    n_ext_wall_label = tk.Label(root, text="Number of External Wall Lights")
    n_ext_wall_label.pack()
    n_ext_wall_input = tk.Entry(root)
    n_ext_wall_input.pack()

    decking_exists_var = tk.BooleanVar()
    decking_exists_checkbutton = tk.Checkbutton(root, text="Decking", variable=decking_exists_var)
    decking_exists_checkbutton.pack()

    decking_dimensions_label = tk.Label(root, text="Decking Dimensions")
    decking_dimensions_label.pack()
    decking_dimensions_input = tk.Entry(root, width=20)
    decking_dimensions_input.pack()

    ##

    decking_type_label = tk.Label(root, text="Decking Type")
    decking_type_label.pack()
    decking_type_input = tk.Entry(root, width=20)
    decking_type_input.pack()

    lam_floor_exists_var = tk.BooleanVar()
    lam_floor_exists_checkbutton = tk.Checkbutton(root, text="Laminate Flooring", variable=lam_floor_exists_var)
    lam_floor_exists_checkbutton.pack()

    ufh_exists_var = tk.BooleanVar()
    ufh_exists_checkbutton = tk.Checkbutton(root, text="Under Floor Heating", variable=ufh_exists_var)
    ufh_exists_checkbutton.pack()

    skirting_exists_var = tk.BooleanVar()
    skirting_exists_checkbutton = tk.Checkbutton(root, text="Skirting Boards", variable=skirting_exists_var)
    skirting_exists_checkbutton.pack()

    aircon_exists_var = tk.BooleanVar()
    aircon_exists_checkbutton = tk.Checkbutton(root, text="Air Conditioning", variable=aircon_exists_var)
    aircon_exists_checkbutton.pack()

    screws_exist_var = tk.BooleanVar()
    screws_exist_checkbutton = tk.Checkbutton(root, text="Ground Screws", variable=screws_exist_var)
    screws_exist_checkbutton.pack()

    save_button = tk.Button(root, text="Save File", command=create_text_file)
    save_button.pack()

    success_label = tk.Label(root, text="")
    success_label.pack()

    root.mainloop()

