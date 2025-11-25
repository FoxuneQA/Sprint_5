import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import AccountPageLocators
from urls import Urls


class TestAccountPage:

    def test_go_to_account(self, driver, wait, registered_user):
        driver.get(Urls.MAIN)

        wait.until(EC.element_to_be_clickable(AccountPageLocators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.ACCOUNT))

        assert driver.current_url == Urls.ACCOUNT

    def test_logout(self, driver, wait, registered_user):
        driver.get(Urls.MAIN)

        wait.until(EC.element_to_be_clickable(AccountPageLocators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.ACCOUNT))

        wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.LOGIN))

        assert driver.current_url == Urls.LOGIN

    def test_go_to_constructor_from_account(self, driver, wait, registered_user):
        driver.get(Urls.MAIN)

        wait.until(EC.element_to_be_clickable(AccountPageLocators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.ACCOUNT))

        wait.until(EC.element_to_be_clickable(AccountPageLocators.CONSTRUCTOR_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.MAIN))

        assert driver.current_url == Urls.MAIN

    def test_go_to_constructor_via_logo(self, driver, wait, registered_user):
        driver.get(Urls.MAIN)

        wait.until(EC.element_to_be_clickable(AccountPageLocators.ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.ACCOUNT))

        wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGO_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.MAIN))

        assert driver.current_url == Urls.MAIN