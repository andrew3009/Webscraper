from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.options import Options

options = Options()

options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')

options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')

driver = webdriver.Chrome(executable_path=str(os.environ.get('CHROMEDRIVER_PATH')), chrome_options=options)

driver.get("https://www.game.co.uk/")

search = driver.find_element_by_xpath('//*[@id="search"]')
search.send_keys('ps5')
search.submit()

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

def checkoutLoop():
  try:
    pre = WebDriverWait(driver, 20).until(
      EC.presence_of_element_located((By.CLASS_NAME, "addToBasket"))
    )
    pre.click()
    print('Added to Basket')
    
    checkout = WebDriverWait(driver, 20).until(
      EC.presence_of_element_located((By.CLASS_NAME, "secure-checkout"))
    )
    checkout.click()
    print('Checkout')
    print('FINISHED')
  except:
    driver.quit()

loopFunc()