from playwright.sync_api import Page

from ui.web_element import WebElement


class AlertsPage:
    def __init__(self, page: Page):
        self.page = page
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

    def click_alert(self):
        self.alert_button.click()

    def click_confirm(self):
        self.confirm_button.click()

    def click_prompt(self):
        self.prompt_button.click()
