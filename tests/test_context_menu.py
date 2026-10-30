from pages.context_menu_page import ContextMenuPage


def test_context_menu(page):
    context_menu_page = ContextMenuPage(page)
    context_menu_page.open()
    dialog = context_menu_page.accept_context_menu()
    assert dialog == "You selected a context menu"
