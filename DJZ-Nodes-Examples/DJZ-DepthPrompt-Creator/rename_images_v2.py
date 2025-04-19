import os
import re

def rename_images():
    print("Starting the image renaming process...")
    
    # Get all files in the current directory
    files = os.listdir('.')
    print(f"Total files found: {len(files)}")

    # Separate image and text files
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    text_files = [f for f in files if f.lower().endswith('.txt')]
    
    print(f"Image files found: {len(image_files)}")
    print(f"Text files found: {len(text_files)}")

    # Create a set of text file names without extension for faster lookup
    text_file_names = {os.path.splitext(f)[0] for f in text_files}

    renamed_count = 0
    for image_file in image_files:
        print(f"\nProcessing image file: {image_file}")
        
        # Remove "_XXXXX_" pattern from the filename (where XXXXX is a 5-digit number)
        new_name = re.sub(r'_\d{5}_', '', image_file)
        
        # Check if a matching text file exists
        if os.path.splitext(new_name)[0] in text_file_names:
            try:
                os.rename(image_file, new_name)
                print(f"Successfully renamed: {image_file} -> {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"Error renaming {image_file}: {str(e)}")
        else:
            print(f"No matching text file found for: {new_name}")

    print(f"\nProcess completed. Total files renamed: {renamed_count}")

if __name__ == "__main__":
    rename_images()
