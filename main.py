import os
from scanner import scan_directory
from config import DIRECTORY_TO_SCAN

def main():
    scan_directory(DIRECTORY_TO_SCAN)

if __name__ == "__main__":
    main()
