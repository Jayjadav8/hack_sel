
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
4. Within `test_p1`function at last add below line to capture screen shots
```bash
self.driver.get_screenshot_as_file("screenshot.png")
```

5. python file `main.py`

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








