import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators
from urls import Urls


class TestConstructor:

    @pytest.mark.parametrize("tab_locator, section_locator", [
        (ConstructorLocators.BUNS_TAB, ConstructorLocators.BUNS_SECTION),
        (ConstructorLocators.SAUCES_TAB, ConstructorLocators.SAUCES_SECTION),
        (ConstructorLocators.TOPPINGS_TAB, ConstructorLocators.TOPPINGS_SECTION),
    ])
    def test_constructor_tabs(self, driver, wait, tab_locator, section_locator):
        driver.get(Urls.MAIN)

        if tab_locator != ConstructorLocators.BUNS_TAB:
            wait.until(EC.element_to_be_clickable(tab_locator)).click()

        section = wait.until(EC.visibility_of_element_located(section_locator))
        assert section.is_displayed()