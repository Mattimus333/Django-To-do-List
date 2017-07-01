from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Matt wants to check out this cool app, he types the address into his browser to check it out!
        self.browser.get(self.live_server_url)

        # He notices the page title and the header mention a to-do list, just what he wants.

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He's invited to insert a to-do item right off the bat.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He enters GO TO THE GYM into a text box.
        inputbox.send_keys('Go to the gym')

        # When he hits enter the page updates and he is able to see the GO TO THE GYM as an item on the list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Go to the gym')

        # There is still a text box visible so he enters DO THREE SETS OF WEIGHTED SQUATS into the box.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Do three sets of squats')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again and now shows both items on the list
        self.check_for_row_in_list_table('1: Go to the gym')
        self.check_for_row_in_list_table('2: Do three sets of squats')

        # Matt wonders if the site will remember the list, he notices there is a unique URL for him, there is some text that explains that.
        self.fail('Finish the test!')

        #  He visits the URL, his to-do list is still there!

        # He's done and exits the page.
