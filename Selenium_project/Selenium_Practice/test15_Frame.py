import time

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://www.dummypoint.com/Frame.html')
assert "Selenium Template" in driver.title

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,NoSuchElementException])

frame_count= driver.find_elements(By.TAG_NAME,'iframe')
print('List of iframe: ', len(frame_count))

# Switch to iframe by index
'''time.sleep(2)
driver.switch_to.frame(1)
data = driver.find_element(By.ID, 'framename')
print('Frame name is : ',data.text)'''

'''# Switch to iframe by name
time.sleep(2)
driver.switch_to.frame("farme3")

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text)'''

"""   
# Switch to iframe by id
time.sleep(2)
driver.switch_to.frame("f4")

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text) """

# Switch to iframe by WebElement

time.sleep(2)
ele = driver.find_element(By.ID,"f2")
driver.switch_to.frame(ele)

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text)


# Switching back to normal content page from frame
time.sleep(2)
driver.switch_to.default_content()

data = driver.find_element(By.ID,"framename")
print("Webpage Name is : ",data.text)


time.sleep(3)
driver.quit()