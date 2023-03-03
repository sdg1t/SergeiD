from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # creating page object
    sign_in_page = SignInPage()

    # open the page https://github.com/login
    sign_in_page.go_to()

    # making attampt to login GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # check expected page title
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # closing browser
    sign_in_page.close()
    