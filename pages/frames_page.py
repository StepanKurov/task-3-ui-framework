from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class FramesPage:
    FRAMES_PATH = "/nested_frames"

    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(page)

        self.middle_text = WebElement(self.page
            .frame_locator('frame[name="frame-top"]')
            .frame_locator('frame[name="frame-middle"]')
            .locator("#content"),
            description="Middle frame"
        )
        self.left_text = WebElement(self.page
            .frame_locator('frame[name="frame-top"]')
            .frame_locator('frame[name="frame-left"]')
            .locator("body"),
            description="Left frame"
        )
        self.right_text = WebElement(self.page
            .frame_locator('frame[name="frame-top"]')
            .frame_locator('frame[name="frame-right"]')
            .locator("body"),
            description="Right frame"
        )
        self.bottom_text = WebElement(self.page
            .frame_locator('frame[name="frame-bottom"]')
            .locator("body"),
            description="Bottom frame"
        )

    def get_left_text(self):
        return self.left_text.get_text_content().strip()

    def get_middle_text(self):
        return self.middle_text.get_text_content().strip()

    def get_right_text(self):
        return self.right_text.get_text_content().strip()

    def get_bottom_text(self):
        return self.bottom_text.get_text_content().strip()

    def open(self):
        self.page_actions.goto(self.FRAMES_PATH)
