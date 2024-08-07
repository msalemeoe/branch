import os

def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except OSError as e:
        print(f"Error accessing file {file_path}: {e}")
        return 0
