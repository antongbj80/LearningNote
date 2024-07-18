"""一系列处理城市的函数"""

def city_country(city, country):
 """返回一个形如'Santiago, Chile'的字符串"""
 return f"{city.title()}, {country.title()}"


def city_country_population(city,country,population=0):
    if population == 0:
        """返回一个形如'Santiago, Chile'的字符串"""
        return f"{city.title()}, {country.title()}"
    else:
        """返回一个形如'Santiago, Chile population - 5000000'的字符串"""
        return f"{city.title()}, {country.title()} population - {population}"


