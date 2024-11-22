import os
from pathlib import Path

def check_and_fix_file(filepath):
    # First try reading with utf-8
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            return True, None, None
    except UnicodeDecodeError as e:
        # If fails, try reading as bytes and decode with replacement
        try:
            with open(filepath, 'rb') as f:
                content = f.read()
                fixed_content = content.decode('utf-8', errors='replace')
            
            # Write the fixed content back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            return False, str(e), filepath
        except Exception as e:
            return False, f"Failed to fix: {str(e)}", None

def main():
    current_dir = Path('.')
    txt_files = list(current_dir.glob('*.txt'))
    
    if not txt_files:
        print("No .txt files found in current directory")
        return

    failed_files = 0
    fixed_files = []
    
    for file_path in txt_files:
        success, error, fixed_path = check_and_fix_file(file_path)
        status = "PASS" if success else "FAIL"
        print(f"{file_path}: {status}")
        if not success:
            failed_files += 1
            print(f"  Error: {error}")
            if fixed_path:
                fixed_files.append(fixed_path)
    
    print(f"\nSummary: {len(txt_files)} files checked, {failed_files} failed")
    if fixed_files:
        print(f"Fixed files: {', '.join(str(f) for f in fixed_files)}")

if __name__ == "__main__":
    main()
