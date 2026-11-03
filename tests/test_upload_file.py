from pages.upload_file_page import UploadFilePage
from ui.page_actions import PageActions


def test_upload_file(page, tmp_path):
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("test file")

    page_actions = PageActions(page)
    upload_page = UploadFilePage(page)
    page_actions.goto('/upload')

    upload_page.upload_file(file_path)
    upload_page.upload()

    expected_result = "File Uploaded!"
    actual_result = upload_page.get_upload_result()

    expected_name = file_path.name
    actual_name = upload_page.get_upload_file_name()

    assert actual_result == expected_result, (
        f"Ожидали: {expected_result}, Получили: {actual_result}"
    )
    assert actual_name == expected_name, (
        f"Ожидали: {expected_name}, Получили: {actual_name}"
    )
