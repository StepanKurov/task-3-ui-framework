from faker import Faker

from pages.alerts_page import AlertsPage

fake = Faker()


def test_js_alert(page):
    alerts_page = AlertsPage(page)
    alerts_page.open()
    dialog = alerts_page.accept_js_alert()
    assert dialog == "I am a JS Alert"
    result = alerts_page.get_result_text()
    assert result == "You successfully clicked an alert"

def test_js_confirm(page):
    alerts_page = AlertsPage(page)
    alerts_page.open()
    dialog = alerts_page.accept_js_confirm()
    assert dialog == "I am a JS Confirm"
    result = alerts_page.get_result_text()
    assert result == "You clicked: Ok"

def test_js_prompt(page):
    alerts_page = AlertsPage(page)
    alerts_page.open()
    prompt_text = fake.word()
    dialog = alerts_page.accept_js_prompt(prompt_text)
    assert dialog == "I am a JS prompt"
    result = alerts_page.get_result_text()
    assert result == f"You entered: {prompt_text}"

