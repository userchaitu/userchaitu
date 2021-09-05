from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_xpath("//div[contains(@class,'h-100')]")
    mobiles = (By.XPATH, "//div[contains(@class,'h-100')]")
    # find_element_by_xpath("div/h4").text
    mobileName = (By.XPATH, "//div[contains(@class,'h-100')]/div/h4")
    # find_element_by_xpath("div/button")
    button = (By.XPATH, "//div[contains(@class,'h-100')]/div/button")

    def getMobiles(self):
        return self.driver.find_elements(*Checkout.mobiles)

    def getMobileName(self):
        return self.driver.find_element(*Checkout.mobileName)

    def addToCart(self):
        return self.driver.find_element(*Checkout.button)

