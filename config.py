# Dict
usernameList = ["111","admin","test"]
passwordList = ["123456","7CUW3P82*iQIxHXWq8","admin124"]

# 目标网站参数
target = "https://39.106.224.19:5000/#/login?redirect=/index"
# 登录页面用户名id标签
getNameId = "custom-validation_username"
# 登录页面密码id标签
getPasswordId = "custom-validation_password"
# 登录页面提交按钮XPATH路径
submitXPATH = '//*[@id="userLayout"]/div/div/div[2]/form/div[2]/div/div/div/div/button/span'
# 登录页面名称值【比如:login.html为login, login.jsp也为login】
login_page_name = "login"

# 登录错误页面大小与登录成功页面大小差值【建议此项默认，除非特殊网站，登录错误和登录成功页面大小相差很小，可修改此值以提高精度】
minValue = -3000
maxValue = 3000
# 绝对错误账户密码【可保持默认设置】
error_username = "928jhsbxcjduJHABSD"
error_password = "928jhsbxcjduJHABSD"
# 是否打开调试模式【True,False】
debug_model = False
# 页面跳转最大等待时间【登录成功后可能时通过页面跳转的方式进入系统，此时跳转需要时间，网速慢或这服务器响应慢会导致跳转时间长，建议观察服务器响应速度自行设置，当前默认等待值为3秒】
maxWait = 5
# 数据定位填充方式，这里写了两种方式来实现定位页面输入框的用户名，密码与提交等。第一个方式是通过ID标签实现定位，第二个是通过xpath路径的方式。根据网站具体情况选择
# position_way = "xpath"
position_way = "id"     # 未完成

