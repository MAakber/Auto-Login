import os
import shutil
import configparser  
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

config = configparser.ConfigParser()  
config.read('setting.cfg')
script_dir = os.path.dirname(os.path.realpath(__file__))
driver_path = EdgeChromiumDriverManager().install()
driver = webdriver.Edge(service=Service(driver_path))
print(driver.capabilities['browserVersion'])# 打印浏览器版本
browser_version = str(driver.capabilities.get('browserVersion')) 
config['DEFAULT']['ver'] = browser_version     
with open('setting.cfg', 'w') as configfile:  
    config.write(configfile)  
driver.quit()
new_driver_path = os.path.join(script_dir, os.path.basename(driver_path))
if os.path.exists(new_driver_path):
    os.remove(new_driver_path)
shutil.move(driver_path, new_driver_path)