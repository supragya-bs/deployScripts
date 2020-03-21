from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import re

#Constants
TIMEOUT = 20

def google_get_new_backup_codes(driver, uname, pwd): #TODO
    driver.get("https://myaccount.google.com/signinoptions/two-step-verification")
    google_login_2fa_phone(driver, uname+"@browserstack.com", pwd)
    # driver.get("https://myaccount.google.com/")
    # driver.find_elements_by_class_name("WpHeLc")[0].click()
    # google_login_2fa_phone(driver, uname+"@browserstack.com", pwd)
    # WebDriverWait(driver, TIMEOUT).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "GWwaOc"))
    # )
    # driver.get("https://myaccount.google.com/security")
    # driver.find_element_by_link_text("2-Step Verification").click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.LINK_TEXT, "SHOW CODES"))
    )
    driver.find_element_by_link_text("SHOW CODES").click()


def google_login_put_username(driver, uname):
    driver.find_element_by_id("identifierId").send_keys(uname)
    driver.find_element_by_id("identifierNext").click()

def google_login_put_password(driver, pwd):
    driver.find_element_by_name("password").send_keys(pwd)
    driver.find_element_by_id("passwordNext").click()

def google_enter_backup_code(driver, code):
    driver.find_element_by_xpath("//*[contains(text(),'Enter one of your 8-digit backup codes')]").click()
    time.sleep(2)
    driver.find_element_by_name("backupCodePin").send_keys(bkp)
    driver.find_element_by_name("backupCodePin").send_keys(Keys.ENTER)    

def google_login_2fa_phone(driver, uname, pwd):
    time.sleep(2)
    google_login_put_username(driver, uname)
    while True:
        time.sleep(2)
        google_login_put_password(driver, pwd)
        if re.search(r'Too many failed attempts', driver.page_source):
            print("Required a Backup code!!")
            google_enter_backup_code(driver, input())
        elif re.search(r'Something went wrong', driver.page_source):
            print("Retrying two step verification")
            driver.find_element_by_xpath("//*[contains(text(),'Try another way')]").click()
            print("Required a Backup code!!")
            google_enter_backup_code(driver, input())

def from_sl_run_query(driver, query, uname, pwd):
    driver.get("https://zombie.browserstack.com/admin/sl_run_query?method=post")
    driver.find_element_by_link_text("Sign in").click()
    google_login_2fa_phone(driver, uname, pwd)
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "q"))
    )
    driver.find_element_by_name("q").send_keys(query)
    driver.find_element_by_name("commit").click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-row"))
    )
    soln = driver.find_elements_by_class_name("alert-row")
    reply = []
    for s in soln:
        reply.append(s.text)
        print(s.text)

def from_sl_run_query2(driver, query, uname, pwd):
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.ID, "q"))
    )
    driver.find_element_by_name("q").clear()
    driver.find_element_by_name("q").send_keys(query)
    driver.find_element_by_name("commit").click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-row"))
    )
    soln = driver.find_elements_by_class_name("alert-row")
    reply = []
    for s in soln:
        reply.append(s.text)
        print(s.text)
if __name__ == "__main__":
    driver = webdriver.Remote(command_executor="http://127.0.0.1:62182",desired_capabilities={})
    driver.session_id = "96e556873c419d9997406fe59c45b5e8"
    # driver = webdriver.Chrome()
    # url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
    # session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'
    # print(url)
    # print(session_id)
    time.sleep(5)
    # google_get_new_backup_codes(driver, "supragya", "Wliaom?dy1122")
    ans = from_sl_run_query2(driver, "SELECT name FROM terminals where state='available' and os='macmav'", "supragya", "Wliaom?dy1122")
    driver.close()
