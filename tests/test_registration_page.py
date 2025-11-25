import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators, LoginPageLocators
from generator import generate_unique_email, generate_password
from urls import Urls


class TestRegistration:
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def test_success_registration(self):
        """Тест успешной регистрации"""
        self.driver.get(Urls.REGISTER)
        
        name = "Георгий"
        email = generate_unique_email()
        password = generate_password()

        # Заполняем форму регистрации
        self.wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # Проверяем переход на страницу логина (увеличим таймаут)
        self.wait.until(EC.url_to_be(Urls.LOGIN), message="Не произошел переход на страницу логина после регистрации")
        assert self.driver.current_url == Urls.LOGIN

    def test_incorrect_password_error(self):
        """Тест ошибки при некорректном пароле"""
        self.driver.get(Urls.REGISTER)
        
        name = "Георгий"
        email = generate_unique_email()
        password = "123"  # Слишком короткий пароль

        # Заполняем форму регистрации
        self.wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # Проверяем сообщение об ошибке
        error_element = self.wait.until(EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR))
        assert "Некорректный пароль" in error_element.text