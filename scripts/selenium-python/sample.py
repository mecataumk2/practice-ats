import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


print(dir(webdriver))
browser = webdriver.Chrome()

browser.get('http://www.yahoo.com')
try:
    assert 'Yahooo' in browser.title, "Title should be yahoo."

except AssertionError as e:
    print(e)


print("After assert error")
elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)
time.sleep(3)
browser.quit()