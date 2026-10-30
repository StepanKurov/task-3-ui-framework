from pages.dynamic_content_page import DynamicContentPage


def test_dynamic_content(page):
    dynamic_page = DynamicContentPage(page)
    dynamic_page.open()

    while not dynamic_page.compare_images():
        dynamic_page.reload_page()

    assert dynamic_page.compare_images()