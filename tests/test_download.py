from pages.download_page import DownloadPage
from ui.page_actions import PageActions


def test_download(page):
    page_actions = PageActions(page)
    download_page = DownloadPage(page)
    page_actions.goto("/download")
    file_index = 2

    expected_name = download_page.get_file_name(file_index)

    with page_actions.expect_download() as download_info:
        download_page.click_file(file_index)
    download_file = download_info.value

    actual_name = download_file.suggested_filename
    assert actual_name == expected_name, (
        f"Ожидали: {expected_name}, Получили: {actual_name}"
    )
