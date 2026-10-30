import json
from playwright.sync_api import Browser


class PageFactory:
    def __init__(self, browser: Browser, config: dict):
        self.browser = browser
        self.config = config

    @classmethod
    def from_json(cls, browser: Browser, file_path: str):
        with open(file_path) as config_file:
            config = json.load(config_file)
        return cls(browser, config)

    def _create_context(self):
        context = self.browser.new_context(
            base_url=self.config["url"],
            http_credentials={
                "username": self.config["username"],
                "password": self.config["password"]
            }
        )
        return context

    def create_page(self):
        context = self._create_context()
        page = context.new_page()
        return page