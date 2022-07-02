import pytest
from selene.support.shared import browser


@pytest.fixture()
def change_size_browser():
    browser.open('https://google.com').driver.set_window_size(1000, 1000)
    yield
    browser.close_current_tab()
