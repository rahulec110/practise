import time

from Appium_Framework_1.base.DriverClass import Driver
import Appium_Framework_1.utilities.CustomLogger as cl
from Appium_Framework_1.base.BasePage import BasePage

driver1 = Driver()
log = cl.customLogger()

driver = driver1.getDriverMethod()
bp = BasePage(driver)
log.info('Launched App....')

bp.clickElement('com.android.permissioncontroller:id/permission_allow_foreground_only_button','id')
time.sleep(3)
bp.keyCode(27)
bp.clickElement('GOT IT','text')

bp.clickElement("com.oneplus.camera:id/filter_icon", 'id')
bp.clickElement('//android.widget.RelativeLayout[@content-desc="Matte"]/android.widget.ImageView', 'xpath')
bp.keyCode(27)
bp.clickElement('com.oneplus.camera:id/more_icon','id')
bp.clickElement('com.oneplus.camera:id/sub_item_panel_setting_icon','id')
bp.screenShot('screenshot_setting')
bp.scrollElement('Current version V6.0.130','text')

driver.back()
driver.back()

ele = bp.clickElement('VIDEO','text')

time.sleep(1)
for x in range(3):
    bp.keyCode(27)
    time.sleep(3)
    bp.keyCode(27)
    time.sleep(2)

bp.clickElement("com.oneplus.camera:id/capture_mode_indicator_slowmotion", "id")
time.sleep(1)
for x in range(2):
    bp.keyCode(27)
    time.sleep(5)
    bp.keyCode(27)
    time.sleep(2)

bp.clickElement("TIME-LAPSE" , 'text')
bp.keyCode(27)
time.sleep(5)
bp.keyCode(27)


driver.start_activity("com.skill2lead.appiumdemo", "com.skill2lead.appiumdemo.MainActivity")
bp.screenShot("launcher app screen")
bp.clickElement("com.skill2lead.appiumdemo:id/ContactUs","id")
driver.back()
bp.scrollElement("AUTO SUGGESTION",'text')


