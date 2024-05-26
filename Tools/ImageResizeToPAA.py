import os
import subprocess
from PIL import Image

# Define the path to the folder containing the images
image_folder_path = r"P:\ResurgenceRP_Dev\IMAGES_TEMP"
processed_folder_path = os.path.join(image_folder_path, "PROCESSED")

# Create the PROCESSED folder if it doesn't exist
if not os.path.exists(processed_folder_path):
    os.makedirs(processed_folder_path)

# Define the path to ImageToPAA.exe
image_to_paa_path = r"D:\SteamLibrary\steamapps\common\DayZ Tools\Bin\ImageToPAA\ImageToPAA.exe"  # Update this path

# Define the target dimensions
target_width, target_height = 2048, 1024

# Function to resize an image while maintaining aspect ratio
def resize_image(image, target_width, target_height):
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height

    if target_width / target_height > aspect_ratio:
        new_height = target_height
        new_width = int(aspect_ratio * target_height)
    else:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    return resized_image

# Loop through all files in the folder
for filename in os.listdir(image_folder_path):
    file_path = os.path.join(image_folder_path, filename)

    # Check if the file is an image
    if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Open the image
        with Image.open(file_path) as img:
            # Resize the image
            resized_img = resize_image(img, target_width, target_height)
            
            # Create a new image with the target dimensions and a black background
            new_img = Image.new("RGB", (target_width, target_height), (0, 0, 0))
            
            # Calculate the position to paste the resized image onto the new image
            paste_x = (target_width - resized_img.width) // 2
            paste_y = (target_height - resized_img.height) // 2
            
            # Paste the resized image onto the new image
            new_img.paste(resized_img, (paste_x, paste_y))
            
            # Save the new image as a temporary PNG file
            temp_file_path = os.path.join(image_folder_path, "temp_" + filename)
            new_img.save(temp_file_path)

            # Define the output PAA file path in the PROCESSED folder
            paa_file_path = os.path.join(processed_folder_path, os.path.splitext(filename)[0] + ".paa")

            # Convert the PNG file to PAA using ImageToPAA.exe
            subprocess.run([image_to_paa_path, temp_file_path, paa_file_path])

            # Remove the temporary PNG file
            os.remove(temp_file_path)

print("All images have been resized and converted to PAA format, and saved in the PROCESSED folder.")
