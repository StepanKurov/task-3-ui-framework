from pathlib import Path

from pages.upload_file_page import UploadFilePage


def test_upload_file(page):
    file_path = Path("file/multfilm_pingviny.jpg")

    upload_page = UploadFilePage(page)
    upload_page.open()

    upload_page.upload_file(file_path)
    upload_page.upload()

    result_uploaded = upload_page.get_upload_result()
    file_name = upload_page.get_upload_file_name()

    assert result_uploaded == "File Uploaded!"
    assert file_name == file_path.name

