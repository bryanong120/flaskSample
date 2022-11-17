import os

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

APP_URL = os.environ.get('APP_URL')


def test_xd(selenium: WebDriver):
    selenium.get(APP_URL + "/aaa123")
    assert selenium.title == "Document"
    elem = selenium.find_element(By.ID, "xd")
    print(elem.text)
    assert elem.text == "aaa123"
