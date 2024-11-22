import os
import re

def clean_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Remove specified characters
        cleaned = re.sub(r'[0-9().:]', '', content)
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(cleaned)
        print(f"Processed: {filename}")
            
    except Exception as e:
        print(f"Error processing {filename}: {str(e)}")

def main():
    # Get all .txt files in current directory
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    
    if not txt_files:
        print("No .txt files found in current directory")
        return
        
    for filename in txt_files:
        clean_file(filename)
    
    print(f"Finished processing {len(txt_files)} files")

if __name__ == "__main__":
    main()
