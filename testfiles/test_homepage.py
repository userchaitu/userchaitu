import pytest

from testbaseutils.test_baseutil import UtilsTest
from testdata.test_homedata import HomeTestData
from testpageobjects.test_Home import HomePage


class TestHomepage(UtilsTest):

    def test_fromSubmit(self, getData):
        log = self.getLog()
        home = HomePage(self.driver)
        home.getName().send_keys(getData['First Name'])
        log.info("First Name is:"+getData['First Name'])
        home.getEmail().send_keys(getData['Email'])
        log.info("Email ID is:" + getData['Email'])
        home.getPassword().send_keys(getData['Password'])
        log.warning("Its a Password, value can't be logged")
        home.selCheckbox().click()
        home.selRadioButton().click()
        home.getGender()
        home.getSubmit().click()
        log.info("Success Message is:"+home.getAlertText())
        self.getScreenshot("file1.png")
        self.driver.refresh()

    @pytest.fixture(params=HomeTestData.testdata("TC_02"))
    def getData(self, request):
        return request.param
