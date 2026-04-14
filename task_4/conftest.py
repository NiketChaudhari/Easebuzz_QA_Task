# Importing packages
import time
import pytest
from selenium import webdriver
from playwright.sync_api import sync_playwright


# Defining functions
def pytest_addoption(parser):
    parser.addoption("--framework", action="store", default="selenium", help="Please specify the testing framework: 'selenium' or 'playwright'")
    try:
        parser.addoption("--browser", action="store", default="chrome", help="Please specify the browser: 'chrome' or 'firefox' or 'edge'")
    except Exception as e:
        pass
        # print("pytest_addoption error : ",e)
        
@pytest.fixture(autouse=True, scope="session")
def framework_name(request):
    return request.config.getoption("--framework")

@pytest.fixture(autouse=True, scope="session")
def browser_name(request):
    return request.config.getoption("--browser")

@pytest.fixture(autouse=True, scope="function")
def setup_and_teardown(framework_name,
                       browser_name):
    global driver
    time.sleep(1)

    frm_wk_name = str(framework_name).lower().strip()

    if(frm_wk_name =="selenium"):
        if((browser_name=="chrome") or (browser_name=="chromium")):
            driver = webdriver.Chrome()
            driver.maximize_window()
        elif(browser_name=="firefox"):
            driver = webdriver.Firefox()
            driver.maximize_window()
        elif(browser_name=="edge"):
            driver = webdriver.Edge()
            driver.maximize_window()
        else:
            raise ValueError("""Unsupported browser name : {}. Please specify the browser name: 'chrome' or 'firefox' or 'edge'""".format(browser_name))
        yield frm_wk_name, driver
        driver.close()

    elif(frm_wk_name =="playwright"):
        with sync_playwright() as plr:
            if(browser_name=="webkit"):
                browser_ = plr.webkit.launch(headless=False, args=["--start-maximized"])
            elif(browser_name=="chromium"):
                browser_ = plr.chromium.launch(channel="chrome",headless=False, args=["--start-maximized"])
            elif(browser_name=="firefox"):
                browser_ = plr.firefox.launch(headless=False, args=["--start-maximized"])
            elif(browser_name=="edge"):
                browser_ = plr.chromium.launch(channel="msedge",headless=False, args=["--start-maximized"])
            else:
                raise ValueError("""Unsupported browser name : {}. Please specify the browser name: 'webkit' or 'chromium' or 'firefox' or 'edge'""".format(browser_name))
            br_context = browser_.new_context(no_viewport=True)
            br_page = br_context.new_page()
            screen_size = br_page.evaluate("""
                () => {
                    return {
                        'width': window.screen.availWidth,
                        'height': window.screen.availHeight
                    };
                }
            """)
            br_page.set_viewport_size(screen_size)
            yield frm_wk_name, br_page
            br_page.close()
            br_context.close()
            browser_.close()
    else:
        raise ValueError("""Unsupported testing framework name : {}. Please specify the testing framework name: 'selenium' or 'playwright'""".format(framework_name))
