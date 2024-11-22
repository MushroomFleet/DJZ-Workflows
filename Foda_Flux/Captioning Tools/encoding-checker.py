import os
import sys
from pathlib import Path

def check_file_encoding(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            f.read()
        return True, None
    except UnicodeDecodeError as e:
        return False, str(e)

def main():
    current_dir = Path('.')
    txt_files = list(current_dir.glob('*.txt'))
    
    if not txt_files:
        print("No .txt files found in current directory")
        return

    failed_files = 0
    for file_path in txt_files:
        success, error = check_file_encoding(file_path)
        status = "PASS" if success else "FAIL"
        print(f"{file_path}: {status}")
        if not success:
            failed_files += 1
            print(f"  Error: {error}")
    
    print(f"\nSummary: {len(txt_files)} files checked, {failed_files} failed")

if __name__ == "__main__":
    main()
