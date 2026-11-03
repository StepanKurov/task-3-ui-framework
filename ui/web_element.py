import logging
from pathlib import Path

from playwright.sync_api import Locator

from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class WebElement:
    def __init__(self, locator: Locator, description: str):
        self.locator = locator
        self.description = description

    def __str__(self):
        return f"WebElement [{self.description}]"

    def get_text_content(self):
        logger.info(f"{self}: get_text_content")
        result = self.locator.text_content()
        logger.info(f"{self}: text content = '{result}'")
        return result

    def click(self):
        logger.info(f"{self}: click JS")
        self.locator.click()

    def right_click(self):
        logger.info(f"{self}: right click")
        self.locator.click(button="right")

    def press(self, key):
        logger.info(f"{self}: press {key}")
        self.locator.press(key)

    def hover(self):
        logger.info(f"{self}: hover")
        self.locator.hover()

    def get_attribute(self, attribute: str):
        logger.info(f"{self}: get attribute {attribute}")
        result = self.locator.get_attribute(attribute)
        logger.info(f"{self}: attribute = {result}")
        return result

    def scroll_into_view_if_needed(self):
        logger.info(f"{self}: scroll into view if needed")
        self.locator.scroll_into_view_if_needed()

    def set_input_files(self, file_path: Path):
        logger.info(f"{self}: set input files '{file_path}'")
        self.locator.set_input_files(file_path)
