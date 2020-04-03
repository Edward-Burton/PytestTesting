import sys
import unittest

import allure
import pytest

# sys.path.append("..")
import yaml
from python.calc import Calc
# print(sys.path)

@allure.feature("加法模块")
class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calc()
    @allure.story("整数计算器加法")
    def test_add(self):
        self.assertEqual(3, self.calc.add(1, 2))
    @allure.story("小数计算器加法")
    def test_add_2(self):
        self.assertEqual(0.03, self.calc.add(0.02, 0.01))


def test_data():
    with open("calc_data.yaml") as f:
        f = yaml.load(f)
        #print(f)
        return  f

def test_step():
    with open("calc_step_data.yaml") as f:
        f = yaml.load(f)
        return f


@allure.feature("计算器模块")
class TestCalcu():
    with open("calc_data.yaml") as f:
        data = yaml.load(f)
    with open("calc_step_data.yaml") as f:
        step_data = yaml.load(f)

    @classmethod
    def setup_class(cls):
        cls.calc=Calc()
        # with open("calc_data.yaml") as f:
        #     cls.data=yaml.load(f)
        print("classmethod")

    def setup(self):
        self.calc = Calc()
        print("setup")

    @pytest.fixture(autouse=True,scope="class")
    def open_calcu(self):
        print("打开计算器")
        yield
        print("关闭计算器")

    @allure.testcase("https://github.com/twoknowapes/AutoTest","加法测试用例")
    @allure.story("整数加法")
    @pytest.mark.usefixtures("open_calcu")
    def test_add(self):
        print("add testcase")
        assert 3 == TestCalcu.calc.add(1, 2)


    @allure.link("http://www.baidu.com",name="百度链接")
    @allure.story("元组分解传参")
    @pytest.mark.usefixtures("open_calcu")
    def test_add_tuple(self):
        print("add_tuple")
        with allure.step("设置元组"):
            a = 2,5
        with allure.step("传参判断"):
            assert 3 == self.calc.add(*a)



    @allure.issue("1056","这是一个issue")
    #在运行时加上访问地址，这里的第一个参数传bug的编号
    #--allure-link-pattern=issue:https://home.testing-studio.com/t/topic/{}
    @allure.story("整数减法")
    @pytest.mark.usefixtures("open_calcu")
    def test_sub(self):
        print("subtraction testcase")
        assert 4 == 764 - 34

    f=[(4,2),(5,1),(37,7),(25,5),(7,0)]
    @pytest.mark.usefixtures("open_calcu")
    @pytest.mark.parametrize("a,b,r",data)
    def test_div(self,a,b,r):
        #self.test_calcscene(a,b,r)
        if(b==0):
            with pytest.raises(ZeroDivisionError):
                self.calc.div(a,b)
        assert r == round(self.calc.div(a,b))


    def test_calcscene(self,a,b,r):
        for step in self.step_data:
            print(step)
            if step == "add":
                assert self.calc.add(a,b) == r
                #pytest.assume(self.calc.add(a,b) == r)
            elif step =="div":
                assert self.calc.div(a,b) == r
                #pytest.assume(self.calc.div(a,b) == r)



   # def test_mul(self,):
# if __name__ == "__main__":
#     unittest.main()
if __name__ == '__main__':
    #pytest.main()
    pytest.main(['-v','-s','test_calc.py::TestCalcu::test_div'])
    #pytest.main("-v -s test_calc.py::TestCalcu::test_sub")
