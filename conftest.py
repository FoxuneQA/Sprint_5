# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, RegistrationPageLocators
from generator import generate_unique_email, generate_password
from urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture
def registered_user(driver, wait):
    """Фикстура для регистрации и входа пользователя"""
    driver.get(Urls.REGISTER)
    
    email = generate_unique_email()
    password = generate_password()
    name = "Георгий"
    
    # Заполняем форму регистрации
    wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NAME_INPUT)).send_keys(name)
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    
    # Ждем перехода на страницу логина
    wait.until(EC.url_to_be(Urls.LOGIN))
    
    # Логинимся
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
    # Ждем перехода на главную страницу
    wait.until(EC.url_to_be(Urls.MAIN))
    
    return email, password


@pytest.fixture
def login_user(driver, wait):
    """Фикстура для входа существующего пользователя"""
    def _login(email, password):
        driver.get(Urls.LOGIN)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wait.until(EC.url_to_be(Urls.MAIN))
    return _login