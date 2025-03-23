# Selenium Python Cheatsheet

## 1. Setup
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

### Initialize WebDriver
```python
driver = webdriver.Chrome()  # Use Chrome
driver.get("https://example.com")  # Open URL
driver.maximize_window()  # Maximize window
driver.set_window_size(1024, 768)  # Set window size
driver.quit()  # Close browser
```

## 2. Locating Elements
### Find Single Element
```python
element = driver.find_element(By.ID, "element_id")
element = driver.find_element(By.NAME, "element_name")
element = driver.find_element(By.CLASS_NAME, "class_name")
element = driver.find_element(By.TAG_NAME, "tagname")
element = driver.find_element(By.LINK_TEXT, "Link Text")
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Partial Link")
element = driver.find_element(By.XPATH, "//tag[@attribute='value']")
element = driver.find_element(By.CSS_SELECTOR, "css.selector")
```

### Find Multiple Elements
```python
elements = driver.find_elements(By.CLASS_NAME, "class_name")  # Returns a list
```

## 3. Interacting with Elements
```python
element.click()  # Click
element.send_keys("Hello")  # Type text
element.clear()  # Clear text field
element.submit()  # Submit form
```

### Handling Buttons, Links & Checkboxes
```python
driver.find_element(By.ID, "button_id").click()
driver.find_element(By.NAME, "checkbox_name").click()
```

### Dropdowns (Select Element)
```python
from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "dropdown_id"))
dropdown.select_by_visible_text("Option 1")
dropdown.select_by_value("option1")
dropdown.select_by_index(2)
```

## 4. Keyboard Actions
```python
element.send_keys(Keys.RETURN)  # Press Enter
element.send_keys(Keys.TAB)  # Press Tab
element.send_keys(Keys.CONTROL, "a")  # Select all
element.send_keys(Keys.CONTROL, "c")  # Copy
element.send_keys(Keys.CONTROL, "v")  # Paste
```

## 5. Mouse Actions
```python
actions = ActionChains(driver)
actions.move_to_element(element).perform()  # Hover
actions.double_click(element).perform()  # Double Click
actions.context_click(element).perform()  # Right Click
actions.drag_and_drop(source, target).perform()  # Drag and Drop
```

## 6. Handling Alerts
```python
alert = Alert(driver)
alert.accept()  # Click OK
alert.dismiss()  # Click Cancel
alert.send_keys("Text")  # Input text into prompt
```

## 7. Waits
### Implicit Wait (Applies to all elements)
```python
driver.implicitly_wait(10)  # Waits up to 10 seconds
```

### Explicit Wait (Waits for a specific condition)
```python
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))
```

## 8. Navigating Pages
```python
driver.back()  # Back
driver.forward()  # Forward
driver.refresh()  # Refresh
```

## 9. Handling Frames
```python
driver.switch_to.frame("frame_name")
driver.switch_to.default_content()  # Exit frame
```

## 10. Handling Multiple Windows/Tabs
```python
handles = driver.window_handles  # Get window handles
driver.switch_to.window(handles[1])  # Switch to new tab
```

## 11. Taking Screenshots
```python
driver.save_screenshot("screenshot.png")
```

## 12. Closing Browser
```python
driver.close()  # Close current tab
driver.quit()  # Close entire browser
