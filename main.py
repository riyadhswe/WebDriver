from selenium import webdriver
browser = webdriver.Chrome('drivers/chromedriver.exe')
browser.get('https://www.pickaboo.com/customer/account/create/')
input_element = browser.find_element_by_css_selector('input[id="firstname"]')
input_element.send_keys('Mr')
input_element = browser.find_element_by_css_selector('input[id="lastname"]')
input_element.send_keys('Riyadh')
input_element = browser.find_element_by_css_selector('input[id="email_address"]')
input_element.send_keys('riyadhswe@gmail.com')
input_element = browser.find_element_by_css_selector('input[id="password"]')
input_element.send_keys('Riyadhp86@')
input_element = browser.find_element_by_css_selector('input[id="password-confirmation"]')
input_element.send_keys('Riyadhp86@')
button_element = browser.find_element_by_css_selector('button[title="Create an Account"]')
button_element.click()
button_element.click()
button_element.click()
button_element.click()
button_element.click()