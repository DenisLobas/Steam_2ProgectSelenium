import allure
from base.base_class import Base
from utilits.logger import Logger


class CheckoutPage(Base):

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    block_header = "//div[@class='block_header']"

    # Methods
    def finish_checkout(self, test):
        """Метод содержащий финальные проверки товара при оплате"""
        with allure.step("Finish checkout"):
            Logger.add_start_step(method="finish_checkout")
            self.get_current_url()
            self.assert_current_element(self.get_visibility_element(self.block_header), "СПОСОБЫ ОПЛАТЫ")
            self.get_screenshot(test)
            Logger.add_end_step(url=self.driver.current_url, method="finish_checkout")
