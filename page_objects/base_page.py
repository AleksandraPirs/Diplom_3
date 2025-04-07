from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    # Базовые методы взаимодействия с элементами
    @allure.step('Найти элемент на странице')
    def find_element(self, by: By, locator: str):
        """Базовый метод поиска элемента"""
        return self.driver.find_element(by, locator)

    @allure.step('Найти элементы на странице')
    def find_elements(self, by: By, locator: str):
        """Базовый метод поиска нескольких элементов"""
        return self.driver.find_elements(by, locator)

    @allure.step('Подождать видимости элемента')
    def wait_visibility_of_element(self, by: By, locator: str, timeout=10):
        """Ожидание видимости элемента"""
        return self.wait.until(
            EC.visibility_of_element_located((by, locator)),
            message=f"Элемент {locator} не стал видимым за {timeout} сек")

    @allure.step('Подождать кликабельности элемента')
    def wait_element_to_be_clickable(self, by: By, locator: str, timeout=10):
        """Ожидание кликабельности элемента"""
        return self.wait.until(
            EC.element_to_be_clickable((by, locator)),
            message=f"Элемент {locator} не стал кликабельным за {timeout} сек")

    # Комплексные методы
    @allure.step('Кликнуть на элемент')
    def click_on_element(self, by: By, locator: str):
        """Клик по элементу с ожиданием его кликабельности"""
        element = self.wait_element_to_be_clickable(by, locator)
        self.action.move_to_element(element).click().perform()

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, by: By, locator: str, keys: str):
        """Ввод текста в поле с предварительной очисткой"""
        element = self.wait_visibility_of_element(by, locator)
        element.clear()
        element.send_keys(keys)

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source_by: By, source_locator: str,
                            target_by: By, target_locator: str):
        """Перетаскивание элемента"""
        source = self.wait_visibility_of_element(source_by, source_locator)
        target = self.wait_visibility_of_element(target_by, target_locator)
        self.action.drag_and_drop(source, target).pause(0.5).perform()

    @allure.step('Получить текст элемента')
    def get_text(self, by: By, locator: str):
        """Получение текста элемента"""
        return self.wait_visibility_of_element(by, locator).text

    @allure.step('Проверить отображение элемента')
    def is_displayed(self, by: By, locator: str):
        """Проверка видимости элемента"""
        try:
            return self.find_element(by, locator).is_displayed()
        except:
            return False

    @allure.step('Подождать исчезновения элемента')
    def wait_for_invisibility(self, by: By, locator: str, timeout=10):
        """Ожидание исчезновения элемента"""
        return self.wait.until(
            EC.invisibility_of_element_located((by, locator)),
            message=f"Элемент {locator} не исчез за {timeout} сек")

    @allure.step('Подождать изменения текста элемента')
    def wait_for_text_to_change(self, by: By, locator: str, old_text: str, timeout=10):
        """Ожидание изменения текста элемента"""
        return self.wait.until(
            EC.text_to_be_present_in_element((by, locator), old_text),
            message=f"Текст элемента {locator} не изменился за {timeout} сек")

    # Дополнительные полезные методы
    @allure.step('Скролл к элементу')
    def scroll_to_element(self, by: By, locator: str):
        """Скролл страницы к элементу"""
        element = self.wait_visibility_of_element(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получить атрибут элемента')
    def get_attribute(self, by: By, locator: str, attribute: str):
        """Получение значения атрибута элемента"""
        return self.wait_visibility_of_element(by, locator).get_attribute(attribute)