from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'oppo'
desired_caps['udid'] = '9d2b8de'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
#desired_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

sleep(5)
driver.quit()
