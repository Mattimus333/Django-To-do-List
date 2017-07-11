from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):

        # Matt wants to check out this cool app, he types the address into his browser to check it out!
        self.browser.get(self.live_server_url)

        # He notices the page title and the header mention a to-do list, just what he wants.

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He's invited to insert a to-do item right off the bat.
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He enters GO TO THE GYM into a text box.
        inputbox.send_keys('Go to the gym')

        # When he hits enter the page updates and he is able to see the GO TO THE GYM as an item on the list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Go to the gym')

        # There is still a text box visible so he enters DO THREE SETS OF WEIGHTED SQUATS into the box.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Do three sets of squats')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again and now shows both items on the list
        self.wait_for_row_in_list_table('1: Go to the gym')
        self.wait_for_row_in_list_table('2: Do three sets of squats')

        # Satified, he goes to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Matt starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Go to the gym')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Go to the gym')

        # He notices that the list has a unique URL
        matt_list_url = self.browser.current_url
        self.assertRegex(matt_list_url, '/lists/.+')

        # Now a new user, Alex, comes to the site

        ## We use a new browser session to make sure that no information of
        ## Matt's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Alex visits the homepage, there is no sign of Matt's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Go to the gym', page_text)

        # Alex starts a new list by entering a new item.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy beans')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy beans')

        # Alex gets his own unique URL
        alex_list_url = self.browser.current_url
        self.assertRegex(alex_list_url, '/lists/.+')
        self.assertNotEqual(alex_list_url, matt_list_url)

        # Again, there is no trace of Matt's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Go to the gym', page_text)
        self.assertIn('Buy beans', page_text)
