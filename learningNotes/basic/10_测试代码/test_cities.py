from city_functions import city_country
from city_functions import city_country_population

def test_city_country():
    """传入简单的城市和国家可行吗？"""
    city_country_name = city_country('santiago','chile')
    assert city_country_name == 'Santiago, Chile'

def test_city_country_population():
    city_country_population_test = city_country_population('santiago','chile',population=5000000)
    assert city_country_population_test == 'Santiago, Chile population - 5000000'