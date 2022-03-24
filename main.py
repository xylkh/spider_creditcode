import time
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from selenium import webdriver
#进入企查查
from selenium.webdriver import Proxy
from selenium.webdriver.common.proxy import ProxyType

# desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
# proxy.add_to_capabilities(desired_capabilities)
# DRIVER_PATH = 'C:\Program Files (x86)\Google\Chrome\Application'
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\chen\AppData\Local\Google\Chrome\User Data")  # 浏览器路径
# options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'")
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument("--window-size=1920,1080");
# options.add_argument("–disable-gpu")
options.add_argument("blink-settings=imagesEnabled=false")
options.add_argument("--start-maximized")  # 开始最大化
options.add_argument("--test-type")
options.add_argument("--ignore-certificate-errors")  # 忽略证书错误

options.add_argument("--disable-popup-blocking")  # 禁用弹出拦截
options.add_argument("no-sandbox")  # 取消沙盒模式
options.add_argument("no-default-browser-check")  # 禁止默认浏览器检查
options.add_argument("about:histograms")
options.add_argument("about:cache")

options.add_argument("disable-extensions")  # 禁用扩展
options.add_argument("disable-glsl-translator")  # 禁用GLSL翻译

options.add_argument("disable-translate")  # 禁用翻译
options.add_argument("--disable-gpu")  # 谷歌文档提到需要加上这个属性来规避bug
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--hide-scrollbars")  # 隐藏滚动条, 应对一些特殊页面
driver = webdriver.Chrome(options=options)
url = 'https://www.qcc.com/'
driver.get(url)
driver.refresh()
# time.sleep(10)
# driver.find_element_by_id('kw').clear() #定位到搜索框
# print("test~~~~~~~~~~~~~~~~~~~~~~")
#
# driver.find_element_by_id('kw').send_keys("eee") #在搜索框中输入查询企业名单
driver.save_screenshot("test.png")

list_name=["天津大学","清华大学","复旦大学","上海交通大学","华东师范大学"]
for j in list_name:
    driver.find_element_by_id('searchKey').clear() #定位到搜索框

    driver.find_element_by_id('searchKey').send_keys(j) #在搜索框中输入查询企业名单

    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/section[1]/div/div/div/div[1]/div/div/span/button').click()
    except:
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div/div/span/button').click()
    try:
        name = driver.find_elements_by_xpath('//html/body/div/div[2]/div[2]/div[3]/div/div[2]/div/table/tr[1]/td[3]/div/div[1]/span[1]/a/span/em')
        res = ""
        for i in range(len(name)):
            res = res + name[i].text
        if res == j:
            name_id = driver.find_element_by_xpath('//span[contains(text(),"统一社会信用代码")][1]/span/div/span[1]').text
        else:
            name_id = "请手动填写"
    except:
        name_id = "请手动填写"
    print(j,name_id)
driver.quit()
