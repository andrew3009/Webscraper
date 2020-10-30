from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.options import Options

# CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"

chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)
options = webdriver.ChromeOptions()
options.binary_location = chrome_bin
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument('--headless')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)

# chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', None)

# opts = Options()

# opts.binary_location = chrome_bin

# driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=opts)

driver.get("https://www.game.co.uk/webapp/wcs/stores/servlet/HubArticleView?langId=44&searchBtn=z&msg=&showResultsPage=true&DM_PersistentCookieCreated=true&sType=SimpleSearch&hubId=2646251&predictiveSearchURL=&resultCatEntryType=2&articleId=2646251&catalogId=10201&pageView=image&searchCount=1&searchTerm=ps5&storeId=10151&beginIndex=0&pageSize=48&ddkey=http%3AAjaxCatalogSearch")

# search = driver.find_element_by_xpath('//*[@id="search"]')
# search.send_keys('ps5')
# search.submit()

def checkoutLoop():
  try:
    pre = WebDriverWait(driver, 20).until(
      EC.presence_of_element_located((By.CLASS_NAME, "addToBasket"))
    )
    pre.click()
    print('Added to Basket')
    
    checkout = WebDriverWait(driver, 20).until(
      EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div/a[2]"))
    )
    
    print('checkout')
    
    checkout.click()
    print('Checkout')
    print('FINISHED')
  except:
    driver.quit()

def loopFunc():
  try:
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