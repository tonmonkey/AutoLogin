# Dict
usernameList = ["admin","test"]
passwordList = ["123456","12345678"]

# 目标网站登录URL
target = ""
# 登录页面用户名XPATH路径
getNameXPATH = ''
# 登录页面密码XPATH路径
getPasswordXPATH = ''
# 登录页面提交按钮XPATH路径
submitXPATH = ''
# 登录页面名称值【比如:login.html为login, login.jsp也为login】
login_page_name = "login"
# 是否打开调试模式【True,False】
debug_model = False
# 页面跳转最大等待时间【登录成功后可能时通过页面跳转的方式进入系统，此时跳转需要时间，网速慢或这服务器响应慢会导致跳转时间长，建议观察服务器响应速度自行设置，当前默认等待值为3秒】
maxWait = 5
# 绝对错误账户密码【可保持默认设置】
error_username = "928jhsbxcjduJHABSD"
error_password = "928jhsbxcjduJHABSD"

