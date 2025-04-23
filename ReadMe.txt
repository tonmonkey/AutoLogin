# AutoLogin
### 工具描述
本工具旨在通过自动化流程模式来模拟正常用户登录操作，其通过无头浏览器的方式进行账户爆破，避免花费大量时间在前端js加解密上浪费时间。

### 使用方法
在运行本工具之前，使用者需要先前往config.py文件下，设置相关参数
+ debug_model：此参数控制工具运行时是否开启调试模式【选填，默认False】
+ target：此参数为网站登陆页面地址URL【必填】
+ getNameXPATH：此参数为网站登录框中用户名所处XPATH路径【必填】
+ getPasswordXPATH：此参数为网站登录框中密码所处XPATH路径【必填】
+ submitXPATH：此参数为网站登录框中提交按钮所处XPATH路径【路径】
+ maxWait：页面跳转最大等待时间【选填】
+ login_page_name：此参数设置登录页面名称值，列如login.html为login, login.jsp也为login【必填】
参数填写完毕后，安装selenium包即可运行，运行完毕后登录成功的结果会在当前目录的result.txt中
```
pip install selenium
python main.py
```

