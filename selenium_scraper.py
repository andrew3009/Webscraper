from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
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
      button = section.find_elements_by_class_name('sectionButton')
      a = button.find_element_by_tag_name('a')

      if 'digital' in a.get_attribute("href"):
        a.click()
  except:
    print('Out of Stock')
    driver.refresh()
    loopFunc()

loopFunc()