from faker import Faker

from pages.alerts_page import AlertsPage
from ui.page_actions import PageActions

fake = Faker()
ALERTS_PATH = "/javascript_alerts"


def test_js_alert(page):
    page_actions = PageActions(page)
    alerts_page = AlertsPage(page)
    page_actions.goto(ALERTS_PATH)

    expected_dialog = "I am a JS Alert"
    expected_result = "You successfully clicked an alert"
    actual_dialog = page_actions.run_and_accept_alert(
        alerts_page.click_alert
    )
    actual_result = alerts_page.get_result_text()

    assert actual_dialog == expected_dialog, (
        f"Ожидали: {expected_dialog}, Получили: {actual_dialog}"
    )
    assert actual_result == expected_result, (
        f"Ожидали: {expected_result}, Получили: {actual_result}"
    )


def test_js_confirm(page):
    page_actions = PageActions(page)
    alerts_page = AlertsPage(page)
    page_actions.goto(ALERTS_PATH)

    expected_dialog = "I am a JS Confirm"
    expected_result = "You clicked: Ok"
    actual_dialog = page_actions.run_and_accept_alert(
        alerts_page.click_confirm
    )
    actual_result = alerts_page.get_result_text()

    assert actual_dialog == expected_dialog, (
        f"Ожидали: {expected_dialog}, Получили: {actual_dialog}"
    )
    assert actual_result == expected_result, (
        f"Ожидали: {expected_result}, Получили: {actual_result}"
    )


def test_js_prompt(page):
    page_actions = PageActions(page)
    alerts_page = AlertsPage(page)
    page_actions.goto(ALERTS_PATH)
    prompt_text = fake.word()

    expected_dialog = "I am a JS prompt"
    expected_result = f"You entered: {prompt_text}"
    actual_dialog = page_actions.run_and_accept_prompt(
        alerts_page.click_prompt,
        prompt_text
    )
    actual_result = alerts_page.get_result_text()

    assert actual_dialog == expected_dialog, (
        f"Ожидали: {expected_dialog}, Получили: {actual_dialog}"
    )
    assert actual_result == expected_result, (
        f"Ожидали: {expected_result}, Получили: {actual_result}"
    )
