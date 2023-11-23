from name_function2 import get_formatted_name

def test_formatting_city_country():
    """Do names like 'Lugo, Spain' work?"""
    formatted_name = get_formatted_name('lugo','spain')
    assert formatted_name == "Lugo, Spain"