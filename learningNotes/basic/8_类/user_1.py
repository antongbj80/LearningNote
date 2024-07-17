class User:
    def __init__(self,first_name,last_name,username, email, location):
        """初始化用户信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0 
    
    def describe_user(self):
        """打印用户信息摘要"""
        print(f"\nThe user is {self.first_name} {self.last_name}")
        print(f"Username:{self.username}")
        print(f"Email:{self.email}")
        print(f"Location:{self.location}")
    
    def greet_user(self):
        """用户发出个性化的问候"""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """用来将属性login_attempts的值加1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """用来将属性login_attempts的值重置为0"""
        self.login_attempts = 0