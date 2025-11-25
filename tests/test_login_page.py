import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, RegistrationPageLocators
from urls import Urls


class TestLogin:

    def test_login_from_main(self, driver, wait, registered_user, logout_user):
        email, password = registered_user

        driver.get(Urls.MAIN)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK_MAIN)).click()

        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.presence_of_element_located(LoginPageLocators.ORDER_BUTTON))

    def test_login_from_account_button(self, driver, wait, registered_user, logout_user):
        email, password = registered_user

        driver.get(Urls.MAIN)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK_ACCOUNT)).click()

        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.presence_of_element_located(LoginPageLocators.ORDER_BUTTON))

    def test_login_from_register_page(self, driver, wait, registered_user, logout_user):
        email, password = registered_user

        driver.get(Urls.REGISTER)
        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)).click()

        wait.until(EC.url_to_be(Urls.LOGIN))

        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.presence_of_element_located(LoginPageLocators.ORDER_BUTTON))

    def test_login_from_forgot_password_page(self, driver, wait, registered_user, logout_user):
        email, password = registered_user

        driver.get(Urls.FORGOT_PASSWORD)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK_FORGOT_PASSWORD)).click()

        wait.until(EC.url_to_be(Urls.LOGIN))

        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.presence_of_element_located(LoginPageLocators.ORDER_BUTTON))