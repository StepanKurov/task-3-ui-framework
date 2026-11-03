from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement


class ScrollPage:
    def __init__(self, page: Page):
        self.page = page
        self.paragraphs = MultiWebElement(
            self.page.locator(".jscroll-added"),
            description="Scroll"
        )

    def get_paragraph_count(self):
        return self.paragraphs.count()

    def scroll_to_last_paragraph(self):
        paragraph_count = self.get_paragraph_count()
        last_index = paragraph_count - 1
        last_paragraph = self.paragraphs.nth(last_index)
        last_paragraph.scroll_into_view_if_needed()
