# Garden Room Image Resizer
This script is designed to resize and save images for a garden room, as well as create related text files for use in a website or other marketing materials. The script includes a GUI that allows the user to select the garden room number, choose a favourite image, and input the location and dimensions of the garden room.

## Getting Started
To use this script, you will need to have Python 3 and the Pillow library installed. You can install Pillow using pip:
pip install Pillow

## Usage
Before using, download a number of .jpg images of the garden room and place them in a folder named "GardenRoomXXX", where XXX is the build number. To run the script, simply execute the garden_room_resizer.py file in your Python environment. This will launch the GUI, which you can use to select the garden room number, choose a favourite image, and input the location and dimensions of the garden room.

Once you have made your selections, click the "Resize Images" button to resize and save the images to the appropriate directories. The resized images will be saved in the TestimonialsTODO, Gallery, and Home directories, while the related text files will be saved in the TestimonialsTODO and Gallery directories.

# Gallery Spec Generator
This is a simple desktop application that generates a specification document for a garden room based on user inputs. The document is generated in HTML format and can be saved to a file.

## Requirements
You will need to install the tkinter library, which is included with most Python installations.

## Usage
To run the application, simply run the gallery_spec_generator.py file using Python:

python gallery_spec_generator.py

The application window will appear, and you can enter your desired specifications for the garden room. Once you have entered all the required information, click the "Save File" button to generate the specification document.

# Workflow
Download the best few images from a Garden Room's folder on the OneDrive. Unzip the folder and rename it to be 'GardenRoomXXX'. Run imgResizer.py, select the build number from the dropdown list, and click load images. The Input the location and dimensions of the build eg. Newark 3m x 3m. Then click the best looking image, and it should get a very light blue highlighted edge around it. Click resize images.

The finished resized images will be stored in the 'Gallery', 'Home' and 'testimonialsTODO' folders.
Next, open the garden room's specifications from quote file one the OneDrive and then run specText.py. Enter the specifications, click 'Save File', name the file 'GardenRoomXXX.txt', and the file will be saved in the folder named 'temp'.

Next open Jpegmini and drag all of the images into it in order to shrink their size.

To upload the images, FTP to the server with FileZilla and go to public.html/img/GardenRoomImages. Upload the file(s) in imgResizer/Home to GardenRoomsHome and the files in imgResizer/Gallery to GardenRoomsGallery.

When a testimonial is released on Facebook/Google etc, copy the text, open testimonialsTODO, paste the text in there, splitting the text into relevant paragraphs. Once saved, upload both the .txt and .jpg files to GardenRoomsTestimonials on the server.