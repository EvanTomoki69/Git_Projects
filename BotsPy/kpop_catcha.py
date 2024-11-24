from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# 01 Create a new Chrome driver instance
selDriver = webdriver.Chrome()

# 02 Go to web address
selDriver.get("https://www.dabeme.com.br/top100/?sfnsn=scwspwa")

# 03 Manage window
selDriver.maximize_window()

# 04 Get the title of the web page and print it out as a log message
kpopTitle = selDriver.title
print("The title is: ", kpopTitle)

# 05 Try block to interact with button01 
try:
     jennieButton = WebDriverWait(selDriver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='JENNIE (BLACKPINK)']"))
     )
     jennieButton.click()
     print("jennieButton clicked successfully!")
except Exception as selException:
     print("Error occurred:", selException)

# 06 button interaction02
try:
     jessicaButton = WebDriverWait(selDriver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='JESSICA']"))
     )
     jessicaButton.click()
     print("jessicaButton clicked successfully!")
except Exception as selException:
     print("Error occurred:", selException)

# 07 button interaction03
try:
     jisooButton = WebDriverWait(selDriver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='JISOO (BLACKPINK)']"))
     )
     jisooButton.click()
     print("jisooButton clicked successfully!")
except Exception as selException:
     print("Error occurred:", selException)

# 08 Scrolling interaction
selDriver.execute_script("window.scrollTo(0, 1000);")
print("Scrolling done!")

#09 Captcha solving
iframeCaptcha = selDriver.find_element(By.XPATH, "//div[@class='g-recaptcha']")
#Create instance of an ActionChain
actions = ActionChains(selDriver)
# Move to a specific location relative to the base element
# For example, hover 50 pixels to the right and 20 pixels down from the base element
actions.move_to_element_with_offset(iframeCaptcha, 50, 20).perform()
print("Element locked!")

#Webos, no puedes saltar el captcha xD