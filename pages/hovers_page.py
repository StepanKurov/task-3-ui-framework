from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class HoversPage:
    HOVERS_PATH = "/hovers"

    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(page)

        self.user_images = MultiWebElement(
            self.page.locator(".figure img"),
            description="user image"
        )
        self.user_names = MultiWebElement(
            self.page.locator(".figure h5"),
            description="user name"
        )
        self.profile_links = MultiWebElement(
            self.page.locator(".figure a"),
            description="user profile"
        )

    def open(self):
        self.page_actions.goto(self.HOVERS_PATH)

    def hover_user(self, index):
        user = self.user_images.nth(index)
        user.hover()

    def get_user_name(self, index):
        user = self.user_names.nth(index)
        return user.get_text_content().strip()

    def get_profile_link(self, index):
        profile_link = self.profile_links.nth(index)
        return profile_link.get_attribute("href")

    def get_users_count(self):
        return self.user_images.count()