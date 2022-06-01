from selenium import webdriver

def smokeTest():
    driver = webdriver.Firefox(executable_path='/home/emperor/Projects/Software/gecko/geckodriver')
    driver.get("http://127.0.0.1:3000")
    element = driver.find_element_by_xpath('//pre')
    if ( element.text == 'Hello Sojith Sugadan'):
        print("smoketest_selenium.py -- " + "Smoke Test Passed")
    else:
        print("smoketest_selenium.py -- " + "Smoke Test Failed")
    driver.quit()
