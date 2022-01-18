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
                #Standard Print Clothing
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[1]/div[1]/div[4]/div[2]/div[1]").click()
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[2]/div[2]/div[4]/div/div[1]/div/fieldset/div[2]/div[3]/label[5]").click()
                slider = self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[2]/div[2]/div[4]/div/div[1]/div/fieldset/div[3]/div[1]/input")
                ActionChains(self.chrome_driver).drag_and_drop_by_offset(slider, 100, 0).perform()
                #Big print clothing
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[1]/div[2]/div[4]/div[2]/div[1]").click()
                self.chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[4]/div/div[2]/div[4]/div/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[2]/label/span/svg").click()
                
                #Caps
                # Chiffon Tops
                # T-shirt dresses
                # Graphic Tees
                # A-line dresses
                # Stickers and magnets
                # Phone Cases & Skins
                # XXL mouse pad
                # Mousepad
                # Cushions and tote bags
                # Prints, cards and posters
                # Pouches, Skins & Laptop Sleeves
                # Duvet covers, bedspreads and shower curtains
                # mugs
                # Thermo mugs
                # Mini skirts
                # Scarves
                # Tablet Cases & Skins
                # Drawstring Bags
                # Spiral Notebooks
                # Hardcover Journals
                # Clocks
                # Art Board Prints
                # acrylic blocks and coasters
                # Plaids and drapes
                # Bath mat
                # Gourds
                # Canvas and wood mounted prints
                # Classic tote bags
                # Badges
                # Masks
                # Aprons
                # Puzzles
                # Double tops
                # Floor cushions
                # Wallet cases
                # leggings
                # Socks
                # Backpack
                # Sports bags
                # Fitted masks
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


       