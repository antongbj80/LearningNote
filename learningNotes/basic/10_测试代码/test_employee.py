from employee import Employee

def  test_give_default_raist():
    """测试使用默认的年薪增加量是否可行"""
    eric = Employee('Eric', 'Johnson', 50_000)
    salary = eric.give_raise()
    assert salary == 55_000

def  test_give_custom_raist():
    """测试自定义年薪增加量是否可行"""
    eric = Employee('Eric', 'Johnson', 50_000)
    salary = eric.give_raise(10_000)
    assert salary == 60_000