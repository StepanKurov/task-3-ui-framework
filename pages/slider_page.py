from playwright.sync_api import Page

from ui.web_element import WebElement


class SliderPage:
    def __init__(self, page: Page):
        self.page = page
        self.horizontal_slider = WebElement(
            self.page.locator('input[type="range"]'),
            description="Slider"
        )
        self.slider_value = WebElement(
            self.page.locator("#range"),
            description="Slider range"
        )

    def set_slider_value(self, value):
        for slide in range(value):
            self.horizontal_slider.press("ArrowRight")

    def get_slider_value(self):
        return self.slider_value.get_text_content().strip()

    def get_min_value(self):
        return float(self.horizontal_slider.get_attribute("min"))

    def get_max_value(self):
        return float(self.horizontal_slider.get_attribute("max"))

    def get_step(self):
        return float(self.horizontal_slider.get_attribute("step"))
