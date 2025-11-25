from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

    LOGIN_LINK_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    LOGIN_LINK_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]/parent::a")
    LOGIN_LINK_REGISTER = (By.XPATH, "//a[contains(text(), 'Войти')]")

    LOGIN_LINK_FORGOT_PASSWORD = (By.XPATH, "//a[@href='/login']")

    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")


class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")

    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")


class AccountPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]/parent::a")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")

    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class,'Modal_modal_overlay')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal_close')]")


class ConstructorLocators:
    BUNS_TAB = (By.XPATH, "//span[contains(text(), 'Булки')]/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[contains(text(), 'Соусы')]/parent::div")
    TOPPINGS_TAB = (By.XPATH, "//span[contains(text(), 'Начинки')]/parent::div")

    BUNS_SECTION = (By.XPATH, "//h2[contains(text(), 'Булки')]")
    SAUCES_SECTION = (By.XPATH, "//h2[contains(text(), 'Соусы')]")
    TOPPINGS_SECTION = (By.XPATH, "//h2[contains(text(), 'Начинки')]")