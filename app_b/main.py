import os
from os.path import dirname, abspath

root ="behave " + '"' + dirname(abspath(__file__)) + '\\' + 'features' + '"'

def main():
    os.system(root)


if __name__ == '__main__':
    main()