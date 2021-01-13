'''
This method is called only when generated the package by setup.py
'''

import os
from app_b.features.util.config import Config


def main():
    env = Config()
    os.chdir(env.get_path("features"))
    os.system("behave")


if __name__ == '__main__':
    main()