import pytest
from selenium.webdriver.support import expected_conditions as ec

@pytest.mark.usefixtures('init_driver')
class Test_flight():
    pass

class Test(Test_flight):

    def test_page_title(self):
        #self.driver.title == "Flight Booking, Flight Tickets Booking at Lowest Airfare | MakeMyTrip"
        ec.title_is("Flight Booking, Flight Tickets Booking at Lowest Airfare | MakeMyTrip")

    def test_screenshot(self):
        self.driver.get_screenshot_as_file('screenshot.png')
