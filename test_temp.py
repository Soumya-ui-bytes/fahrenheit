
from temp import celsius_to_fahrenheit

def test_celsius_to_fahrenheit_freezing_point():
    assert round(celsius_to_fahrenheit(0), 2) == 32.00

def test_celsius_to_fahrenheit_boiling_point():
    assert round(celsius_to_fahrenheit(100), 2) == 212.00

def test_celsius_to_fahrenheit_negative_value():
    assert round(celsius_to_fahrenheit(-40), 2) == -40.00