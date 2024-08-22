import os
from PIL import Image, ImageEnhance
from datetime import datetime

def process_images(main_folder_path):
    # Get today's date in the format "dd.mm"
    today_date = datetime.now().strftime("%d.%m")
    
    # Construct the folder path for today's date
    date_folder_path = os.path.join(main_folder_path, today_date)
    
    if not os.path.exists(date_folder_path):
        print(f"The folder for today's date '{today_date}' does not exist.")
        return
    
    # Construct the folder path for the edited images
    edited_folder_path = os.path.join(main_folder_path, f"{today_date}_edited")
    
    # Create the edited images folder if it doesn't exist
    os.makedirs(edited_folder_path, exist_ok=True)
    
    # Get a list of all files in the folder
    files = os.listdir(date_folder_path)
    
    for file_name in files:
        # Construct the full file path
        file_path = os.path.join(date_folder_path, file_name)
        
        # Open the image file
        with Image.open(file_path) as img:
            # Resize the image to 2000x1500
            img_resized = img.resize((1900, 1425))
            
            # Calculate the coordinates for cropping the 1200x800 area from the center
            left = (img_resized.width - 1200) / 2
            top = (img_resized.height - 800) / 2
            right = left + 1200
            bottom = top + 800
            img_cropped = img_resized.crop((left, top, right, bottom))
            
            # Adjust the exposure by the factor of 1.12
            enhancer = ImageEnhance.Brightness(img_cropped)
            img_exposed = enhancer.enhance(1.6)
            
            # Save the edited image with the same name in the edited folder
            new_file_path = os.path.join(edited_folder_path, file_name)
            img_exposed.save(new_file_path)
            print(f"Processed and saved: {new_file_path}")

# Example usage
main_folder_path = "D:\\modelcarshop\\"  # Replace with the path to your main folder
process_images(main_folder_path)
