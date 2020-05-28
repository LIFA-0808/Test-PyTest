import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_adding_button(browser):
    browser.get(link)

    time.sleep(30)

    button = len(browser.find_element_by_css_selector(".btn-add-to-basket").text)

    assert button > 0, 'no button'

    # pytest --language=es test_items.py
    # pytest --language=fr test_items.py
