import os
from app_b.features.util.configuration_environment import ConfigurationEnvironment as ce


def main():
    env = ce()
    os.chdir(env.get_path("features"))
    os.system("dir")
    os.system("behave")


if __name__ == '__main__':
    main()