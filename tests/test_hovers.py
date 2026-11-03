from pages.hovers_page import HoversPage
from ui.page_actions import PageActions


def test_hovers_page(page):
    page_actions = PageActions(page)
    hovers_page = HoversPage(page)
    page_actions.goto("/hovers")

    users_count = hovers_page.get_users_count()

    for index in range(users_count):
        hovers_page.hover_user(index)
        expected_name = f"name: user{index + 1}"
        actual_name = hovers_page.get_user_name(index)
        assert actual_name == expected_name, (
            f"Ожидали: {expected_name}, Получили: {actual_name}"
        )
        expected_link = f"/users/{index + 1}"
        actual_link = hovers_page.get_profile_link(index)
        assert actual_link == expected_link, (
            f"Ожидали: {expected_link}, Получили: {actual_link}"
        )
