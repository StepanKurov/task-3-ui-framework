from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement


class DownloadPage:
    def __init__(self, page: Page):
        self.page = page
        self.files = MultiWebElement(
            self.page.locator(".example a"),
            description="files"
        )

    def get_file_name(self, index):
        name_file = self.files.nth(index)
        return name_file.get_text_content().strip()

    def click_file(self, index):
        self.files.nth(index).click()
