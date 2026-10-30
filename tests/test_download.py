from pages.download_page import DownloadPage


def test_download(page):
    download_page = DownloadPage(page)
    download_page.open()

    file_name = download_page.get_file_name(2)
    download_file_name = download_page.download_file(2).suggested_filename

    assert file_name == download_file_name
