import random

from pages.slider_page import SliderPage


def test_slider(page):
    slider = SliderPage(page)
    slider.open()
    slide_values = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    random_value = random.choice(slide_values)
    slider.set_slider_value(random_value)
    result = float(slider.get_slider_value())
    assert result == random_value
