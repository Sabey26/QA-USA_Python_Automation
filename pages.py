import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import helpers


# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    DRIVE_ICON_LOCATOR = (By.XPATH, '(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, '(//div[contains(text(),"Add a driver")])[2]')
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    DATE_OF_BIRTH_LOCATOR = (By.ID, 'birthDate')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and text()="Add"]')
    ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Add a driver")]')
    VERIFICATION_TEXT_LOCATOR = (By.XPATH, '//div[@class="section active"]//div[@style="margin-bottom: 30px;"]')
    DURATION_TEXT_LOCATOR = (By.XPATH, '//div[contains(text(),"Duration")]')
    CALL_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    ACTIVE_CAR_LOCATOR = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    SUPPORTIVE_CAR_ICON= (By.XPATH, '//div[text()="Supportive"]')
    PHONE_NUMBER_LOCATOR = (By.XPATH, '//div[@class="np-text"]')
    PHONE_NUMBER_INPUT = (By.ID, 'phone')
    PHONE_NUMBER_SUBMIT = (By.XPATH, '//button[text() = "Next"]')
    PHONE_CODE_LOCATOR = (By.ID, 'code')
    CONFIRM_BUTTON_CODE_LOCATOR = (By.XPATH, '//button[@type="submit" and text()="Confirm"]')
    PAYMENT_METHOD_LOCATOR = (By.CLASS_NAME, "pp-value-text")
    ADD_CARD_LOCATOR = (By.XPATH, '//div[text()="Add card"]')
    ADD_CARD_NUMBER_LOCATOR = (By.ID, 'number')
    ADD_CARD_CODE_LOCATOR = (By.XPATH,'//input[@class="card-input" and @id="code"]')
    CARD_NUMBER_INPUT_LOCATOR = (By.ID, "number")
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and text()="Link"]')
    CLOSE_PAYMENT_METHOD_LOCATOR = (By.CSS_SELECTOR, ".payment-picker .close-button.section-close")
    MESSAGE_FOR_DRIVER_LOCATOR = (By.ID, "comment")
    AMOUNT_OF_ICE_CREAM_LOCATOR = (By.CLASS_NAME, "counter-value")
    ICE_CREAMS_LOCATOR = (By.CLASS_NAME, "counter-plus")
    BLANKET_AND_HANDKERCHIEF_SWITCH_LOCATOR = (By.XPATH, '//div[@class="switch"] ')
    BLANKET_AND_HANDKERCHIEF_SWITCH_INPUT_LOCATOR = (By.XPATH, '//input[@class="switch-input" and @type="checkbox"] ')
    CAR_SEARCH_WINDOW_LOCATOR= (By.CLASS_NAME, "order-body")
    ORDER_BUTTON_LOCATOR= (By.CLASS_NAME, "smart-button-wrapper")

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_call_taxi_option(self):
        # Click Call taxi
        self.driver.find_element(*self.CALL_TAXI_BUTTON_LOCATOR).click()

    def set_route(self, from_location, to_location):
        self.enter_from_location(from_location)
        self.enter_to_location(to_location)
        self.click_call_taxi_option()
    def get_from(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property("value")

    def get_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property("value")

    def click_supportive_icon(self):
        # Click Supportive
        self.driver.find_element(*self.SUPPORTIVE_CAR_ICON).click()

    def get_supportive_text(self):
            # Return Supportive text
        return self.driver.find_element(*self.ACTIVE_CAR_LOCATOR).text

    def click_phone_number(self):
        # Click Phone Number
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()

    def enter_phone_number(self, number):
        # Enter Phone number
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(number)

    def submit_phone_number(self):
        # Submit Phone number
        self.driver.find_element(*self.PHONE_NUMBER_SUBMIT).click()

    def enter_sms_code(self, code):
        # Enter and submit sms code
        self.driver.find_element(*self.PHONE_CODE_LOCATOR).send_keys(code)

    def click_confirm_code(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_CODE_LOCATOR).click()

    def fill_phone_number(self, enter_phone):
        self.click_phone_number()
        time.sleep(1)
        self.enter_phone_number(enter_phone)
        self.submit_phone_number()
        time.sleep(3)
        code= helpers.retrieve_phone_code(self.driver)
        self.enter_sms_code(code)
        self.click_confirm_code()

    def get_enter_phone(self):
        return self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).text

    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    def click_add_card_number(self):
        # Click Add Card Number
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    def add_card_number(self, card_number):
        # Click Add Card Number
        self.driver.find_element(*self.CARD_NUMBER_INPUT_LOCATOR).send_keys(card_number)

    def card_code(self, code):
        # Enter Code
        self.driver.find_element(*self.ADD_CARD_CODE_LOCATOR).send_keys(code)
        self.driver.find_element(*self.ADD_CARD_CODE_LOCATOR).send_keys(Keys.TAB)

    def link_card(self):
        # Click Link
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def close_payment(self):
        self.driver.find_element(*self.CLOSE_PAYMENT_METHOD_LOCATOR).click()

    def fill_card(self, card_number, card_code):
        self.click_payment_method()
        self.click_add_card_number()
        time.sleep(1)
        self.add_card_number(card_number)
        self.card_code(card_code)
        time.sleep(3)
        self.link_card()
        self.close_payment()

    def get_card_payment_method(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).text


    def message_for_driver(self, driver):
        # Enter Message
        self.driver.find_element(*self.MESSAGE_FOR_DRIVER_LOCATOR).send_keys(driver)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.MESSAGE_FOR_DRIVER_LOCATOR).get_property("value")

    def check_blanket_and_handkerchiefs(self):
        # Click Blanket and Handkerchiefs
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEF_SWITCH_INPUT_LOCATOR).get_property("checked")

    def click_blanket_and_handkerchiefs(self):
        # Click Blanket and Handkerchiefs
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEF_SWITCH_LOCATOR).click()

    def select_blanket_and_handkerchiefs(self):
        self.check_blanket_and_handkerchiefs()
        time.sleep(1)
        self.click_blanket_and_handkerchiefs()

    def get_blanket_and_handkerchiefs(self):
        return self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEF_SWITCH_INPUT_LOCATOR).get_property("checked")

    def order_2_ice_creams(self, number_ice_cream):
         for ice_cream in range(number_ice_cream):
            self.driver.find_elements(*self.ICE_CREAMS_LOCATOR)[0].click()

    def get_2_ice_creams(self):
        return self.driver.find_elements(*self.AMOUNT_OF_ICE_CREAM_LOCATOR)[0].text

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()

    def is_taxi_order_popup_displayed(self):
        return self.driver.find_element(*self.CAR_SEARCH_WINDOW_LOCATOR).is_displayed()





