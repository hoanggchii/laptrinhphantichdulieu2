from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
PATH = 'chromedriver.exe'

##### Handling of Allow Pop Up In Facebook
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

driver = webdriver.Chrome(r"C:\Users\ADMIN\Downloads\chromedriver.exe")
# driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)

driver.maximize_window()
driver.get("https://www.facebook.com/")
###Login To The Account
def login(id,password):

  email = driver.find_element (By.ID, 'email')
  email.send_keys(id)
  Password = driver.find_element (By.ID, 'pass')
  Password.send_keys(password)
  button = driver.find_element (By.NAME, 'login').click()
  # button.click()
  pass
  # try:
  #   email = driver.find_element (By.ID, 'email')
  #   email.send_keys(id)
  # except NoSuchElementException:
  #     print("exception handled")
  # Password = driver.find_element (By.ID, 'pass')
  # Password.send_keys(password)
  # button = driver.find_element (By.ID, '"u_0_b"')
    

  # password.send_keys("mercury")
  # button.click()

#### Post Content On FaceBook

def post_content(content):
  # button = driver.find_element(By.NAME, 'submit_composer')
  # button.click()
  # time.sleep(3) ## A 3 second break in the program so that everythin loads perfectly
  # actions= ActionChains(driver) ##Action Chains
  # actions.send_keys(Keys.TAB)  ##Press TAB
  # actions.send_keys(Keys.ENTER) ##Press ENTER
  # actions.send_keys(content)
  # actions.send_keys(Keys.TAB * 10)  ### Press TAB 10 Times to reach POST button
  # actions.send_keys(Keys.ENTER) ### Press ENTER to post the content on facebook
  # actions.perform()  ## To perfrom all the operations in the action chains
  # pass
  # content = driver.find_element (by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div')
  # content.send_keys(id)
  
  wait = WebDriverWait(driver, 10)
  driver.get('https://facebook.com/')
  whats_on_your_mind = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]')
  # whats_on_your_mind = driver.find_element_by_xpath()
  post_input = whats_on_your_mind.find_element(by=By.XPATH, value = '..')
  post_input.click()
  wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]')))
  post_text_area = driver.find_element(by=By.XPATH, value = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/p')
  # post = input('Enter your post: ')
  # post = driver.find_element (by=By.XPATH, value = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/p/span')
  # post.send_keys(id)

  # gửi
  post_text_area.send_keys(content)
  
  post_btn = driver.find_element(by=By.XPATH, value = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div')
  post_btn.click()
  wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '')]")))

  pass
login("nhom06facebook@gmail.com","Hieu030201") 
time.sleep(5)	
content = "I am a Bot Podfghjsting ybuhj xdcfvgbhnjFacebook"  ## Demo Content
post_content(content)