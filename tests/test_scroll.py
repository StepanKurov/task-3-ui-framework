from pages.scroll_page import ScrollPage
from ui.page_actions import PageActions


def test_scroll(page):
    page_actions = PageActions(page)
    scroll_page = ScrollPage(page)
    page_actions.goto("/infinite_scroll")

    while scroll_page.get_paragraph_count() < 10:
        scroll_page.scroll_to_last_paragraph()

    paragraph_count = scroll_page.get_paragraph_count()
    assert paragraph_count >= 10
