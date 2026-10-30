import pytest
from logger import setup_logger
from ui.page_factory import PageFactory
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()

@pytest.fixture
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(channel="chrome", headless=False, slow_mo=1000)
    page_factory = PageFactory.from_json(browser, "config/config.json")
    page = page_factory.create_page()

    yield page
    browser.close()
    playwright.stop()
