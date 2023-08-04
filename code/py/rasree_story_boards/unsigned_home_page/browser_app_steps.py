# pyright: reportGeneralTypeIssues= false, reportUnknownMemberType= false
# pyright: reportOptionalMemberAccess= false, reportUnboundVariable = false
# pyright: reportUnknownArgumentType= false, reportUnknownVariableType= false
# pyright: reportUnknownParameterType= false, reportMissingTypeArgument= false
# pyright: reportMissingTypeStubs= false

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException, \
    InvalidArgumentException, InvalidElementStateException
import time
import yaml
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from mdutils import MdUtils


class BrowserAppSteps:
    '''
    A class representing browser app steps.
        Attributes:
            driver: The driver instance for the browser.
            browser_name (str): The name of the browser.
            browser_server_url (str): The server URL for the browser.
            duration (int): The duration of the app steps.
            comic_out_folder (str): The output folder for comic files.
    '''

    driver= None
    browser_name= None 
    browser_server_url= None
    duration= 10

