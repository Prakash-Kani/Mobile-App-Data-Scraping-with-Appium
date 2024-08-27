from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

import time


def to_swipe(driver):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(497, 1330)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(556, 565)
    actions.w3c_actions.pointer_action.release()
    actions.perform()


options = AppiumOptions()
options.load_capabilities({
	"appium:automationName": "UiAutomator2",
	"appium:platformName": "Android",
	"appium:platforVersion": "11",
	"appium:deviceName": "RZ8M9257CAL",
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(519, 1696)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(510, 639)
actions.w3c_actions.pointer_action.release()
actions.perform()
el1 = driver.find_element(by=AppiumBy.ID, value="com.sec.android.app.launcher:id/app_search_edit_text")
el1.click()
time.sleep(2)
el2 = driver.find_element(by=AppiumBy.ID, value="com.samsung.android.app.galaxyfinder:id/edit_search")
el2.click()

el2.send_keys("Linkedin")
el3 = driver.find_element(by=AppiumBy.ID, value="com.samsung.android.app.galaxyfinder:id/app_icon")
el3.click()
time.sleep(6)
el4 = driver.find_element(by=AppiumBy.ID, value="com.linkedin.android:id/search_bar_text")
el4.click()
time.sleep(3)
el5 = driver.find_element(by=AppiumBy.ID, value="com.linkedin.android:id/search_bar_edit_text")
el5.click()
el5.send_keys("Python Developer")
time.sleep(2)
el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"com.linkedin.android:id/search_home_query_item\").instance(0)")
el6.click()

time.sleep(2)

el7 = driver.find_element(by=AppiumBy.ID, value="com.linkedin.android:id/search_cluster_card_action_button")
el7.click()

import time
for j in range(5):
    for i in range(6):
    
        # if i:
        try:
            xpath = f"new UiSelector().resourceId(\"com.linkedin.android:id/careers_job_item_entity_lockup\").instance({i})"
            el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=xpath)
            el8.click()
            time.sleep(2)
            company = driver.find_element(by= 'id', value= 'com.linkedin.android:id/careers_top_card_subtitle_1_v2').text
            role = driver.find_element(by= 'id', value= 'com.linkedin.android:id/entities_top_card_title_v2').text
            data = driver.find_element(by= 'id', value= 'com.linkedin.android:id/careers_top_card_tertiary_description').text.split('·')
            location = data[0]
            posted_date = data[1]
            applicant_cnt = data[2]
            careers_para = driver.find_element(by= 'id', value= 'com.linkedin.android:id/careers_paragraph_body').text
            
            print(company, role, location, posted_date, applicant_cnt)
            print(careers_para)
            driver.back()
        except Exception as e:
            print('Error Occured: \n')

        # if (i+1)%6==0:
    print('SWIPE')
    time.sleep(3)
    to_swipe(driver)
    time.sleep(3)
            