import os
import sys

import main
import clustering

if __name__ == "__main__":
    path = '.'

    if "main.py" not in os.listdir(path):
        print("File 'main.py' not exists")
        sys.exit(1)
    else:
        print("Try to start main\n")
        clustering.main()
        print("Finish!!\n")
