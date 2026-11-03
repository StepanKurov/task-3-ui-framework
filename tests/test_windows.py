from pages.windows_page import WindowsPage
from pages.new_window_page import NewWindowPage
from ui.page_actions import PageActions


def test_windows(page):
    page_actions = PageActions(page)
    windows_page = WindowsPage(page)
    page_actions.goto("/windows")

    with page_actions.expect_new_page() as first_page_info:
        windows_page.click_link()
    first_page = first_page_info.value

    first_window = NewWindowPage(first_page)
    first_page_actions = PageActions(first_page)
    expected_result = "New Window"
    actual_result = first_window.get_title()
    assert actual_result == expected_result, (
        f"Ожидали: {expected_result}, Получили: {actual_result}"
    )

    page_actions.bring_to_front()
    with page_actions.expect_new_page() as second_page_info:
        windows_page.click_link()
    second_page = second_page_info.value

    second_window = NewWindowPage(second_page)
    second_page_actions = PageActions(second_page)
    actual_result = second_window.get_title()
    assert actual_result == expected_result, (
        f"Ожидали: {expected_result}, Получили: {actual_result}"
    )

    page_actions.bring_to_front()
    first_page_actions.close_page()
    second_page_actions.close_page()

    expected_pages_count = 1
    actual_pages_count = page_actions.get_pages_count()
    assert actual_pages_count == expected_pages_count, (
        f"Ожидали: {expected_pages_count} вкладку,"
        f" Получили: {actual_pages_count} вкладку"
    )
