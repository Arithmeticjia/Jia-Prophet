from selenium import webdriver
import time
import threading


def mycsdn():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 设置option,后台运行
    driver = webdriver.Chrome(chrome_options=option)
    # driver = webdriver.Chrome()
    i = 'https://blog.csdn.net/ssjdoudou/article/details/'
    j = ['103318086', '103318039','103318019','103164370','103162927','103148442','103140973','103112194','103111006','102862496','102801033','102704258','102647153','102642141','102549054','102531781','102495060','102469901','102465779','102252523','102146201','102099373','101870927','101722932','101646442','101562745','101557468','101345520','101266623','101230496','101207906','101199757','101174866','101164389','101051865','100916108','100719624','100717106','100694353','100187997','100167777','100069959','100063088','100047810']
    js = 'window.open("https://blog.csdn.net/ssjdoudou");'
    print(len(j))
    driver.execute_script(js)
    for k in range(len(j)):
        print(k)
        s = i + j[k]
        # print('window.open("{url}");'.format(url=s))
        driver.execute_script('window.open("{url}");'.format(url=s))
        time.sleep(1)
    driver.quit()


def mytime():
    while 1:
        mycsdn()
        time.sleep(200)


if __name__ == "__main__":
    t = threading.Thread(target=mytime())
    t.start()