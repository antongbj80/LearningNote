"""
练习 9.12 多个模块
将User类存储在一个模块中,并将Privileges类和Admin类存储在另一个模块中。再创
建一个文件,在其中创建一个Admin实例并对其调用show_privileges()方法，以确认一切
依然能够正确地运行。
"""

import admin as ad

eric = ad.Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com','alaska')
eric.describe_user()

eric_privileges = ['can reset passwords','can moderate discussions','can suspend accounts',]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()