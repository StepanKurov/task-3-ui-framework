from pages.scroll_page import ScrollPage


def test_scroll(page):
    scroll_page = ScrollPage(page)
    scroll_page.open()


    while scroll_page.get_paragraph_count() < 10:
        scroll_page.scroll_to_last_paragraph()

    paragraph_count = scroll_page.get_paragraph_count()
    assert paragraph_count >= 10

