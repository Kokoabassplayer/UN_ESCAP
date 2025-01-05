from PIL import Image
import os

def make_background_transparent(image_path, output_path):
    # Load the image
    image = Image.open(image_path).convert("RGBA")
    
    # Make white background transparent
    datas = image.getdata()
    new_data = []
    for item in datas:
        # Check for white areas and make them transparent
        if item[:3] == (255, 255, 255):
            new_data.append((255, 255, 255, 0))  # Fully transparent
        else:
            new_data.append(item)
    
    image.putdata(new_data)
    image.save(output_path, "PNG")

# Folder paths
input_folder = r"C:\Users\OSNuttapongB\Downloads\UN-ESCAP\2024\population data insight button"
output_folder = r"C:\Users\OSNuttapongB\Downloads\UN-ESCAP\2024\population data insight button\processed"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process all images in the folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".png"):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, f"processed_{file_name}")
        make_background_transparent(input_path, output_path)
        print(f"Processed: {file_name}")
