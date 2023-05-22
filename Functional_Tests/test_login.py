from Pages.Login import LoginPage


def test_successful_login(browser):
    login_page = LoginPage(browser)
    login_page.enter_username("myusername")
    login_page.enter_password("mypassword")
    login_page.click_login_button()

    # Add assertions to verify the login was successful
    assert "Welcome" in browser.page_source


def test_failed_login(browser):
    login_page = LoginPage(browser)
    login_page.enter_username("invalidusername")
    login_page.enter_password("invalidpassword")
    login_page.click_login_button()

    # Add assertions to verify the error message or behavior
    assert "Invalid credentials" in browser.page_source
