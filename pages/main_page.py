import time
import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from utilits.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    search_area = "//input[@id='store_nav_search_term']"
    search_link = "//a[@id='store_search_link']"
    hidden_genre_element = "//*[@id='genre_flyout']/div/div[2]/div[7]/a[7]"
    genre_tap = "//div[@id='genre_tab']"
    game_element_cart = "//div[contains(@class, 'yoe6d_43t3I6-mjbZGkLs')]"
    product_element = "//div[@class='apphub_AppName']"
    my_profile_button = "//button[@id='account_pulldown']"
    logaut_button = "//*[@id='account_dropdown']/div/a[4]"
    delete_product = "//div[text()='Удалить все товары']"

    # Methods
    def search_product(self, name_product):
        """Метод для поиска товара с помощью поисковой строки"""
        with allure.step("Search product"):
            Logger.add_start_step(method="search_product")
            self.get_current_url()
            self.send_keys_to_element(By.XPATH, self.search_area, name_product, "Input search area")
            self.click_element_with_java(By.XPATH, self.search_link, "Click search link")
            Logger.add_end_step(url=self.driver.current_url, method="search_product")

    def logaut(self):
        """Метод для выхода с аккаунта"""
        with allure.step("Logaut"):
            Logger.add_start_step(method="logaut")
            self.click_element(By.XPATH, self.my_profile_button, "Click my profile button")
            self.click_element(By.XPATH, self.logaut_button, "Click logaut button")
            Logger.add_end_step(url=self.driver.current_url, method="logaut")

    def delete_all_product(self):
        """Метод для очистки корзины"""
        with allure.step("Delete all product"):
            Logger.add_start_step(method="delete_all_product")
            self.driver.back()
            time.sleep(1)
            self.click_element(By.XPATH, self.delete_product, "Delete all product")
            Logger.add_end_step(url=self.driver.current_url, method="delete_all_product")

    def search_product_with_filter(self):
        """Метод для поиска товара с помощью фильтров"""
        with allure.step("Search product with filter"):
            Logger.add_start_step(method="search_product_with_filter")
            self.get_current_url()
            self.get_current_url()
            self.click_element(By.XPATH, self.genre_tap, "Click genre tap")
            self.click_element(By.XPATH, self.hidden_genre_element, "Click hidden genre element")
            self.scroll_to_coordinates(0, 3300)
            self.click_tap_genre("Жанры")
            time.sleep(1)
            self.click_genre("Партийная ролевая игра")
            time.sleep(1)
            self.scroll_to_coordinates(0, 3800)
            time.sleep(1)
            self.click_tap_genre("Темы и атмосфера")
            self.click_genre("Фэнтези")
            time.sleep(1)
            self.scroll_to_coordinates(0, 4300)
            time.sleep(1)
            self.click_tap_genre("Цена")
            self.click_dialog_slider(-80, 0, "//div[@class='DialogSlider_Grabber']")
            time.sleep(1)
            self.scroll_to_coordinates(0, 3000)
            self.click_element_index(By.XPATH, self.game_element_cart, 1, "Click game element")
            time.sleep(1)
            self.click_element_index(By.XPATH, self.game_element_cart, 1, "Two click game element")
            Logger.add_end_step(url=self.driver.current_url, method="search_product_with_filter")
