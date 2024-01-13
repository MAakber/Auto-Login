from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import subprocess
import configparser
import ctypes
import win32api
import sys
import os

config_file_path = 'setting.cfg'   
exe_file_path = 'msedgedriver.exe'  
config = configparser.ConfigParser(interpolation=None)

def check_and_download_file(filename):   # 检查文件是否存在  
    if os.path.isfile(filename):   
        print(f"{filename} OK") 
    else:   
        result = ctypes.windll.user32.MessageBoxW(0, f"驱动文件 {filename} 不存在，是否安装?\n(选择自动安装需要一定时间)", u"驱动文件丢失",  0x40 | 0x1)  
        if result == 1:  
            subprocess.run(["python", "自动下载Edge浏览器驱动.py", filename])
            result = ctypes.windll.user32.MessageBoxW(0, f"安装成功", u"完成",  0x40 | 0x0)
        else:
            sys.exit()
  
def check_url(url):
    if not url:  
        ctypes.windll.user32.MessageBoxW(0, u"URL为空！请在同目录下的setting.cfg中填写url", u"URL 错误", 0x40 | 0x0)  
        sys.exit()   
    elif not url.startswith("http://") and not url.startswith("https://"):  
        ctypes.windll.user32.MessageBoxW(0, u"无效的 URL：{}\n请检查setting.cfg中的url是否填写正确".format(url), u"URL 错误", 0x10 | 0x0)
        sys.exit()
    else:
        print("URL OK")

def check_buttonID(ID):   
    if not ID:  
        ctypes.windll.user32.MessageBoxW(0, u"按钮的ID不能为空！\n请检查setting.cfg中的check_button是否已经填写。", u"ID 错误", 0x10 | 0x0)  
        sys.exit() 
    else:
        print("ID OK") 

def get_exe_version(file_path):  # 获取exe文件的版本号 
    try:  
        info = win32api.GetFileVersionInfo(file_path, '\\')  
        ms = info['FileVersionMS']  
        ls = info['FileVersionLS']  
        version = "{:d}.{:d}.{:d}.{:d}".format(win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))  
        return version  
    except Exception as e:  
        print(f"An error occurred while getting the exe version: {e}")  
        return None  
    
if not os.path.exists(config_file_path):  #检测环节 
    with open(config_file_path, 'w') as configfile:  
        configfile.write('[DEFAULT]\n')  
        configfile.write('url = \n')  
        configfile.write('check_button = \n') 
        configfile.write('ver = \n')  
check_and_download_file("msedgedriver.exe")

with open(config_file_path, 'r') as configfile:   # 读取文件内容到配置解析器  
    config.read_file(configfile)   
config.read(config_file_path)  
try:  
    expected_version = config['DEFAULT']['ver']  
except KeyError:  
    print("Version not found in the config file.")  
    expected_version = None  
exe_version = get_exe_version(exe_file_path)   
if expected_version and exe_version:  
    if expected_version == exe_version:  
        print("Versions OK")  
    else:  
        print(f"Versions do not match. Expected: {expected_version}, Found: {exe_version}")  
        subprocess.run(["python", "自动下载Edge浏览器驱动.py"])
else:  
    ctypes.windll.user32.MessageBoxW(0, u"出现未知错误，请尝试重装该程序", u"错误",  0x10 | 0x0)
    sys.exit()
url = config.get('DEFAULT', 'url')
check_url(url)
check_button_id = config.get('DEFAULT', 'check_button')
check_buttonID(check_button_id)

user_path = os.environ['USERPROFILE']# 调用edge的用户数据
user_data_path = os.path.join(user_path, 'AppData', 'Local', 'Microsoft', 'Edge', 'User Data')
edge_driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')
edge_options = webdriver.EdgeOptions()
edge_options.add_argument(f'--user-data-dir={user_data_path}')
driver = webdriver.Edge(service=Service(edge_driver_path), options=edge_options)
driver.get(url)
try:  
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, check_button_id)))
    print("Button OK")  
    login_button.click() 
except Exception as e:  
    print(f"An error occurred: {e}")  
finally:  
    driver.quit()
    sys.exit()