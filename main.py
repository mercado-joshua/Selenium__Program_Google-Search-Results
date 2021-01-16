#===========================
# Imports
#===========================

import pyinputplus as pyip
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

#===========================
# Main App
#===========================

class Google_Search:
    def __init__(self, query):
        # Navigate to the application home page
        self.target_url = 'https://www.google.com/'
        self.query = query
        self.create_session()
        self.search_query()

    def create_session(self):
        """Create a new Firefox session."""
        self.driver = wd.Firefox(executable_path=r'C:\\Python\\Selenium\\Firefox\\geckodriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(self.target_url)

    def search_query(self):
        # get the search textbox
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys(self.query)
        search_field.send_keys(Keys.ENTER)
        self.get_results()

    def display_results(self, min):
        i = 0
        for item in self.lists:
            print(f'{item.get_attribute("innerHTML")}\n')
            i += 1
            if i > min:
                break

    def get_results(self):
        """get the list of elements which are displayed after the search."""
        # currently on result page using find_elements_by_class_name method
        self.lists = self.driver.find_elements_by_class_name('tF2Cxc')

        # get the number of elements found
        print (f'Found {len(self.lists)} searches:\n')
        self.display_results(10)

def main():
    query = pyip.inputStr('Search: ')
    app = Google_Search(query)

#===========================
# Start App
#===========================

if __name__ == '__main__':
    main()