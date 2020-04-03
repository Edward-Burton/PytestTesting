import yaml
from appium.webdriver.webdriver import WebDriver
#安装 Appium-Python-Client

class BasePage:

    #定义弹出黑名单
    _black_list=[]

    #处理死循环的问题
    _error_cont=0
    _error_max=10

    #使用字典，该字典中的key存yaml中的需要命中字典中value属性的值，该字典中的value是命中属性后需要替换的值
    _params={}

    def __init__(self,driver:WebDriver):
        self._driver=driver

    def find(self,by,locator=None):
        try:
            element = self._driver.find_element(*by) if isinstance(by,tuple) else self._driver.find_element(by,locator)
            self._error_cont=0
            return element
        except Exception as e:
        #处理页面弹出问题，所以弹出是一个异常？
            self._error_cont+=1
            if self._error_cont>=self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_element(*black)
                if len(elements)>0:
                    elements[0].click()
                    return self.find(by,locator)
            raise e

    def steps(self,path):
        with open(path,encoding="utf-8") as f:
            steps:list[dict] = yaml.safe_load(f)
            for step in steps:
                if"by" in step.keys():
                    element = self.find(step["by"],step["locator"])
                if "action" in step.keys():
                    if "click" ==step["aciton"]:
                        element.click()
                    if "send" ==step["action"]:
                        content:str = step["value"]
                        for param in self._params:
                            #该字典中的key存yaml中的需要命中字典中value属性的值，该字典中的value是命中属性后需要替换的值
                            #对文件中的数据进行一次再加工
                            content=content.replace("{%s}"%param,self._params[param])
                        element.send_keys(content)
