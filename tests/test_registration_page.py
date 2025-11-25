import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from generator import generate_unique_email, generate_password
from urls import Urls


class TestRegistration:

    def test_success_registration(self, driver, wait):
        driver.get(Urls.REGISTER)

        name = "Георгий"
        email = generate_unique_email()
        password = generate_password()

        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NAME_INPUT)).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        wait.until(EC.url_to_be(Urls.LOGIN))
        assert driver.current_url == Urls.LOGIN

    def test_incorrect_password_error(self, driver, wait):
        driver.get(Urls.REGISTER)

        name = "Георгий"
        email = generate_unique_email()
        password = "123"

        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NAME_INPUT)).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        error = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR))
        assert "Некорректный пароль" in error.text