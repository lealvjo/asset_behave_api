import subprocess
from os.path import dirname, abspath

root ="behave " + '"' + dirname(abspath(__file__)) + '\\' + 'features' + '"'

def main():
    subprocess.run(root)


if __name__ == '__main__':
    main()