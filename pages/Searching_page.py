import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilits.logger import Logger


class SearchingPage(Base):

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    product = "//span[@class='title']"

    # Methods
    def select_needed_element(self):
        """Метод для выбора нужного товара на странице поиска"""
        with allure.step("Select needed element"):
            Logger.add_start_step(method="select_needed_element")
            self.click_element(By.XPATH, self.product, "Click product")
            Logger.add_end_step(url=self.driver.current_url, method="select_needed_element")
