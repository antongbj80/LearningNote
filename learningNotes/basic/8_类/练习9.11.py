"""
练习 9.11 导入 Admin 类  
以为完成练习9.8而做的工作为基础。将User类、Privileges类和Admin类存储在一个模块中,
再创建一个文件,在其中创建一个Admin实例并对其调用show_privileges()方法，以确认一切都能正确地运行。
"""

from user import *

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric_privileges = ['can reset passwords','can moderate discussions','can suspend accounts',]
eric.privileges.privileges = eric_privileges
print(f"\nThe admin {eric.username} has these privileges: ")
eric.privileges.show_privileges()