from pages.frames_page import FramesPage
from ui.page_actions import PageActions


def test_frames_page(page):
    page_actions = PageActions(page)
    frame_page = FramesPage(page)
    page_actions.goto("/nested_frames")

    expected_left = "LEFT"
    actual_left = frame_page.get_left_text()

    expected_middle = "MIDDLE"
    actual_middle = frame_page.get_middle_text()

    expected_right = "RIGHT"
    actual_right = frame_page.get_right_text()

    expected_bottom = "BOTTOM"
    actual_bottom = frame_page.get_bottom_text()

    assert actual_left == expected_left, (
        f"Ожидали: {expected_left}, Получили: {actual_left}"
    )
    assert actual_right == expected_right, (
        f"Ожидали: {expected_right}, Получили: {actual_right}"
    )
    assert actual_bottom == expected_bottom, (
        f"Ожидали: {expected_bottom}, Получили: {actual_bottom}"
    )
    assert actual_middle == expected_middle, (
        f"Ожидали: {expected_middle}, Получили: {actual_middle}"
    )
