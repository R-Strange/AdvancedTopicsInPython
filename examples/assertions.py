def decrease_parameter(parameter, decrease_percentage):
    new_parameter_value = parameter["value"] * (1 - decrease_percentage)

    assert 0 <= new_parameter_value <= 1

    return new_parameter_value

