from pathlib import Path

from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class UploadFilePage:
    UPLOAD_FILE_PATH = '/upload'

    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(page)

        self.file_input = WebElement(
            self.page.locator("#file-upload"),
            description="Select file to upload"
        )

        self.upload_button = WebElement(
            self.page.locator("#file-submit"),
            description="Upload file"
        )

        self.upload_result = WebElement(
            self.page.locator(".example h3"),
            description="File uploaded!"
        )

        self.upload_file_name = WebElement(
            self.page.locator("#uploaded-files"),
            description="Name uploaded file"
        )

    def open(self):
        self.page_actions.goto(self.UPLOAD_FILE_PATH)

    def upload_file(self, file_path: Path):
        self.file_input.set_input_files(file_path)

    def upload(self):
        self.upload_button.click()

    def get_upload_result(self):
        return self.upload_result.get_text_content().strip()

    def get_upload_file_name(self):
        return self.upload_file_name.get_text_content().strip()
