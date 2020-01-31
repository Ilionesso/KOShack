from time import sleep
import re
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from datetime import datetime

LOGIN = "sheikili"
SUBJECT_CODES = ["2336016"]
SLEEP_SECONDS = 1800

PASSWORD = getpass.getpass(prompt='Password: ', stream=None)


chrome_options = Options()
driver = webdriver.Chrome(chrome_options=chrome_options)
while (len(SUBJECT_CODES) > 0):
    driver.get('https://www.kos.cvut.cz/kos/')
    driver.find_element_by_id("userName").send_keys(LOGIN)
    driver.find_element_by_id("password").send_keys(PASSWORD)
    driver.find_element_by_name("vstup").submit()
    driver.execute_script("javascript:window.open('subjectsCode.do?page='+pageCode,'_self')")
    for subject_code in SUBJECT_CODES:
        driver.find_element_by_name("codeSubject").send_keys(subject_code)
        driver.find_element_by_name("Zapsat").click()
        result = driver.find_element_by_class_name("errors").text
        print(f"{datetime.now()} : {result}")
        if re.search("byl", result):
            print(f"{datetime.now()} : Yay! ^_^")
            SUBJECT_CODES.remove(subject_code)
        elif re.search("zapsanych", result):
            SUBJECT_CODES.remove(subject_code)
            print(f"{datetime.now()} : Yay! ^_^")
    if len(SUBJECT_CODES) == 0:
        exit(0)
    else:
        print(f"{datetime.now()} : Remaining codes:{SUBJECT_CODES}")
    sleep(SLEEP_SECONDS)
