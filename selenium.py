# Selenium Python Cheatsheet

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com")
driver.maximize_window()
driver.set_window_size(1024, 768)
driver.quit()

# Locating Elements
element = driver.find_element(By.ID, "element_id")
elements = driver.find_elements(By.CLASS_NAME, "class_name")

# Interacting with Elements
element.click()
element.send_keys("Hello")
element.clear()
element.submit()

# Handling Dropdowns
dropdown = Select(driver.find_element(By.ID, "dropdown_id"))
dropdown.select_by_visible_text("Option 1")
dropdown.select_by_value("option1")
dropdown.select_by_index(2)

# Keyboard Actions
element.send_keys(Keys.RETURN)
element.send_keys(Keys.TAB)
element.send_keys(Keys.CONTROL, "a")

actions = ActionChains(driver)
actions.move_to_element(element).perform()
actions.double_click(element).perform()
actions.context_click(element).perform()

# Handling Alerts
alert = Alert(driver)
alert.accept()
alert.dismiss()
alert.send_keys("Text")

# Waits
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))

# Navigating Pages
driver.back()
driver.forward()
driver.refresh()

# Handling Frames
driver.switch_to.frame("frame_name")
driver.switch_to.default_content()

# Handling Multiple Windows/Tabs
handles = driver.window_handles
driver.switch_to.window(handles[1])

# Taking Screenshots
driver.save_screenshot("screenshot.png")

# Closing Browser
driver.close()
driver.quit()
