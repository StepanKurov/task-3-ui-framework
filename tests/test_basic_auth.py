from pages.basic_auth_page import BasicAuthPage
from ui.page_actions import PageActions


def test_basic_auth(page):
    page_actions = PageActions(page)
    basic_auth_page = BasicAuthPage(page)
    page_actions.goto("/basic_auth")
    expected_result = "Congratulations! You must have the proper credentials."
    actual_result = basic_auth_page.get_result_text()

    assert actual_result == expected_result, (
        f"Ожидали: {expected_result}, Получили: {actual_result}"
    )
