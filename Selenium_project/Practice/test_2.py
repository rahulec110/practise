import pytest

@pytest.mark.usefixtures('init_driver')
class Test_GreyT():
    pass

class Test(Test_GreyT):

    def test_page_title(self):
        self.driver.title == 'greytHR'

    def test_google_Url(self):

        url = self.driver.current_url
        assert self.driver.current_url == "https://zentree.greythr.com/v3/portal/ess/home"