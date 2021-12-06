import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.hubzu.com/')
wait = WebDriverWait(driver, 20,poll_frequency=1, ignored_exceptions=(NoSuchElementException,TimeoutException))

print('The title of the page: ',driver.title)
status = wait.until(ec.title_is('Homes For Sale | Online Real Estate Auctions | Properties | Hubzu'))
print('Is page title is matched: ',status)



driver.find_element_by_link_text('start my search.').click()
buy_ele = driver.find_element_by_id('buyAHomeMenu')
action = ActionChains(driver)
action.move_to_element(buy_ele).perform()
driver.find_element_by_link_text('All Auctions').click()
time.sleep(3)
'''Window handles '''
parent_window = driver.current_window_handle
print('Parent window name is: ', parent_window)

'''Click for next window'''
driver.find_element_by_id('img-property-tuple-88516489772').click()

child_window = driver.window_handles
print("Type of all windows: ", type(child_window))
for child in child_window:
    print(child)
    if parent_window != child:
        print('Switching to new window...')
        driver.switch_to.window(child)
        url_status = wait.until(ec.url_contains('88516489772-127-SWEETGRASS-LN'))
        print('Status of url: ',url_status)
        url= driver.current_url
        print('Url of child window: ',url)
        time.sleep(2)
        driver.close()

driver.switch_to.window(parent_window)
city_id = url[31:42]
print(city_id)
driver.find_element_by_id('googleAPI_result_1_1').send_keys(city_id)
wait.until(lambda x:x.find_element_by_id('search-button')).click()

time.sleep(10)
driver.quit()