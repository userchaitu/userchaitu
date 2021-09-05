from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shopItem = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.XPATH, "//*[contains(@id,'Password1')]")
    checkbox = (By.XPATH, "//input[@id='exampleCheck1']")
    radiobutton = (By.CSS_SELECTOR, "input[id='inlineRadio2']")
    gender = (By.CSS_SELECTOR, "select.form-control")
    submit = (By.XPATH, "//input[@value='Submit']")
    alert_text = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def getShopItem(self):
        return self.driver.find_element(*HomePage.shopItem)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def selCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def selRadioButton(self):
        return self.driver.find_element(*HomePage.radiobutton)

    def getGender(self):
        select = Select(self.driver.find_element(*HomePage.gender))
        return select.select_by_index(0)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlertText(self):
        return self.driver.find_element(*HomePage.alert_text).text
