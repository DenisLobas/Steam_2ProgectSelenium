import allure

from base.base_class import Base
from selenium.webdriver.common.by import By

from utilits.logger import Logger


class LoginPage(Base):

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    # Locators
    user_name = "DonDelas6"
    user_password = "DonDelas123"
    input_login = "//input[@type='text']"
    input_password = "//input[@type='password']"
    login_button = "//*[@id='responsive_page_template_content']/div[3]/div[1]/div/div/div/div[2]/div/form/div[4]/button"
    global_action_link = "//a[@class='global_action_link']"

    # Methods
    def authorization(self):
        """ Метод для авторизации пользователя"""
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.get_current_url()
            self.click_element(By.XPATH, self.global_action_link, "Click global action link")
            self.get_current_url()
            self.send_keys_to_element(By.XPATH, self.input_login, self.user_name, "Input login")
            self.send_keys_to_element(By.XPATH, self.input_password, self.user_password, "Input password")
            self.click_element(By.XPATH, self.login_button, "Click login button")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
