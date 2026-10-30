import logging
from collections.abc import Callable

from playwright.sync_api import Page, Dialog

from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class PageActions:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        logger.info(f"PageAction: goto '{url}'")
        self.page.goto(url)

    def run_and_accept_alert(self, action: Callable[[], None]):
        logger.info("PageAction: accept dialog")
        return self._handle_dialog(action, mode="accept")

    def run_and_dismiss_alert(self, action: Callable[[], None]):
        logger.info("PageAction: dismiss dialog")
        return self._handle_dialog(action, mode="dismiss")

    def run_and_accept_prompt(self, action: Callable[[], None], prompt_text: str):
        logger.info("PageAction: accept prompt")
        return self._handle_dialog(action, mode="accept", prompt_text=prompt_text)

    def _handle_dialog(self, action: Callable[[], None], mode: str, prompt_text=None):
        logger.info("PageAction: expect dialog")
        message = ""

        def handle_dialog(dialog: Dialog):
            nonlocal message
            message = dialog.message

            if mode == "dismiss":
                dialog.dismiss()
                return

            if prompt_text is None:
                dialog.accept()
                return

            dialog.accept(prompt_text)

        self.page.once("dialog", handle_dialog)
        action()

        if not message:
            raise RuntimeError("Expected dialog was not shown")

        return message

    def expect_new_page(self):
        logger.info("PageAction: expect new page")
        return self.page.context.expect_page()

    def bring_to_front(self):
        logger.info("PageAction: bring page to front")
        self.page.bring_to_front()

    def close_page(self):
        logger.info("PageAction: close page")
        self.page.close()

    def get_pages_count(self):
        logger.info("PageAction: get pages count")
        return len(self.page.context.pages)

    def reload(self):
        logger.info("PageAction: reload page")
        self.page.reload()

    def expect_download(self):
        logger.info("PageAction: expect download")
        return self.page.expect_download()