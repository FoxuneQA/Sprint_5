import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators
from urls import Urls


class TestConstructor:
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @pytest.mark.parametrize("tab_locator,section_locator,expected_text", [
        (ConstructorLocators.BUNS_TAB, ConstructorLocators.BUNS_SECTION, "Булки"),
        (ConstructorLocators.SAUCES_TAB, ConstructorLocators.SAUCES_SECTION, "Соусы"),
        (ConstructorLocators.TOPPINGS_TAB, ConstructorLocators.TOPPINGS_SECTION, "Начинки")
    ])
    def test_constructor_tabs(self, tab_locator, section_locator, expected_text):
        """Параметризованный тест разделов конструктора"""
        self.driver.get(Urls.MAIN)
        
        # Ждем загрузки страницы
        self.wait.until(EC.element_to_be_clickable(tab_locator))
        
        # Кликаем на вкладку с помощью JavaScript для избежания перехвата клика
        tab_element = self.driver.find_element(*tab_locator)
        self.driver.execute_script("arguments[0].click();", tab_element)
        
        # Проверяем, что вкладка активна
        self.wait.until(EC.visibility_of_element_located(section_locator))
        
        # Проверяем, что отображается соответствующий раздел
        section_element = self.driver.find_element(*section_locator)
        assert expected_text in section_element.text
        
        # Проверяем активность вкладки по классу
        tab_class = tab_element.get_attribute("class")
        assert "current" in tab_class or "tab_tab_type_current" in tab_class