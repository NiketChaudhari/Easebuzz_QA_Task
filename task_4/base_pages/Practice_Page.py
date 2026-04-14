# Importing packages
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



# Base Class
class Practice_Page:
    radio_btn_xpath_1 = "//label[contains(normalize-space(), '" 
    radio_btn_xpath_2 = "')]/input"
    suggession_dropdown_xpath = "//input[@placeholder='Type to Select Countries']"
    suggession_dropdown_list_xpath = "(//li[@class='ui-menu-item'])/div"
    option_dropdown_id = "dropdown-class-example"


    def __init__(self, arg_framework_name, arg_driver):
        self.framework_name = arg_framework_name
        self.driver = arg_driver
        time.sleep(1)


    def get_current_url_value(self):
        if(self.framework_name=="selenium"):
            time.sleep(1)
            return self.driver.current_url
        else:
            self.driver.wait_for_timeout(1000)
            return self.driver.url
   

    def get_current_title_value(self):
        if(self.framework_name=="selenium"):
            time.sleep(1)
            return self.driver.title
        else:
            self.driver.wait_for_timeout(1000)
            return self.driver.title()


    def select_radio_button(self, arg_radio_text):
        path = self.radio_btn_xpath_1 + str(arg_radio_text).strip() + self.radio_btn_xpath_2
        if(self.framework_name=="selenium"):
            ele = self.driver.find_element(By.XPATH, path)
            ele.click()
            time.sleep(1)
            return ele.is_selected()
        else:
            ele = self.driver.locator("{}".format(path))
            ele.click()
            self.driver.wait_for_timeout(1000)
            return ele.is_checked()


    def select_suggession_dropdown(self, arg_country_text):
        if(self.framework_name=="selenium"):
            ele = self.driver.find_element(By.XPATH, self.suggession_dropdown_xpath)
            ele.send_keys(arg_country_text)
            time.sleep(1)
            eles = self.driver.find_elements(By.XPATH, self.suggession_dropdown_list_xpath)
            for itm in eles:
                if(str(itm.text).lower()==str(arg_country_text).lower()):
                    parent_li = itm.find_element(By.XPATH, "..")
                    time.sleep(1)
                    parent_li.click()
                    time.sleep(2)
                    break            
        else:
            ele = self.driver.locator("{}".format(self.suggession_dropdown_xpath))
            ele.fill(arg_country_text)
            self.driver.wait_for_timeout(1000)
            eles = self.driver.locator("{}".format(self.suggession_dropdown_list_xpath)).all()
            for itm in eles:
                if(str(itm.text_content()).lower()==str(arg_country_text).lower()):
                    parent_li = itm.locator("..")
                    self.driver.wait_for_timeout(1000)
                    parent_li.click()
                    self.driver.wait_for_timeout(2000)
                    break
        

    def select_option_dropdown(self, arg_option_text):
        if(self.framework_name=="selenium"):
            ele = self.driver.find_element(By.ID, self.option_dropdown_id)
            select = Select(ele)
            time.sleep(2)
            select.select_by_visible_text(arg_option_text)
            time.sleep(2)
        else:
            ele = self.driver.locator("#{}".format(self.option_dropdown_id))
            self.driver.wait_for_timeout(2000)
            ele.select_option(label=arg_option_text)
            self.driver.wait_for_timeout(2000)











