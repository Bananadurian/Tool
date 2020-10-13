from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = 'oppo'
desired_caps['udid'] = '9d2b8de'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
desired_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#button_8 = driver.find_element_by_id('com.android.calculator2:id/digit8')
button_8 = driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="8"]')
button_add = driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="加"]')
button_subtract = driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="减"]')
button_multiply = driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="乘"]')
button_divide = driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="除"]')
button_equal = driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="等于"]')

button_8.click()
sleep(1)
button_add.click()
sleep(1)
button_8.click()
sleep(1)
button_equal.click()

sleep(1)
driver.quit()
