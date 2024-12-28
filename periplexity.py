# Import necessary packages
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pathlib

warnings.simplefilter("ignore")
url = "https://www.perplexity.ai/"
chrome_driver_path = 'DataBase\\chromedriver.exe'
chrome_options = Options()
#chrome_options.add_argument("--headless=new")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(50)


driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/textarea").send_keys("who was shivaji maharaj?")
sleep(1)
driver.find_element(by=By.XPATH,value='//*[@id="__next"]/main/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]/button[2]').click()
input("")

