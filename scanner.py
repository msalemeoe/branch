import os
from file_info import get_file_size
from utils import format_size

def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = get_file_size(file_path)
            if file_size > 100 * 1024 * 1024:  # 100 MB in bytes
                print(f"File: {file_path}, Size: {format_size(file_size)}")
