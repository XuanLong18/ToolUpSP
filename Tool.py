
import time
from selenium import webdriver

class RBauto:
    def __init__(self):
        self.chrome_driver=webdriver.Chrome(executable_path="C:\\Users\\LongTx\\Documents\\ToolUpSP\\chromedriver.exe")
        self.chrome_driver.maximize_window()
    def Login(self):
        self.chrome_driver.get("https://www.redbubble.com/auth/login")
        txtEmail = self.chrome_driver.find_element_by_id("ReduxFormInput1")
        txtEmail.send_keys("lkeangnam2920@gmail.com")
        txtPass = self.chrome_driver.find_element_by_id("ReduxFormInput2")
        txtPass.send_keys("Chipchip@1882")
        txtPass.send_keys(Keys.ENTER)
        time.sleep(10)
        self.chrome_driver.quit()
        



