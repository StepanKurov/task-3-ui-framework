from pages.hovers_page import HoversPage


def test_hovers_page(page):
    hovers_page = HoversPage(page)
    hovers_page.open()

    users_count = hovers_page.get_users_count()

    for index in range(users_count):
        hovers_page.hover_user(index)
        name = hovers_page.get_user_name(index)
        assert name == f"name: user{index + 1}"
        link = hovers_page.get_profile_link(index)
        assert link == f"/users/{index + 1}"