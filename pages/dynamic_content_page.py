from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class DynamicContentPage:
    DYNAMIC_CONTENT_PATH = "/dynamic_content"

    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(page)

        self.images = MultiWebElement(
            self.page.locator(".large-2.columns img"),
            description="Dynamic images"
        )

    def open(self):
        self.page_actions.goto(self.DYNAMIC_CONTENT_PATH)

    def get_image_src(self, index):
        image = self.images.nth(index)
        return image.get_attribute("src")

    def reload_page(self):
        self.page_actions.reload()

    def compare_images(self):
        image1 = self.get_image_src(0)
        image2 = self.get_image_src(1)
        image3 = self.get_image_src(2)
        if image1 == image2:
            return True

        if image1 == image3:
            return True

        if image2 == image3:
            return True

        return False