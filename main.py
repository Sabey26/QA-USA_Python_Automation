import time

from selenium import webdriver
from pages import UrbanRoutesPage
import data
import helpers

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")


    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert page.get_from() == data.ADDRESS_FROM
        assert page.get_to() == data.ADDRESS_TO


    def test_select_plan (self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_icon()
        actual_value = page.get_supportive_text()
        expected_value = "Supportive"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.fill_phone_number(data.PHONE_NUMBER)
        assert page.get_enter_phone() == data.PHONE_NUMBER


    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        assert page.get_card_payment_method() == "Card"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert page.get_message_for_driver()== data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        page.click_supportive_icon()
        page.click_blanket_and_handkerchiefs()
        time.sleep(3)
        assert page.get_blanket_and_handkerchiefs()== True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        page.click_supportive_icon()
        page.order_2_ice_creams(2)
        time.sleep(2)
        assert page.get_2_ice_creams()== "2"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_supportive_icon()
        page.fill_phone_number(data.PHONE_NUMBER)
        time.sleep(2)
        page.message_for_driver(data.MESSAGE_FOR_DRIVER)
        page.click_order_button()
        time.sleep(2)
        assert page.is_taxi_order_popup_displayed()== True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()