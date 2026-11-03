from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement


class DynamicContentPage:
    def __init__(self, page: Page):
        self.page = page
        self.images = MultiWebElement(
            self.page.locator(".large-2.columns img"),
            description="Dynamic images"
        )

    def get_image_src(self, index):
        image = self.images.nth(index)
        return image.get_attribute("src")

    def get_image_sources(self):
        sources = []

        for index in range(self.images.count()):
            sources.append(self.get_image_src(index))

        return sources
