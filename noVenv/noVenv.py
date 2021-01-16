import sys
import glob
import os

if __name__ == "__main__":
    root = sys.argv[1]
    for dir in glob.glob(f'{root}/*/**/venv/', recursive = True):
        if input(f' delete {dir} [y|n]').lower == 'y':
            print(f'  ...deleting {dir}')
            os.rmdir(dir)