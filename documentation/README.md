# Step-by-Step Guide for setup of   Automation testing  through selenium.

* This code was developed on linux Ubuntu x64.

## Pre-requisites (One time Activity):
* Ubuntu 22.10 
    - To check Ubuntu Version :
    ```bash
    $ lsb_release -a
    ``` 
* Python version 3.10.7
    - To check Python  Version :
    ```bash
    $ python -V
    ``` 
* Google Chrome browser
    - To check google chrome Version :
    ```bash
    $ google-chrome --version
    ```


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
- The `pwd` command stands for "print working directory" and displays the current directory you are in as below.

```bash
/home/user/path-to-current-directory
```
* Example :
```bash
/home/jay/code/hack_sel
```

2. Now determine the path to the Python interpreter that will be executed when you run the python command in the terminal

```bash
$ which python
```
 - Result of above command will be as below describing that this is machine level python interpretor :
```bash
/usr/bin/python 
```

3. Create a new Virtual Environment :
```bash
$ python -m venv .venv
```

4. This will create a hidden directory name .venv , in order to check if .venv directory is created, you can :
```bash
$ ll
```

5. Next step is to activate virtual environment:
```bash
$ source .venv/bin/activate
```
 - On execution of above command on terminal , you can find change on command line as below , indicating that virtual environment is activated:

```bash
(.venv) user@device:~/path-to-current-directory$
```

* For Example:
```bash
(.venv) jay@jay-Latitude-3410:~/code/hack_sel$ 
```


6. Creation of .gitignore file :
- The `.gitignore` file is a special file used in Git repositories to specify which files and directories should be ignored and not tracked by Git.
- It allows you to exclude certain files or patterns from being committed to the repository, keeping the repository clean and avoiding unnecessary tracking of files that do not need to be version controlled.

``` bash
$ touch .gitignore
```

7. This will create a hidden file name .gitignore , in order to check if .gitignore is created, you can :
```bash
$ ll
```

8. Now paste following in .gitignore file
```bash
.venv
```
- When you add these lines to the .gitignore file in a Git repository, it specifies patterns for files and directories that should be ignored and not tracked by Git.


9. Create proper working directory as below :
```bash
$ mkdir -p code/py
$ cd code/py
```
- This will create directory code and within code will create py directory.

10. Now determine the path to the Python interpreter that will be executed when you run the python command in the terminal

```bash
$ which python
```
- Result of above command will be similar to  as below describing that this is machine level python interpretor :

```bash 
/home/user/path-to-current-directory/code/py/.venv/bin/python
```

11. Install necessary packages for project:

```bash
$ pip install pytest 
$ pip install selenium
$ pip install webdriver-manager 
```

12. Now we need to generate req.txt file:
```bash
$ pip freeze > req.txt
```

- This command generates a req.txt file that lists all the installed Python packages and their versions. It is commonly used for sharing project dependencies and ensuring consistent environments across different systems.

13. Create another  .gitignore file :

``` bash
$ touch .gitignore
```
* And  Now paste following in .gitignore file
```bash
*.png
```

## Verification of setup:

- In order to verify packages are install :

1. pytest:

```bash
$ pip freeze | grep pytest
```
- Output
```bash
pytest==7.4.0
```

2. webdriver-manager

```bash
$  pip freeze | grep webdriver-manager
```
- Output
```bash
webdriver-manager==4.0.0
```
3. selenium

```bash
$ pip freeze | grep selenium
```
- Output
```bash
selenium==4.10.0
```

## To run script
```
$  python  execution.py  unsigned_home_page_comic_in.yaml
```

