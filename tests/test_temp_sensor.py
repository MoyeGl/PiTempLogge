from src import temp_sensor

def test_temp_within_range():
    temp = temp_sensor.read_temperature_c()
    assert 20.0 <= temp <= 30.0
