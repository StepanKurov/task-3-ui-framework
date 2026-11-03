from pages.context_menu_page import ContextMenuPage
from ui.page_actions import PageActions


def test_context_menu(page):
    page_actions = PageActions(page)
    context_menu_page = ContextMenuPage(page)
    page_actions.goto("/context_menu")
    expected_result = "You selected a context menu"
    actual_result = page_actions.run_and_accept_alert(
        context_menu_page.right_click_context_area
    )

    assert actual_result == expected_result, (
        f"Ожидали: {expected_result}, Получили: {actual_result}"
    )
