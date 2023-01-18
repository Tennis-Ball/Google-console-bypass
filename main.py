from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(desired_capabilities=d, options=chrome_options)

driver.get("https://dashboard.outlier.org")
url = "https://dashboard.outlier.org"

while True:
    for entry in driver.get_log('browser'):
        if entry["level"] == "INFO":
            print(entry["message"])
            print()
    # if driver.current_url != url:
    #     print(f"_______________________________________________{driver.current_url}__")
    #     url =  driver.current_url
