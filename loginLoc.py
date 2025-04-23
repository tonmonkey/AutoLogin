from selenium import webdriver
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import login_page_name, debug_model, maxWait

# 获取登录失败响应各项参数基准
def loginError(target,getNameXPATH,getPasswordXPATH,error_username,error_password,submitXPATH,driver):
    try:
        driver.get(target)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, getPasswordXPATH)))
        # 找到用户名和密码输入框并输入内容
        username = driver.find_element(By.XPATH, getNameXPATH)
        password = driver.find_element(By.XPATH, getPasswordXPATH)
        # 错误标本对照，先发送一个绝对错误的登录账户，保存返回内容，与后面需要测试的账户密码进行对比，不一致则说明测试账户密码登录成功，反之
        if debug_model:
            print("[+] 绝对错误基准账户:"+error_username,error_password)
        username.send_keys(error_username)
        password.send_keys(error_password)
        login_button = driver.find_element(By.XPATH, submitXPATH)
        login_button.click()
        # 登录失败后响应页面大小
        error_page_text_len = len(driver.page_source)
        if debug_model:
            print("[+] 登录失败页面大小: "+str(error_page_text_len))
        # 登录失败后跳转的路径
        error_url = driver.current_url
        if debug_model:
            print("[+] 登录失败页面路径: "+error_url)
        return error_page_text_len,error_url
    except Exception as err:
        print("[+] 异常运行错误！{}".format(err))

# 登录测试模块
def loginLogic(target,getNameXPATH,getPasswordXPATH,error_username,error_password,submitXPATH,usernameList,passwordList,):
    global status, right_username, right_password
    chrome_options = Options()
    if debug_model is False:
        chrome_options.add_argument('--headless')  # 启用无头模式
    chrome_options.add_argument("--incognito")   # 无痕模式
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        '''})
    try:
        driver.get(target)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, getNameXPATH)))
        # 找到用户名和密码输入框并输入内容
        username = driver.find_element(By.XPATH, getNameXPATH)
        password = driver.find_element(By.XPATH, getPasswordXPATH)
        # 测试
        error_page_text_len, error_url = loginError(target, getNameXPATH, getPasswordXPATH, error_username, error_password,submitXPATH,driver)
        for un in usernameList:
            username.clear()
            username.send_keys(un)
            for pw in passwordList:
                password.clear()
                password.send_keys(pw)
                print("***************************\n[+] 当前测试用户名与密码:" + un, pw)
                # 找到登录按钮并点击
                login_button = driver.find_element(By.XPATH, submitXPATH)
                if debug_model:
                    print("[+] 当前页面登录按钮XPATH路径:"+submitXPATH)
                login_button.click()
                if debug_model:
                    print("[+] 当前页面最大等待时间:"+str(maxWait)+"秒/s")
                try:
                    WebDriverWait(driver, maxWait).until_not(EC.url_contains(login_page_name))
                except TimeoutException:
                    pass
                page_text = driver.page_source
                current_url = driver.current_url
                page_text_len = len(page_text)
                if debug_model:
                    print("[+] 当前测试登录页面大小:"+ str(page_text_len))
                    print("[+] 当前测试登录页面路径:" + str(current_url))
                if debug_model:
                    if error_url == current_url:
                        print("[+] 绝对登录失败页面路径与测试登录路径: 相同-失败")
                    else:
                        # 成功结果输出模块
                        print("\033[5;31;44m【+】\033[0m 绝对登录失败页面路径与测试登录路径: 不相同-成功")
                        print("***************************\n[+] 登录成功！\n[+] 用户名:{}\n[+] 密码:{}\n***************************".format(un,pw))
                        with open(r"./result.txt","a+",encoding='utf-8') as w:
                            w.write("\ntarget:{}\nusername:{}\npassword:{}\n".format(target,un,pw))
                        break
                else:
                    continue
        driver.quit()
    except StaleElementReferenceException:
        pass
    except Exception as err:
        print("[+] 异常运行错误！{}".format(err))