from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class AlertsPage:
    JS_ALERTS_PATH = "/javascript_alerts"

    def __init__(self, page: Page):
        self.page = page
        self.page_actions = PageActions(page)

        self.alert_button = WebElement(
            self.page.locator('button[onclick="jsAlert()"]'),
            description="Alerts"
        )
        self.confirm_button = WebElement(
            self.page.locator('button[onclick="jsConfirm()"]'),
            description="Confirm"
        )
        self.prompt_button = WebElement(
            self.page.locator('button[onclick="jsPrompt()"]'),
            description="Prompt"
        )
        self.result_text = WebElement(
            self.page.locator("#result"),
            description="Result"
        )

    def get_result_text(self):
        return self.result_text.get_text_content().strip()

    def open(self):
        self.page_actions.goto(self.JS_ALERTS_PATH)

    def accept_js_alert(self):
        return self.page_actions.run_and_accept_alert(self.alert_button.click)

    def accept_js_confirm(self):
        return self.page_actions.run_and_accept_alert(self.confirm_button.click)

    def accept_js_prompt(self, prompt_text):
        return self.page_actions.run_and_accept_prompt(self.prompt_button.click, prompt_text)
