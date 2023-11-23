from population_function import get_formatted_name

def test_formatting_city_country():
    """Do names like 'Lugo, Spain' work?"""
    formatted_name = get_formatted_name('lugo','spain', 500)
    assert formatted_name == "Lugo, Spain has a population of 500"