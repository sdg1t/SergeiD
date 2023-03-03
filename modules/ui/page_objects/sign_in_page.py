from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https;//github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)    

    def try_login(self, username, password):
        # Find element with wrong username or email
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Enter wrong username or email
        login_elem.send_keys(username)

        # Find element with wrong password
        pass_elem = self.driver.find_element(By.ID, "password")

        #Enter wrong password
        pass_elem.send_keys(password)
    
        # Find sign-in button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Emulate click by left mouse button
        btn_elem.click()  

    def check_title(self, expected_title):
        return self.driver.title == expected_title    
