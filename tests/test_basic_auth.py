from pages.basic_auth_page import BasicAuthPage


def test_basic_auth(page):
    basic_auth_page = BasicAuthPage(page)
    basic_auth_page.open()
    result = basic_auth_page.get_result_text()
    assert result == "Congratulations! You must have the proper credentials."