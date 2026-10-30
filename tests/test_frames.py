from pages.frames_page import FramesPage


def test_frames_page(page):
    frame_page = FramesPage(page)
    frame_page.open()
    left = frame_page.get_left_text()
    middle = frame_page.get_middle_text()
    right = frame_page.get_right_text()
    bottom = frame_page.get_bottom_text()

    assert left == "LEFT"
    assert right == "RIGHT"
    assert bottom == "BOTTOM"
    assert middle == "MIDDLE"
