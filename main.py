from loginLoc import loginLogic
import config


if __name__ == "__main__":
    print("""
chrome                  Tommonkey.cn
   _         _          ___ _ _    
  /_\  _   _| |_ ___   / __\ | | __
 //_\\| | | | __/ _ \ / /  | | |/ /
/  _  \ |_| | || (_) / /___| |   < 
\_/ \_/\__,_|\__\___/\____/|_|_|\_\
                                   
Tommonkey                 Ver:1.0.2
    """)
    if config.debug_model:
        print("[+] 当前调试模式:开启")
    else:
        print("[+] 当前调试模式:关闭")
    # 读取配置
    print("[+] 读取配置中……")
    target = config.target
    getNameXPATH = config.getNameXPATH
    getPasswordXPATH = config.getPasswordXPATH
    error_username = config.error_username
    error_password = config.error_password
    submitXPATH = config.submitXPATH
    usernameList = config.usernameList
    passwordList = config.passwordList
    loginLogic(target,getNameXPATH,getPasswordXPATH,error_username,error_password,submitXPATH,usernameList,passwordList)
