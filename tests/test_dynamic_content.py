from pages.dynamic_content_page import DynamicContentPage
from ui.page_actions import PageActions


def test_dynamic_content(page):
    page_actions = PageActions(page)
    dynamic_page = DynamicContentPage(page)

    page_actions.goto("/dynamic_content")
    image_sources = dynamic_page.get_image_sources()
    while len(image_sources) == len(set(image_sources)):
        page_actions.reload()
        image_sources = dynamic_page.get_image_sources()

    expected_result = True
    actual_result = len(image_sources) != len(set(image_sources))
    assert actual_result == expected_result, (
        f"Ожидали: {expected_result}, Получили: {actual_result}"
    )
