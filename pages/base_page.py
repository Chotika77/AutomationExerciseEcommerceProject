from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    #def input_text(self, *locator, text):
    #    self.driver.find_element(*locator).send_keys(text)



    def input_text(self, text, *locator):
        self.wait_for_element_to_appear(*locator)  # Wait for the element to be visible
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    def wait_to_be_clickable(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        message = f'element {locator} not clickable' )

    def wait_to_be_clickable_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        message = f'element {locator} not clickable' ).click()

    def wait_for_element_to_appear(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
        message = f'element {locator} did not appear'
        )



    def get_current_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        #self.wait.until(EC.new_window_is_opened(current_handles=[self.get_current_window()]))
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(f'Switching to window {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])

    def close(self):
        self.driver.close()

    def switch_to_window_by_id(self, window_id):
        print(f'Switching to window {window_id}')
        self.driver.switch_to.window(window_id)

    def verify_text(self, expected_text, *locator):
        element = self.wait_for_element_to_appear(*locator)
        actual_text = element.text.strip()
        assert actual_text.lower() == expected_text.lower(), f"Expected {expected_text}, got actual {actual_text}"

    def verify_partial_text(self, expected_text, *locator):
        element = self.wait_for_element_to_appear(*locator)
        actual_text = element.text.strip()
        assert expected_text.lower() in actual_text.lower(), f"Expected {expected_text}, not shown in actual {actual_text}"

    def verify_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url,f"Expected {expected_url}, got current {current_url}"


    def verify_partial_url(self, expected_partial_url):
        current_url = self.driver.current_url
        assert expected_partial_url in current_url, f"Expected partial URL {expected_partial_url}, not in {current_url}"

    def verify_amount_item(self,expected_amount, *locator):
        actual_amount = self.find_element(*locator).text
        assert expected_amount in actual_amount,f"Expected {expected_amount}, got actual {actual_amount}"
