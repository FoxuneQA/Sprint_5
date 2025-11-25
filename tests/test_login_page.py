import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators, AccountPageLocators
from urls import Urls


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def test_login_from_main_button(self, registered_user):
        """Тест входа через кнопку 'Войти в аккаунт' на главной"""
        email, password = registered_user
        
        # Выходим из аккаунта
        self.driver.find_element(*AccountPageLocators.ACCOUNT_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()
        self.wait.until(EC.url_to_be(Urls.LOGIN))
        
        # Входим через кнопку на главной
        self.driver.get(Urls.MAIN)
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK_MAIN)).click()
        
        # Заполняем форму логина
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Надежная проверка успешного входа - ждем появления кнопки "Оформить заказ" на главной
        self.wait.until(EC.url_to_be(Urls.MAIN))
        order_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        assert order_button.is_displayed()

    def test_login_from_account_button(self, registered_user):
        """Тест входа через кнопку 'Личный кабинет'"""
        email, password = registered_user
        
        # Выходим из аккаунта
        self.driver.find_element(*AccountPageLocators.ACCOUNT_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()
        self.wait.until(EC.url_to_be(Urls.LOGIN))
        
        # Входим через кнопку личного кабинета
        self.driver.get(Urls.MAIN)
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK_ACCOUNT)).click()
        
        # Заполняем форму логина
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Надежная проверка успешного входа
        self.wait.until(EC.url_to_be(Urls.MAIN))
        order_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        assert order_button.is_displayed()

    def test_login_from_register_page(self, registered_user):
        """Тест входа через кнопку в форме регистрации"""
        email, password = registered_user
        
        # Выходим из аккаунта если залогинены
        try:
            self.driver.get(Urls.MAIN)
            self.driver.find_element(*AccountPageLocators.ACCOUNT_BUTTON).click()
            self.wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()
            self.wait.until(EC.url_to_be(Urls.LOGIN))
        except:
            pass
        
        # Переходим на страницу регистрации
        self.driver.get(Urls.REGISTER)
        
        # Ждем загрузки страницы
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")))
        
        # Находим и кликаем ссылку "Войти"
        try:
            login_links = self.driver.find_elements(By.XPATH, "//a[contains(text(), 'Войти')]")
            if login_links:
                login_links[0].click()
            else:
                self.driver.get(Urls.LOGIN)
        except:
            self.driver.get(Urls.LOGIN)
        
        # Ждем страницу логина
        try:
            self.wait.until(EC.url_to_be(Urls.LOGIN))
        except:
            self.wait.until(EC.url_contains("/login"))
        
        # Заполняем форму логина
        email_input = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)
        
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
        
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        
        # Надежная проверка успешного входа
        self.wait.until(EC.url_to_be(Urls.MAIN))
        order_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        assert order_button.is_displayed()

    def test_login_from_forgot_password_page(self, registered_user):
        """Тест входа через кнопку в форме восстановления пароля"""
        email, password = registered_user
        
        # Выходим из аккаунта если залогинены
        try:
            self.driver.get(Urls.MAIN)
            self.driver.find_element(*AccountPageLocators.ACCOUNT_BUTTON).click()
            self.wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()
            self.wait.until(EC.url_to_be(Urls.LOGIN))
        except:
            pass
        
        # Переходим на страницу восстановления пароля
        self.driver.get(Urls.FORGOT_PASSWORD)
        
        # Ждем загрузки страницы
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")))
        
        # Находим и кликаем ссылку "Войти"
        try:
            login_links = self.driver.find_elements(By.XPATH, "//a[contains(text(), 'Войти')]")
            if login_links:
                login_links[0].click()
            else:
                self.driver.get(Urls.LOGIN)
        except:
            self.driver.get(Urls.LOGIN)
        
        # Ждем страницу логина
        self.wait.until(EC.url_to_be(Urls.LOGIN))
        
        # Заполняем форму логина
        email_input = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)
        
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
        
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        
        # Надежная проверка успешного входа
        self.wait.until(EC.url_to_be(Urls.MAIN))
        order_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        assert order_button.is_displayed()