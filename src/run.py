import os
import sys

import main

if __name__ == "__main__":
    path = '.'

    if "main.py" not in os.listdir(path):
        print("File 'main.py' not exists")
        sys.exit(1)
    else:
        main.main()
