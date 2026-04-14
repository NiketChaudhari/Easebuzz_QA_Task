# Importing packages
import pytest
from base_pages.Practice_Page import Practice_Page


# Test Class
class Test_Practice_Page:
    page_url = "https://rahulshettyacademy.com/AutomationPractice/"
    page_title = "Practice Page"
    radio_btn_text = "Radio2"
    country_text = "indian"
    option_text = "Option2"
    

    def test_validate_page_url(self, setup_and_teardown):
        self.frm_wk_name, self.driver = setup_and_teardown

        if(self.frm_wk_name=="selenium"):
            self.driver.get(self.page_url)
        else:
            self.driver.goto(self.page_url)

        self.page_obj = Practice_Page(self.frm_wk_name, self.driver)
        actual_value = self.page_obj.get_current_url_value()
        expected_value = self.page_url
        print("Actual URL : ",actual_value)
        print("Expected URL : ",expected_value)
        assert (actual_value == expected_value), "Page URL mismatch."


    def test_validate_page_title(self, setup_and_teardown):
        self.frm_wk_name, self.driver = setup_and_teardown

        if(self.frm_wk_name=="selenium"):
            self.driver.get(self.page_url)
        else:
            self.driver.goto(self.page_url)

        self.page_obj = Practice_Page(self.frm_wk_name, self.driver)
        actual_value = self.page_obj.get_current_title_value()
        expected_value = self.page_title
        print("Actual URL : ",actual_value)
        print("Expected URL : ",expected_value)
        assert (actual_value == expected_value), "Page Title mismatch."


    def test_select_radio_button(self, setup_and_teardown):
        self.frm_wk_name, self.driver = setup_and_teardown

        if(self.frm_wk_name=="selenium"):
            self.driver.get(self.page_url)
        else:
            self.driver.goto(self.page_url)

        self.page_obj = Practice_Page(self.frm_wk_name, self.driver)
        radio_select_flag = self.page_obj.select_radio_button(arg_radio_text=self.radio_btn_text)
        assert radio_select_flag, "Radio button {} is not selected.".format(self.radio_btn_text)



    def test_select_country_dropdown(self, setup_and_teardown):
        self.frm_wk_name, self.driver = setup_and_teardown

        if(self.frm_wk_name=="selenium"):
            self.driver.get(self.page_url)
        else:
            self.driver.goto(self.page_url)

        self.page_obj = Practice_Page(self.frm_wk_name, self.driver)
        self.page_obj.select_suggession_dropdown(arg_country_text=self.country_text)



    def test_select_option_dropdown(self, setup_and_teardown):
        self.frm_wk_name, self.driver = setup_and_teardown

        if(self.frm_wk_name=="selenium"):
            self.driver.get(self.page_url)
        else:
            self.driver.goto(self.page_url)

        self.page_obj = Practice_Page(self.frm_wk_name, self.driver)
        self.page_obj.select_option_dropdown(arg_option_text=self.option_text)
