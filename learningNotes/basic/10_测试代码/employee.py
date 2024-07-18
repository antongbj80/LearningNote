class Employee:
    """一个表示雇员的类"""

    def __init__(self,firt_name,last_name,annual_salary):
        """初始化雇员"""
        self.first_name = firt_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self,percent=5000):
        """给雇员加薪"""
        self.annual_salary +=  percent
        return self.annual_salary

