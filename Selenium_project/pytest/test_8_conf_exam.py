import pytest

@pytest.mark.usefixtures('init_driver')
class Test_Google():

    def test_google_title(self):
        self.driver.get('http://www.google.com')
        assert self.driver.title == 'Google'

    def test_google_Url(self):
        text =None
        self.driver.get('http://www.google.com')
        url = self.driver.current_url
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"

