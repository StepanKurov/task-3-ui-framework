from pages.windows_page import WindowsPage
from pages.new_window_page import NewWindowPage


def test_windows(page):
    windows_page = WindowsPage(page)
    windows_page.open()
    first_page = windows_page.open_new_window()
    first_window = NewWindowPage(first_page)
    first_title = first_window.get_title()
    assert first_title == "New Window"

    windows_page.switch_to_main_page()
    second_page = windows_page.open_new_window()
    second_window = NewWindowPage(second_page)
    second_title = second_window.get_title()
    assert second_title == "New Window"

    first_window.close()
    second_window.close()

    count_pages = windows_page.get_open_pages_count()
    assert count_pages == 1