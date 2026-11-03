import random

from pages.slider_page import SliderPage
from ui.page_actions import PageActions


def test_slider(page):
    page_actions = PageActions(page)
    slider = SliderPage(page)
    page_actions.goto("/horizontal_slider")

    min_value = slider.get_min_value()
    max_value = slider.get_max_value()
    step = slider.get_step()

    step_count = int((max_value - min_value) / step)
    random_step = random.randint(0, step_count)
    expected_result = min_value + random_step * step
    slider.set_slider_value(random_step)
    actual_result = float(slider.get_slider_value())
    assert actual_result == expected_result, (
        f"Ожидали: {expected_result}, Получили: {actual_result}"
    )
