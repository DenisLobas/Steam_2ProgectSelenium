import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.common.action_chains import ActionChains


class Base:
    base_url = "https://store.steampowered.com"

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Метод для проверки корректности url"""
        get_url = self.driver.current_url
        print("\nCurrent url: " + get_url)

    def assert_current_element(self, word, result):
        """Метод для проверки корректности элемента"""
        value_ward = word.text
        assert value_ward == result
        print(f"Current element: {value_ward}")

    def assert_current_value(self, word, result):
        """Метод для проверки корректности элемента"""
        assert word == result
        print(f"Current element: {word}")

    def get_screenshot(self, test):
        new_data = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name_screenshot = f"{test} " + new_data + ".png"
        self.driver.save_screenshot(f"/Users/denis/SteamProgress/screen/{name_screenshot}")

    def open_browser(self):
        self.driver.get(self.base_url)

    def scroll_to_coordinates(self, x, y):
        """Метод для скроллинга к указанным координатам (x, y)"""
        self.driver.execute_script(f"window.scrollTo({x}, {y});")

    def click_element(self, by, value, massage):
        element = WebDriverWait(self.driver, 30).until(es.element_to_be_clickable((by, value)))
        element.click()
        print(f"{massage}")

    def click_element_index(self, by, value, index, massage):
        element = WebDriverWait(self.driver, 30).until(es.element_to_be_clickable((by, f"({value})[{index}]")))
        element.click()
        print(f"{massage}")

    def click_genre(self, genre):
        get_genre = WebDriverWait(self.driver, 60).until(
            es.visibility_of_element_located(
                (By.XPATH, f"//div[@class='_12piyDV8d50GcK-wlEd3fy']//a[text()='{genre}']")))
        get_genre.click()
        print(f"Click genre: {genre}")

    def click_tap_genre(self, tap_genre):
        get_tap_genre = WebDriverWait(self.driver, 60).until(
            es.element_to_be_clickable((By.XPATH, f"//div[text()='{tap_genre}']")))
        get_tap_genre.click()
        print(f"Click genre: {tap_genre}")

    def click_element_with_java(self, by, value, massage):
        element = WebDriverWait(self.driver, 30).until(es.element_to_be_clickable((by, value)))
        self.driver.execute_script("arguments[0].click();", element)
        print(massage)

    def send_keys_to_element(self, by, value, keys, massage):
        element = WebDriverWait(self.driver, 30).until(es.visibility_of_element_located((by, value)))
        element.send_keys(keys)
        print(massage)

    def get_clickable_element(self, element):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, element)))

    def get_visibility_element(self, element):
        return WebDriverWait(self.driver, 30).until(
            es.element_to_be_clickable((By.XPATH, element)))

    def click_dialog_slider(self, x, y, element):
        action = ActionChains(self.driver)
        slider = self.driver.find_element(By.XPATH, element)
        time.sleep(3)
        action.click_and_hold(slider).move_by_offset(x, y).release().perform()
