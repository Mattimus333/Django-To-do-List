from selenium import webdriver
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
        self.fail('Finish the test!')

        # He's invited to insert a to-do item right off the bat.

        # He enters GO TO THE GYM into a text box.

        # When he hits enter the page updates and he is able to see the GO TO THE GYM as an item on the list

        # There is still a text box visible so he enters DO THREE SETS OF WEIGHTED SQUATS into the box.

        # The page updates again and now shows both items on the list

        # Matt wonders if the site will remember the list, he notices there is a unique URL for him, there is some text that explains that.

        #  He visits the URL, his to-do list is still there!

        # He's done and exits the page.
if __name__ == '__main__':
    unittest.main(warnings='ignore')
