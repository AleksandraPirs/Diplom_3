from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    # Локаторы для новых методов
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter')]")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'ingredient-item')]")
    ORDER_CONTAINER = (By.XPATH, "//div[contains(@class, 'order-container')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_CONFIRMATION_MODAL = (By.XPATH, "//div[contains(@class, 'order-confirmation')]")

    @allure.step('Кликнуть по кнопке перехода в личный кабинет в хэдере')
    def click_on_personal_account_in_header(self):
        self.click_on_element(*MainPageLocators.button_personal_account)

    @allure.step('Кликнуть по кнопке "Лента заказов" в хэдере')
    def click_header_feed_button(self):
        self.click_on_element(*MainPageLocators.button_order_feed_in_header)

    @allure.step('Переход на страницу конструктора')
    def click_on_button_constructor(self):
        self.click_on_element(*MainPageLocators.header_of_page_constructor)

    @allure.step('Получение главного заголовка конструктора')
    def get_text_on_title_of_constructor(self):
        return self.get_text(*MainPageLocators.constructor_title)

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_on_button_login_in_main(self):
        self.click_on_element(*MainPageLocators.button_login_in_main)

    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        return self.is_displayed(*MainPageLocators.confirmation_modal_of_order)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.click_on_element(*MainPageLocators.ingredient_1)

    @allure.step('Проверить отображение окна "Детали ингредиента"')
    def check_displaying_of_modal_details(self):
        return self.is_displayed(*MainPageLocators.header_of_modal_details)

    @allure.step('Проверить, что окно "Детали ингредиента" не отображается')
    def check_not_displaying_of_modal_details(self):
        self.wait_for_invisibility(*MainPageLocators.header_of_modal_details)
        return not self.is_displayed(*MainPageLocators.header_of_modal_details)

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_modal(self):
        self.click_on_element(*MainPageLocators.button_close_modal)

    @allure.step('Добавить ингредиенты в заказ')
    def drag_and_drop_ingredient_to_order(self):
        self.drag_and_drop_element(
            *MainPageLocators.burger_ingredient,
            *MainPageLocators.place_for_ingredients
        )

    @allure.step('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_text(*MainPageLocators.count_of_ingredient) or '0'

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_on_button_make_order(self):
        self.click_on_element(*MainPageLocators.button_make_order)

    @allure.step('Получить номер в окне о создании заказа')
    def get_number_of_order_in_modal_confirmation(self):
        self.wait_for_text_to_change(
            *MainPageLocators.number_of_order_in_modal_confirmation,
            '9999'
        )
        return self.get_text(*MainPageLocators.number_of_order_in_modal_confirmation)

    @allure.step('Кликнуть на кнопку закрытия окна о создании заказа')
    def click_on_button_close_confirmation_modal(self):
        self.click_on_element(*MainPageLocators.button_close_confirmation)

    @allure.step('Получить текущее значение счетчика ингредиентов')
    def get_ingredients_count(self):
        return self.get_text(*self.INGREDIENT_COUNTER) or '0'

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self):
        self.drag_and_drop_element(*self.INGREDIENT_ITEM, *self.ORDER_CONTAINER)

    @allure.step('Ожидать увеличения счетчика ингредиентов')
    def wait_for_ingredients_count_increase(self, initial_count):
        self.wait.until(
            lambda _: int(self.get_ingredients_count()) > int(initial_count),
            message=f"Счетчик не увеличился с {initial_count}"
        )

    @allure.step('Перейти на страницу логина')
    def go_to_login_page(self):
        self.click_on_element(*self.LOGIN_BUTTON)

    @allure.step('Отправить заказ')
    def submit_order(self):
        self.click_on_element(*self.MAKE_ORDER_BUTTON)

    @allure.step('Проверить отображение модального окна подтверждения заказа')
    def is_order_confirmation_modal_displayed(self):
        return self.is_displayed(*self.ORDER_CONFIRMATION_MODAL)

    @allure.step('Проверить авторизацию пользователя')
    def is_user_logged_in(self):
        return self.is_displayed(*MainPageLocators.button_make_order)