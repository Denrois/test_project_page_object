from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, element):
        try:
            assert self.browser.find_element(*element)
        except NoSuchElementException:
            return False
        return True

    def text_in_elements_match(self, first, second):
        first_element = self.browser.find_element(*first).text
        second_element = self.browser.find_element(*second).text
        return first_element == second_element
