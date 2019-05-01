import os
import sys

from main import main

if __name__ == "__main__":
    path = '.'

    if "preprocessing.py" not in os.listdir(path):
        print("File 'main.py' not exists")
        sys.exit(1)
    else:
        main
