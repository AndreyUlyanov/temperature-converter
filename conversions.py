def to_celsius(value, scale):
    if scale == 'F':
        return (value - 32) * 5 / 9
    elif scale == 'K':
        return value - 273.15
    elif scale == 'R':
        return (value - 491.67) * 5 / 9
    elif scale == 'De':
        return 100 - value * 2 / 3
    elif scale == 'N':
        return value * 100 / 33
    else:
        return value


def from_celsius(value, scale):
    if scale == 'F':
        return value * 9 / 5 + 32
    elif scale == 'K':
        return value + 273.15
    elif scale == 'R':
        return (value + 273.15) * 9 / 5
    elif scale == 'De':
        return (100 - value) * 3 / 2
    elif scale == 'N':
        return value * 33 / 100
    else:
        return value
