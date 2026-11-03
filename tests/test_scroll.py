from pages.scroll_page import ScrollPage
from ui.page_actions import PageActions


def test_scroll(page):
    page_actions = PageActions(page)
    scroll_page = ScrollPage(page)
    page_actions.goto("/infinite_scroll")

    expected_result = 10
    while scroll_page.get_paragraph_count() < expected_result:
        scroll_page.scroll_to_last_paragraph()

    actual_result = scroll_page.get_paragraph_count()
    assert actual_result >= expected_result, (
        f"Ожидали: {expected_result}, Получили: {actual_result}"
    )
