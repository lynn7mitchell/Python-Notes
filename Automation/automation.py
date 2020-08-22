# https://selenium-python.readthedocs.io/

from selenium import webdriver
# you can also put in in your path
chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# check to see if you are on the right page by grabbing title from <head> tag
# if assert is not true then the window will close out
assert 'Selenium Easy Demo' in chrome_browser.title

show_message_button = chrome_browser.find_element_by_class_name("btn-default")

# print(show_message_button.get_attribute('innerHTML'))

# check the entire page source to see if Show Message is there
assert 'Show Message' in chrome_browser.page_source


user_message = chrome_browser.find_element_by_id('user-message')
# chrome_browser.find_element_by_css_select('#get-input > .btn)
# clear the input
user_message.clear()
# type in the input
user_message.send_keys("Stuff and things")
# click button
show_message_button.click()
# output message
output_message = chrome_browser.find_element_by_id('display')
# check output message
assert 'Stuff and things' in output_message.text

# does not always work. Call it twice if it does not work. (works at the time of coding 8-21-2020)
chrome_browser.close()
# chrome_browser.quit() closes all instances of chrome


# there are waits that you can see in the selenium documentation
# waits allow you to try to convice the site you are a human by not being as fast
# https://selenium-python.readthedocs.io/waits.html