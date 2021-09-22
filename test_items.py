# $ pytest -sv --language=fr --browser=chrome
import pytest

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/", 
        # "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/",
        # "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/",
]

@pytest.mark.parametrize('link', links)
def test_find_btn_add_to_basket(browser, link):
    browser.get(link)

    btn = browser.find_element_by_css_selector(".btn-add-to-basket")
    disabled = btn.get_attribute("disabled")

    assert disabled is None, "Button is disabled..."

    print(f"=> Button text is: {btn.text}")
