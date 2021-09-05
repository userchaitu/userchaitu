import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("test_setup")
class UtilsTest:

    def getLog(self):
        LoggerName = inspect.stack()[1][3]
        filehandler = logging.FileHandler(
            "C:\\Users\\user\\PycharmProjects\\pythonProject\\Sel_PythonFramework\\testbaseutils\\logFile.log")
        logs = logging.getLogger(LoggerName)
        formatting = logging.Formatter("%(asctime)s, %(levelname)s, %(name)s, %(message)s")
        filehandler.setFormatter(formatting)
        logs.addHandler(filehandler)
        logs.setLevel(logging.DEBUG)
        return logs

    def WaitTimeforText(self, text):
        wait = WebDriverWait(self.driver, 8)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def getScreenshot(self, filename):
        return self.driver.get_screenshot_as_file(filename)
