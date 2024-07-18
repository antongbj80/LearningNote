import pytest
from employee import Employee

@pytest.fixture  #夹具
def employee():
    """创建一个可供所有测试函数使用的 Employee 对象"""
    employee = Employee('Eric','Jonson',50_000)
    return employee

def  test_give_default_raist(employee):
    """测试使用默认的年薪增加量是否可行"""
    salary = employee.give_raise()
    assert salary == 55_000

def  test_give_custom_raist(employee):
    """测试自定义年薪增加量是否可行"""
    salary = employee.give_raise(10_000)
    assert salary == 60_000