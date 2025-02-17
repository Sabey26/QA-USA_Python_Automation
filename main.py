import data
import helpers

class TestUrbanRoutes:

    # This function is figuring out if the URL works
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print ("Connected to the Urban Routes server")
        else:
            print( "Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        # Add in S8
        print("function created for set route")
        pass

    def test_select_plan (self):
        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # The loop is repeating the print function twice
        for ice_cream in range(2):
             # Add in S8
             print("function created for ice creams")
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for search model appears")
        pass