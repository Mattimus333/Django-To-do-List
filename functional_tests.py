from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Matt wants to check out this cool app, he types the address into his browser to check it out!
        self.browser.get('http://localhost:8000')

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Go to the gym' for row in rows)
        )

        # There is still a text box visible so he enters DO THREE SETS OF WEIGHTED SQUATS into the box.
        self.fail('Finish the test!')

        # The page updates again and now shows both items on the list

        # Matt wonders if the site will remember the list, he notices there is a unique URL for him, there is some text that explains that.

        #  He visits the URL, his to-do list is still there!

        # He's done and exits the page.
if __name__ == '__main__':
    unittest.main()
