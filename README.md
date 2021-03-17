# asset_behave_api
Example of how to automate API, using python and behavior-oriented development (BDD)
     
Framework documentation:
     
    
        - https://behave.readthedocs.io/en/latest/

Application Programming Interface used for testing
    
        
        - https://github.com/lealvjo/scraping_games

# Importing the project and creat virtual environment project Pycharm

import the project into git: https://github.com/lealvjo/asset_behave_api.git
    
- [x] Open the project in pycharm
- [x] Navigate to file and settings
- [x] Navigate to python interpreter and click on the gear
- [x] Select add and new environment
    
# Enabling virtual environment
    
A virtual environment is a Python environment, so the Python interpreter, libraries and scripts 
installed in it are isolated from those installed in other virtual environments.
     
- [x] Open a terminal in pycharm in your root folder
- [x] And type: cd venv\Scripts\
- [x] And type: activate
    
    
    After this will appear a (venv) before your project, it means that the virtual environment has been enabled**
        Ex: (venv) C:\Users\{user}\PycharmProjects\asset_behave_api\

# Installing external packages

Text file, containing a list of items / packages to be installed during pip install.

- [x] Open a terminal at the root where the requirements.txt file is located
- [x] Type: pip install -r requirements.txt
    
  
    To check what has been installed
    
- [x] Type: pip list
  

    The application is at the root /app_b

# Running behavior-oriented tests (BDD)

- [x] Open a terminal in pycharm in your root folder
- [x] And type: cd app_b\features\
- [x] And type: behave


    Behave argument and to run the tests that are located in the features folder, 
    according to those that was configured in the behave.ini.

    He and the equivalent of the mvn test of the maven :)

# Environment definitions behave.ini

    The environments are configured in the folder features/stage
        - environment.yml
    
    *** behave.ini and the test parameterization file.
        - features/behave.ini
    
    Definitions stage in behave.ini:
    
    [behave.userdata]    [behave.userdata]  [behave.userdata]
    STAGE=LOCAL          STAGE=DEV           STAGE=QA  
    
    LOCAL: Wheel pointing to local environment
    DEV: Wheel pointing to development environment
    QA: Wheel pointing to test environment
 
    behave.ini and equivalent to classRunner() of java  :)
 
# To generate a new installable package setup.py

Setup.py is a python file, which usually informs you that the module / package you are about to install has been packaged and distributed with Distutils, 
which is the standard for distributing Python modules. This allows you to easily install Python packages.
    
- [x] Open a terminal at the root where the
- [x] type: python setup.py bdist_wheel
    
        You can install it in the virtual environment or on any other machine, even yours locally.

- [x] type: pip install --upgrade --force-reinstall dist/asset_behave_api-{version}-py3-none-any.whl
    

# To run the project installed

If installed in any environment to run by calling entry_points.
    
- [x] In the terminal type: {asset_behave_api_run} and press enter
    
    

