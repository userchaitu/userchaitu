# import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# @pytest.mark.usefixtures("test_setup")
from testpageobjects.test_checkout import Checkout
from testbaseutils.test_baseutil import UtilsTest
from testpageobjects.test_Home import HomePage


class TestEndtoEnd(UtilsTest):

    def test_setup(self, test_setup):

        log = self.getLog()
        Homeobj = HomePage(self.driver)
        # options.add_argument("--headless")
        Checkobj = Checkout(self.driver)
        log.info("Title is:"+self.driver.title)
        Homeobj.getShopItem().click()
        mobiles = Checkobj.getMobiles()
        # //div[contains(@class,'h-100')]/div/h4
        for mobile in mobiles:
            names = Checkobj.getMobileName().text
            log.info(names)
            if names == "iphone X":
                Checkobj.addToCart().click()

        self.driver.find_element_by_xpath("//a[contains(@class,'btn-primary')]").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_css_selector("input#country").send_keys("in")
        # Explicit Wait
        self.WaitTimeforText("India")

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//label[@for='checkbox2']").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        textmsg = self.driver.find_element_by_css_selector("div[class*='alert-success']").text
        log.info("Alert Success Message is:"+textmsg)
        assert "Success! Thank you!" in textmsg

        self.getScreenshot("file3.png")
