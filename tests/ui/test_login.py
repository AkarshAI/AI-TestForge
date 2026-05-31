import pytest


@pytest.mark.ui
@pytest.mark.smoke
def test_login_page_contains_form(browser_client):
    page = browser_client.load_page("https://qa.example.com/login")
    assert page["url"].endswith("/login")
    assert browser_client.find_text("Login")
    assert browser_client.find_text("Sign In")
