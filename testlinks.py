from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." in driver.page_source
# print(driver.get_screenshot_as_file('screen.png'))
# driver.close()

base_url = "https://visa.1point3acres.com/"
aquery = "h1b/salary/job-science-teacher/city-phoenix,az/"
driver = webdriver.Chrome()
driver.get(base_url+aquery)
# time.sleep(5)
#doc = driver.find_element(By.XPATH, '//li[@title="Next Page"]/button')   #//button[@class="ant-pagination-item-link"], //a[@href="/h1b/lca/2022/I-200-22104-068585"]
try:
    next_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//li[@title="Next Page"]/button'))
    )
    
    next_button.click()
    time.sleep(15)
    
    data_element = driver.find_element(By.ID, "__NEXT_DATA__")
    data = data_element.get_attribute('innerHTML')
    print(data)
    # page = requests.get(driver.page_source)
    # soup = BeautifulSoup(page.content)
    # mainTable = soup.find('table')
    # print(mainTable)
finally:  
    driver.quit() 

#print(driver.get_screenshot_as_file('screen.png'))

# time.sleep(5)
# print(doc)