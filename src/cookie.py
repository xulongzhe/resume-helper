from selenium import webdriver
from time import sleep

def fetch_cookie(user_dir):
    option = webdriver.ChromeOptions()
    option.add_argument('--user-data-dir=/home/xulongzhe/.config/google-chrome-test') 
    option.add_argument(f"--profile-directory={user_dir}");
    option.add_argument("--disable-extensions");
    driver = webdriver.Chrome(options=option)
    driver.get('https://easy.lagou.com/can/new/index.htm?can=true&famousCompany=0&needQueryAmount=true&pageNo=1&pageSize=20&stage=NEW')
    cookie_list=driver.get_cookies()
    driver.quit()
    cookies =";".join([item["name"] +"=" + item["value"] +""  for item in cookie_list])
    return cookies