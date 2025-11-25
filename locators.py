from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGIN_LINK_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    LOGIN_LINK_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    LOGIN_LINK_REGISTER = (By.XPATH, "//a[contains(@href, '/login')]")
    LOGIN_LINK_FORGOT_PASSWORD = (By.XPATH, "//a[contains(@href, '/login')]")

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")

class AccountPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")

class ConstructorLocators:
    BUNS_TAB = (By.XPATH, "//span[contains(text(), 'Булки')]/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[contains(text(), 'Соусы')]/parent::div")
    TOPPINGS_TAB = (By.XPATH, "//span[contains(text(), 'Начинки')]/parent::div")
    BUNS_SECTION = (By.XPATH, "//h2[contains(text(), 'Булки')]")
    SAUCES_SECTION = (By.XPATH, "//h2[contains(text(), 'Соусы')]")
    TOPPINGS_SECTION = (By.XPATH, "//h2[contains(text(), 'Начинки')]")
    CURRENT_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")