# README :
* This code was developed on linux Ubuntu x64.

## Pre-requisites:
* Ubuntu 22.10 
* python version 3.10.7

### Installation of python packages:

- This command will install the python-is-python3 package, which sets Python 3 as the default Python version, and the python3-pip package, which provides the package installer for Python 3. 

``` bash
$ sudo apt install python-is-python3 python3-pip

```

### Installation of Web driver for Chrome :
- On Ubuntu Linux for selenium test.

#### Reference documentation :
- URL [for this](https://tecadmin.net/setup-selenium-with-python-on-ubuntu-debian/)

#### Steps :

1. Download the latest Gooogle Chrome Debian package on your system:
```bash
$ wget -nc https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
```
2. Now, execute the following commands to install Google Chrome from the locally downloaded file:
```bash
$ sudo apt update 
$ sudo apt install -f ./google-chrome-stable_current_amd64.deb 
```
- This will checks for any updates or changes to the package lists.
- and , install Google Chrome from the locally downloaded file.

## Virtual Environment:
-  Aim is to  create python virtual environment for itself.

### Steps:

1.  Check your current working directory :
```bash
$ pwd
```
- Result of above command will be as below describing user is present in hack_sel directory:

```bash
/home/jay/code/play_dir/hack_sel
```

2. Create proper working directory and get into py directory:
```bash
$ mkdir -p code/py
$ cd code/py
```
- This will create directory code and within code will create py directory.

3. Now determine the path to the Python interpreter that will be executed when you run the python command in the terminal

```bash
$ which python
```
 - Result of above command will be as below describing that this is machine level python interpretor :
```bash
/usr/bin/python 
```

4. Create a new Virtual Environment :
```bash
$ python -m venv .venv
```

5. This will create a hidden directory name .venv , in order to check if .venv directory is created, you can :
```bash
$ ll
```

6. Next step is to activate virtual environment:
```bash
$ source .venv/bin/activate
```
 - On execution of above command on terminal , you can find change on command line as below:

```bash
(.venv) jay@jay-Latitude-3410:~/code/play_dir/hack_sel/code/py$ 
```

7. Now determine the path to the Python interpreter that will be executed when you run the python command in the terminal

```bash
$ which python
```
- Result of above command will be as below describing that this is machine level python interpretor :

```bash 
/home/jay/code/play_dir/hack_sel/code/py/.venv/bin/python
```

8. Install necessary packages for project:

```bash
$ pip install pytest 
$ pip install selenium
$ pip install webdriver-manager 
```

9. Now we need to generate req.txt file:
```bash
$ pip freeze > req.txt
```

- This command generates a req.txt file that lists all the installed Python packages and their versions. It is commonly used for sharing project dependencies and ensuring consistent environments across different systems.

10. Creation of .gitignore file :
- The `.gitignore` file is a special file used in Git repositories to specify which files and directories should be ignored and not tracked by Git.
- It allows you to exclude certain files or patterns from being committed to the repository, keeping the repository clean and avoiding unnecessary tracking of files that do not need to be version controlled.

``` bash
$ touch .gitignore
```

11. This will create a hidden file name .gitignore , in order to check if .gitignore is created, you can :
```bash
$ ll
```

12. Now paste following in .gitignore file
```bash
__pycache__/**
*.png
```

## Automation testing:

1. Import the python file extracted from selenium extension to py directory( current directory) lets say it as `test_P1.py` .
2. Create python file say `main.py` 
-  This is executable file for  `test_P1.py` .

### Make following Changes in  test_P1.py  as follows:

1. Import required imports which are as follows:

```bash
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
options = Options()
```

2. Create Chrome WebDriver instance with the ChromeDriverManager:
```bash
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

```
3. Within `setup_method` function :

- Initializes the Chrome WebDriver.

```bash
self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
```
- Remove the  webdriver.Remote class (is used to create a WebDriver instance that connects to a remote Selenium server or a Selenium Grid.)

```bash
#webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

```
4. python file `main.py`

- The `main.py` script serves as the entry point for executing the main function and running the tests defined in the `TestP1` class.
- Importing the `TestP1` class from `test_P1.py` :
```bash
from test_p1 import TestP1
```
- Defining the main() function which  is the entry point of the script.
-  It is responsible for orchestrating the execution of the tests defined in the `TestP1` class.
- Creating an instance of the TestP1 class:
```bash
p1 = TestP1()
```
- call the methods of class `TestP1` class
```bash
    p1.setup_method("")
    p1.test_p1()
    p1.teardown_method("")
```








