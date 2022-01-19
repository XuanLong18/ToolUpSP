from re import A
import sys
import os
import json
import shutil
import time
from tkinter import Y, image_names
import autoit
import threading
from time import sleep
from random import randint, choice
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PyQt5.QtWidgets import *
from ToolGUI import Ui_ToolUPSP
from PyQt5 import uic

class Ui(QMainWindow):
    def __init__(self):
        self.ILLEGAL_CHARACTERS = r'\/:*?"<>|~#%&+{}'
        with open("C:\\Users\\admin\\OneDrive - Hanoi University of Mining and Geology\\Desktop\\ToolUpSP\\config.json", "r") as f:
            self.settings = json.loads(f.read())
        with open("C:\\Users\\admin\\OneDrive - Hanoi University of Mining and Geology\\Desktop\\ToolUpSP\\trademark.txt", "r", encoding="utf-8") as f:
            self.trademark_words = f.read().splitlines()
        self.chrome_driver=None
        super(Ui,self).__init__()
        uic.loadUi('C:\\Users\\admin\\OneDrive - Hanoi University of Mining and Geology\\Desktop\\ToolUpSP\\toolUpSP.ui',self)
        self.input = self.findChild(QLineEdit,'lineUser')
        self.btnStart = self.findChild(QPushButton,'pushButton')
        self.btnBrowse = self.findChild(QPushButton, 'btUpImage')
        self.textTB = self.findChild(QTextEdit, 'textTB')
        #hàm lấy file trong thư mục img -> mảng gồm tên các file
        aa = os.listdir("C:\\Users\\admin\\OneDrive - Hanoi University of Mining and Geology\\Desktop\\ToolUpSP\\img")
        self.btnStart.clicked.connect(lambda: self.upload_img(aa))
        self.btnBrowse.clicked.connect(self.select_folder_copy_img)
        self.show()
    def open_web(self):
        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir='+self.input.text())
        self.chrome_driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\OneDrive - Hanoi University of Mining and Geology\\Desktop\\ToolUpSP\\chromedriver.exe",options=options)
        self.chrome_driver.maximize_window()
    def select_folder_copy_img(self):
        selectf = QFileDialog.getOpenFileNames(self, 'Open file', 'C:\\Users')
        for i in selectf[0]:
            src_dir = i
            dst_dir = "C:\\Users\\admin\\OneDrive - Hanoi University of Mining and Geology\\Desktop\\ToolUpSP\\img"
            shutil.copy(src_dir , dst_dir)
    def upload_img(self, img_list):
        for img_name in img_list:
    
            print(img_name,type(img_name))
            img_title = img_name.split(".png")[0]
            for char in self.ILLEGAL_CHARACTERS:
                img_title = img_title.replace(char, "")
            for word in self.trademark_words:
                img_title = img_title.replace(word, "")
            img_title = " ".join(img_title.split())
            self.open_web()
            self.chrome_driver.get("https://www.redbubble.com/fr/portfolio/images/new")
            try:
                upload_btn = WebDriverWait(self.chrome_driver,3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/div[2]/form/div/div[1]/div[1]')))
                upload_btn.click()
            except Exception as e:
                return False
            # for i in range(20):
            #     if autoit.win_exists("File Upload") == 1 or autoit.win_exists("File Upload") == 0:
            #         handle_file_thread = threading.Thread(target=self.handle_upload, args=(f"C:\\Users\\admin\\OneDrive - Hanoi University of Mining and Geology\\Desktop\\ToolUpSP\\img",))
            #         handle_file_thread.start()
            #         break
            #     else:
            #         if i >=3:
            #             try:
            #                 autoit.win_close("File Upload")
            #             except Exception as e:
            #                 pass
            self.chrome_driver.find_element_by_id("select-image-single").send_keys("C:\\Users\\admin\\OneDrive - Hanoi University of Mining and Geology\\Desktop\\ToolUpSP\\img\\"+img_name)
            # self.chrome_driver.find_element_by_id("select-image-single").send_keys(Keys.ESCAPE)
            sleep(10)
            autoit.send('{ESC}')
            try:
                #WebDriverWait(self.chrome_driver, 600).until(EC.visibility_of_element_located(By.CSS_SELECTOR, '.product-selector-wrap header h2'))
                self.chrome_driver.find_element_by_id("work_title_fr").send_keys(img_title)
                self.chrome_driver.find_element_by_id("work_tag_field_fr").send_keys(img_title)
                self.chrome_driver.find_element_by_id("work_description_fr").send_keys(img_title)
                sleep(10)
                enabled_product_boxes = self.chrome_driver.find_elements(By.CSS_SELECTOR, ".product-row > div:not(.all-disabled)")
                for el in enabled_product_boxes:
                    self.scroll_to_element(el)
                    el.find_element(By.CSS_SELECTOR, ".product-buttons .disable-all").click()
                disabled_product_boxes = self.chrome_driver.find_elements(By.CSS_SELECTOR, ".product-row > div.all-disabled")
                for el in disabled_product_boxes:
                    self.scroll_to_element(el)
                    el.find_element(By.CSS_SELECTOR, ".product-buttons .enable-all").click()
                self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/div/div[1]/div[1]/div[3]/div/div").click()
                #ActionChains(self.chrome_driver).double_click("/html/body/div[41]/div[2]/div[2]/input").perform()
                self.chrome_driver.find_element_by_xpath("/html/body/div[41]/div[2]/div[2]/input").clear()
                self.chrome_driver.find_element_by_xpath("/html/body/div[41]/div[2]/div[2]/input").send_keys("#000000")
                # autoit.send('{ENTER}')
                #Standard Print Clothing
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[1]/div[1]/div[4]/div[2]/div[1]").click()
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[2]/div[2]/div[4]/div/div[1]/div/fieldset/div[2]/div[3]/label[5]").click()
                slider = self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[2]/div[2]/div[4]/div/div[1]/div/fieldset/div[3]/div[1]/input")
                ActionChains(self.chrome_driver).drag_and_drop_by_offset(slider, 100, 0).perform()
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[2]/div[2]/div[4]/div/div[1]/div/fieldset/div[3]/div[2]/button[2]").click()
                sleep(2)
                #Big print clothing
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[1]/div[2]/div[4]/div[2]/div[1]").click()
                self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[4]/div/div[2]/div[4]/div/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[2]").click()
                adjust = self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[4]/div/div[2]/div[4]/div/div[1]/div/div[1]/div[6]/div/input")
                ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust, 100, 0).perform()
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[4]/div/div[2]/div[4]/div/div[1]/div/div[1]/div[5]/button[2]").click()
                sleep(2)
                #Caps
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[1]/div[3]/div[4]/div[2]/div[1]").click()
                adjust1 = self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[6]/div/div[2]/div[3]/div/div[1]/div/div[1]/div[6]/div/input")
                ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust1, -8, 0).perform()
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[6]/div/div[2]/div[3]/div/div[1]/div/div[1]/div[5]/button[1]").click()
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[6]/div/div[2]/div[3]/div/div[1]/div/div[1]/div[5]/button[2]").click()
                sleep(2)
                # # Chiffon Tops
                # self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[7]/div[1]/div[4]/div[2]/div[1]").click()
                # adjust2 = self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[9]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust2, 100, 0).perform()
                # self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[9]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[9]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # T-shirt dresses
                # self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[7]/div[2]/div[4]/div[2]/div[1]").click()
                # adjust3 = self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[9]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust3, 100, 0).perform()
                # self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[9]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[9]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Graphic Tees
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[7]/div[3]/div[4]/div[2]/div[1]").click()
                # adjust4 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[13]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust4, 100, 0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[13]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[13]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # A-line dresses
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[14]/div[1]/div[4]/div[2]/div[1]").click()
                # adjust5 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[16]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust5, 100, 0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[16]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[16]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Stickers and magnets bỏ do k edit đc
                # # Phone Cases & Skins
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[14]/div[3]/div[4]/div[2]/div[1]").click()
                # adjust6 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[20]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust6, 20 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[20]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[20]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # XXL mouse pad chỉ đổi màu+ căn chỉnh
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[21]/div[1]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[23]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[23]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Mousepad
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[21]/div[2]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/input").send_keys("#000000")
                # adjust7 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[25]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust7, 60, 0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[25]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[25]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Cushions and tote bags k scale
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[21]/div[3]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[11]/div[2]/div[2]/input").send_keys("#000000")
                # adjust8 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[27]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust8, 70, 0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[27]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[27]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Prints, cards and posters k scale
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[28]/div[1]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[12]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[29]/div[2]/div[4]/div/div[1]/div/fieldset/div[2]/div[2]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[29]/div[2]/div[4]/div/div[1]/div/fieldset/div[2]/div[2]/button[2]").click()
                # sleep(2)
                # # Pouches, Skins & Laptop Sleeves k scale 
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[28]/div[2]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[13]/div[2]/div[2]/input").send_keys("#000000")
                # adjust9 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[31]/div/div[3]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust9, 80, 0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[31]/div/div[3]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[31]/div/div[3]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Duvet covers, bedspreads and shower curtains k scale
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[28]/div[3]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[14]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[33]/div/div[3]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[33]/div/div[3]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # mugs scale 85-> 40
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[34]/div[1]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[15]/div[2]/div[2]/input").send_keys("#000000")
                # adjust10 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[35]/div[2]/div[4]/div/div[1]/div/fieldset/div[2]/div[2]/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust10, 40, 0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[35]/div[2]/div[4]/div/div[1]/div/fieldset/div[2]/div[3]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[35]/div[2]/div[4]/div/div[1]/div/fieldset/div[2]/div[3]/button[2]").click()
                # sleep(2)
                # # Thermo mugs scale 75-> 70
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[34]/div[2]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[16]/div[2]/div[2]/input").send_keys("#000000")
                # adjust11 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[36]/div[2]/div[4]/div/div[1]/div/fieldset/div[2]/div[2]/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust11, 70, 0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[36]/div[2]/div[4]/div/div[1]/div/fieldset/div[2]/div[3]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[36]/div[2]/div[4]/div/div[1]/div/fieldset/div[2]/div[3]/button[2]").click()
                # sleep(2)
                # # Mini skirts scale 84->70
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[34]/div[3]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[17]/div[2]/div[2]/input").send_keys("#000000")
                # adjust12 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[38]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust12, 70, 0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[38]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[38]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Scarves đổi màu căn chỉnh trung tâm k di chuyển
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[39]/div[1]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[18]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[41]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[41]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                #Foulards
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[39]/div[1]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[43]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[43]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # # Tablet Cases & Skins scale 100->80
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[39]/div[2]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[19]/div[2]/div[2]/input").send_keys("#000000")
                # adjust13 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[43]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust13, 80, 0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[43]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[43]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Drawstring Bags scale 93->100
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[39]/div[3]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[20]/div[2]/div[2]/input").send_keys("#000000")
                # adjust14 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[45]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust14, 100 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[45]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[45]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Spiral Notebooks k scale
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[46]/div[1]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[21]/div[2]/div[2]/input").send_keys("#000000")
                # adjust15 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[48]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust15, 80 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[48]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[48]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Hardcover Journals scale 100->80
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[46]/div[2]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[21]/div[2]/div[2]/input").send_keys("#000000")
                # adjust16 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[48]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust16, 80 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[48]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[48]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Clocks scale 99->70
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[46]/div[3]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[21]/div[2]/div[2]/input").send_keys("#000000")
                # adjust17 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[48]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust17, 70 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[48]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[48]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Art Board Prints căn chỉnh center
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[52]/div[1]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[24]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[54]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[54]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # acrylic blocks and coasters căn chỉnh center
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[52]/div[2]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[25]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[56]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[56]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Plaids and drapes căn chỉnh center
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[52]/div[3]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[26]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[58]/div/div[3]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[58]/div/div[3]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Bath mat căn chỉnh center
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[59]/div[1]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[27]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[61]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[61]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Gourds scale 99->80
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[59]/div[2]/div[4]/div[2]/div[1]").click()
                # adjust18 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[63]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust18, 80 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[63]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[63]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Canvas and wood mounted prints căn chỉnh center
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[59]/div[3]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[28]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[65]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[65]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Classic tote bags scale 93->100
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[66]/div[1]/div[4]/div[2]/div[1]").click()
                # adjust19 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[68]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust19, 100 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[68]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[68]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Badges scale 34->25
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[66]/div[2]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[29]/div[2]/div[2]/input").send_keys("#000000")
                # adjust20 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[70]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust20, 25 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[70]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[70]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Masks scale 75->40 có thể đẩy trái
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[66]/div[3]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[30]/div[2]/div[2]/input").send_keys("#000000")
                # adjust21 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[72]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust21, 40 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[72]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[72]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Aprons căn chỉnh trung tâm
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[73]/div[1]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[31]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[75]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[75]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Puzzles căn chỉnh trung tâm
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[73]/div[2]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[32]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[77]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[77]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Double tops căn chỉnh trung tâm
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[73]/div[3]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[33]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[79]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[79]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Floor cushions căn chỉnh trung tâm
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[80]/div[1]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[34]/div[2]/div[2]/input").send_keys("#000000")
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[82]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[82]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Wallet cases k scale
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[80]/div[2]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[35]/div[2]/div[2]/input").send_keys("#000000")
                # adjust22 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[84]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust22, 70 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[84]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[84]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # leggings bỏ
                
                # # Socks bỏ 
                
                # # Backpack bỏ
                
                # # Sports bags scale 100->80
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[93]/div[1]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[39]/div[2]/div[2]/input").send_keys("#000000")
                # adjust23 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[95]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust23, 80 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[95]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[95]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # # Fitted masks scale 85->50 có thể phải di chuyển sang trái
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[93]/div[2]/div[4]/div[2]/div[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[40]/div[2]/div[2]/input").send_keys("#000000")
                # adjust24 = self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[97]/div/div[2]/div[3]/div/div[1]/div/div/div[6]/div/input")
                # ActionChains(self.chrome_driver).drag_and_drop_by_offset(adjust24, 50 ,0).perform()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[97]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[1]").click()
                # self.chrome_driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[97]/div/div[2]/div[3]/div/div[1]/div/div/div[5]/button[2]").click()
                # sleep(2)
                # product_list = self.settings['main_products'][:]
                # random_products = self.settings['random_products'][:]
                # for i in range(randint(3, 4)):
                #     tmp = choice(random_products)
                #     random_products.remove(tmp)
                #     product_list.append(tmp)
                # for el in disabled_product_boxes:
                #     if str(el.find_element(By.CSS_SELECTOR, ".preview-info .preview-name").text).strip() in product_list:
                #         self.scroll_to_element(el)
                #         # Click enable
                #         el.find_element(By.CSS_SELECTOR, ".product-buttons .enable-all").click()
                #         if str(el.find_element(By.CSS_SELECTOR, ".preview-info .preview-name").text).strip() in ["Standard Print Clothing", "Large Print Clothing"]:
                #             # Click edit
                #             el.find_element(By.CSS_SELECTOR, ".product-buttons .edit-product").click()

                #             # Wait for Scale input range
                #             try:
                #                 scale_el = WebDriverWait(self.chrome_driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".expanded input[type='range']")))
                #                 for i in range(100):
                #                     scale_el.send_keys(Keys.RIGHT)

                #                 # Click Apply Changes Btn
                #                 # Type 1
                #                 try:
                #                     self.chrome_driver.find_element(By.CSS_SELECTOR, ".expanded .buttons button[class='rb-button red apply-changes'][name='button']").click()
                #                 # Type 2
                #                 except Exception as e:
                #                     self.chrome_driver.find_element(By.CSS_SELECTOR, ".expanded button[class='app-entries-uploaderPage-components-ProductOptionsPanel-ProductOptionsPanel_primary_RT_d_ apply-changes']").click()

                #                 sleep(1)
                #             except Exception as e:
                #                 pass

                # Select box
                select = Select(self.chrome_driver.find_element_by_id("work_default_product"))
                select.select_by_visible_text(self.settings['default_product'])

                # Is mature content?
                self.chrome_driver.find_element(By.CSS_SELECTOR, "input#work_safe_for_work_true[value='true']").click()

                # I have the right
                self.chrome_driver.find_element(By.CSS_SELECTOR, "#rightsDeclaration").click()

                sleep(randint(3, 5))

                # Save Work Btn
                self.chrome_driver.find_element(By.CSS_SELECTOR, "#submit-work").click()

                # Wait until Uploading successfully
                for i in range(200):
                    if self.chrome_driver.current_url != "https://www.redbubble.com/portfolio/images/new?ref=account-nav-dropdown":
                        break
                    sleep(1)

                return True

            except Exception as e:
                return False
    # def handle_upload(self, path):
    #     try:
    #         sleep(1)
    #         autoit.win_active("File Upload")
    #         autoit.control_set_text("File Upload", "Edit1", path)
    #         autoit.control_click("File Upload", "Button1")
    #     except Exception as e:
    #         pass
    def scroll_to_element(self, element):
        try:
            action = ActionChains(self.chrome_driver)
            action.move_to_element(element).perform()
        except Exception as e:
            pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Ui()
    sys.exit(app.exec())


       