class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        """初始化描述餐馆的属性"""
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """返回格式规范的描述性信息"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")
    
    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业"""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")
    
    def set_number_served(self,number):
        """
        设置就餐人数
        禁止往回调整
        """
        if number >= self.number_served:
            self.number_served = number
            return self.number_served
        else:
            print("You can't roll back the number!")
    
    def increment_number_served(self,number):
        """让就餐人数递增"""
        self.number_served += number
        return self.number_served
    

class IceCreamStand(Restaurant):
    """一个表示冰激凌小店的类"""
    def __init__(self,restaurant_name,cuisine_type='ice cream'):
        """初始化父类的属性"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """显示出售的冰激凌口味"""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")