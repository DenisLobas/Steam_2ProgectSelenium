import allure
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilits.logger import Logger


class CartPage(Base):

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    finish_pay_button = "//*[@id='page_root']/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/button"
    continue_product_name = "//div[@class='EflKs0JjldhDSxbUBaiOp']"
    all_final_price = "//*[@id='page_root']/div[2]/div/div[2]/div[3]/div[2]/div/div[1]/div[1]"

    # Actions
    def only_price(self):
        """Получение цены товара"""
        text = self.get_visibility_element(self.all_final_price).text
        result = text.replace("Общая стоимость", "").strip()
        return result

    # Methods
    def continue_pay(self, result, price):
        """Метод для перехода к странице оплаты товара"""
        with allure.step("Continue pay"):
            Logger.add_start_step(method="continue_pay")
            self.assert_current_element(self.get_clickable_element(self.continue_product_name), result)
            self.assert_current_value(self.only_price(), price)
            self.click_element(By.XPATH, self.finish_pay_button, "Click finish pay button")
            Logger.add_end_step(url=self.driver.current_url, method="continue_pay")
