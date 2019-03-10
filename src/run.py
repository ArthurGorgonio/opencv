import os
import sys

import main

if __name__ == "__main__":
    path = '.'

    if "main.py" in os.listdir(path):
        main.main()
    else:
        print("File 'main.py' not exists")
        sys.exit(1)
