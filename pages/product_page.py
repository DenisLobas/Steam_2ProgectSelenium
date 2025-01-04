import allure
from base.base_class import Base
from selenium.webdriver.common.by import By
from utilits.logger import Logger


class ProductPage(Base):

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    product_name = "//div[@class='apphub_AppName']"
    cart_button = "//a[@class='btn_green_steamui btn_medium']"
    continue_pay_button = "/html/body/div[3]/dialog/div/div[2]/div/div[3]/div/div[3]/button[2]"
    continue_product_name = "//div[@class='EflKs0JjldhDSxbUBaiOp']"
    final_price = "//div[@class='pk-LoKoNmmPK4GBiC9DR8']"
    value_final_price = None

    # Actions
    def check_price(self):
        self.value_final_price = self.get_clickable_element(self.final_price).text
        print(f"Цена продукта: {self.value_final_price} ")

    # Methods
    def select_product_with_search(self, result):
        """Метод для выбора товара при использовании быстрога поиска"""
        with allure.step("Select product with search"):
            Logger.add_start_step(method="select_product_with_search")
            self.get_current_url()
            self.assert_current_element(self.get_visibility_element(self.product_name), result)
            self.scroll_to_coordinates(0, 500)
            self.click_element(By.XPATH, self.cart_button, "Click cart button")
            self.assert_current_element(self.get_clickable_element(self.continue_product_name), result)
            self.check_price()
            self.click_element(By.XPATH, self.continue_pay_button, "Click Continue Pay Button")
            Logger.add_end_step(url=self.driver.current_url, method="select_product_with_search")

    def select_product_with_filter(self, result):
        """Метод для выбора товара при использовании фильтра """
        with allure.step("Select product with filter"):
            Logger.add_start_step(method="select_product_with_filter")
            self.assert_current_element(self.get_clickable_element(self.continue_product_name), result)
            self.value_final_price = self.get_clickable_element(self.final_price).text
            self.check_price()
            self.click_element(By.XPATH, self.continue_pay_button, "Click continue pay button")
            Logger.add_end_step(url=self.driver.current_url, method="select_product_with_filter")
