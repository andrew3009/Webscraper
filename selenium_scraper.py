from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.options import Options

chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)
options = webdriver.ChromeOptions()
options.binary_location = chrome_bin
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
# options.add_argument('--headless')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)

driver.get("https://www.game.co.uk/webapp/wcs/stores/servlet/HubArticleView?langId=44&searchBtn=z&msg=&showResultsPage=true&DM_PersistentCookieCreated=true&sType=SimpleSearch&hubId=2646251&predictiveSearchURL=&resultCatEntryType=2&articleId=2646251&catalogId=10201&pageView=image&searchCount=1&searchTerm=ps5&storeId=10151&beginIndex=0&pageSize=48&ddkey=http%3AAjaxCatalogSearch")

def basketLoop():
  try:
    # print('In Basket Loop')
    # checkout = WebDriverWait(driver, 20).until(
    #   EC.presence_of_element_located((By.CLASS_NAME, "cta-large"))
    # )
    # print('did it find checkout')
    # checkout.click()
    
    driver.get('https://www.game.co.uk/webapp/wcs/stores/servlet/GameAccountNewCheckout?rewardPoints=&catalogId=10201&langId=44&storeId=10151&mobileFlag=false')
    
    print('Checkout')
    print('FINISHED')
  except:
    driver.refresh()
    sleep(3)
    basketLoop()

def checkoutLoop():
  try:
    pre = WebDriverWait(driver, 20).until(
      EC.presence_of_element_located((By.CLASS_NAME, "addToBasket"))
    )
    pre.click()
    print('Added to Basket')

    sleep(3)
    driver.refresh()
    
    print('Page Refreshed')

    # basket = WebDriverWait(driver, 20).until(
    #   EC.presence_of_element_located((By.ID, "basketLink"))
    # )
    basket = driver.find_element_by_id('basketLink')
    basket.click()
    
    print('Clicked on Basket Link')
    
    basketLoop()
  except:
    checkoutLoop()

def loopFunc():
  try:
    print('2')
    
    primary = WebDriverWait(driver, 20).until(
      EC.presence_of_element_located((By.ID, "primary"))
    )

    sections = primary.find_elements_by_id('contentPanels2')
    for section in sections:
      button = section.find_element_by_class_name('sectionButton')
      a = button.find_element_by_tag_name('a')
      print(a.get_attribute("href"))

      if 'dualsense' in a.get_attribute("href"):
        print('Found DualSense')
        a.click()
        checkoutLoop()
  except:
    print('Out of Stock')
    driver.refresh()
    loopFunc()

loopFunc()