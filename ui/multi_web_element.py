from playwright.sync_api import Locator

from ui.web_element import WebElement


class MultiWebElement:
    def __init__(self, locator: Locator, description: str):
        self.locator = locator
        self.description = description

    def nth(self, index: int):
        return WebElement(
            locator=self.locator.nth(index),
            description=f"{self.description}[{index}]"
        )

    def count(self):
        return self.locator.count()