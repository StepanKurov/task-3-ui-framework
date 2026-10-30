from pathlib import Path

from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.multi_web_element import MultiWebElement


class DownloadPage:
    DOWNLOAD_PATH = "/download"

    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(page)

        self.files = MultiWebElement(
            self.page.locator(".example a"),
            description="files"
        )

    def open(self):
        self.page_actions.goto(self.DOWNLOAD_PATH)

    def get_file_name(self, index):
        name_file = self.files.nth(index)
        return name_file.get_text_content().strip()

    def download_file(self, index):
        with self.page_actions.expect_download() as download_info:
            self.files.nth(index).click()

        download = download_info.value
        return download
