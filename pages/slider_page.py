from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class SliderPage:
    SLIDER_PATH = "/horizontal_slider"

    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(page)
        self.horizontal_slider = WebElement(
            self.page.locator('input[type="range"]'),
            description="Slider"
        )
        self.slider_value = WebElement(
            self.page.locator("#range"),
            description="Slider range"
        )

    def set_slider_value(self, value):
        press_count = int(value / 0.5)
        for slide in range(press_count):
            self.horizontal_slider.press("ArrowRight")

    def get_slider_value(self):
        return self.slider_value.get_text_content().strip()

    def open(self):
        self.page_actions.goto(self.SLIDER_PATH)