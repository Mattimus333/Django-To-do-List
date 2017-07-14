from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_error_messages_are_cleared_on_input(self):

        # Matt starts a list and causes a validation error, silly Matt!
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Be shampionship')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Be shampionship')
        self.get_item_input_box().send_keys('Be shampionship')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertTrue(
            self.get_error_element().is_displayed()
        ))

        # He starts typing a new item in the input box
        self.get_item_input_box().send_keys('w')

        # The error message goes away!
        self.wait_for(lambda: self.assertFalse(
            self.get_error_element().is_displayed()
        ))

    def test_cannot_add_empty_list_items(self):
        # Matt goes to the home page and accidentally tries to submit
        # an empty list item. He hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The browser intercepts the request, and does not load the
        # list page
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
        ))

        # He starts typing some text for the new item and the error disappears
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
        ))

        # And she can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # He now decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Again, the browser will not comply
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:valid'
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_list_items(self):

        # He starts by adding an item to a list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy mints')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy mints')

        # He accidently tries to add the same item
        self.get_item_input_box().send_keys('Buy mints')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # He sees a helpful error message
        self.wait_for(lambda: self.assertEqual(
            self.get_error_element().text, "You've already got this in your list"
        ))
