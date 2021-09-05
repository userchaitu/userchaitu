import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def test_setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="C:\\Users\\user\\eclipse\\chromedriver_win32\\chromedriver.exe",
                              options=options)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()
