from selenium import webdriver
import os
import time

chromedriver = "D:/tool/chromedriver/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

options = webdriver.ChromeOptions()
options.add_extension("D:/temp/2.0.2_0.crx")

browser = webdriver.Chrome(chromedriver, chrome_options=options)

url = "chrome-extension://kekdpkbijjffmohdaonbpeeaiknhbkhj/game/index.html"
browser.get(url)

splash = browser.find_element_by_id("splash")
replay = browser.find_element_by_id("replay").find_element_by_tag_name("img")
b = browser.find_element_by_tag_name("body")

while 1:
    time.sleep(0.2)
    if replay.is_displayed() == False and splash.is_displayed() == False:
        b.click()
        print("B")

    if replay.is_displayed():
        replay.click()
        print("replay")

    if splash.is_displayed():
        splash.click()
        print("splash")

    # browser.get_screenshot_as_base64()
    # browser.save_screenshot("D:/temp/00.png")
    # png = browser.get_screenshot_as_png()
    # print(png)
