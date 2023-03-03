import pytest

from selenium import webdriver
from selenium .webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_incorrrect_username():
    # Creating object to control browser
    driver = webdriver.Chrome(
        service=Service(r"/Users/sd/SergeiD/" + "chromedriver")
    )

    # Open page https://github.com/login
    driver.get("https://github.com/login")

    # Find element with wrong username or email
    login_elem = driver.find_element(By.ID, "login_field")

    # Enter wrong username or email
    login_elem.send_keys("sergiibutenko@mistakeemail.com")

    # Find element with wrong password
    pass_elem = driver.find_element(By.ID, "password")

    #Enter wrong password
    pass_elem.send_keys("wrong password")
    
    # Find sign-in button
    btn_elem = driver.find_element(By.NAME, "commit")

    # Emulate click by left mouse button
    btn_elem.click()
    
    # Check page name we expected
    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(3)

    # Closing browser
    driver.close()
