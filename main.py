from conversions import to_celsius, from_celsius
from getting_parameters import getting_parameters

s = input()

while s != 'exit':
    try:
        value, from_scale, to_scale = getting_parameters(s)
        if from_scale == to_scale:
            print('The temperature scales are the same. No conversions required.')
        else:
            value_in_new_scale = from_celsius(to_celsius(value, from_scale), to_scale)
            print(f"{value} {from_scale} = {value_in_new_scale} {to_scale}")
        print('<----->')
    except ValueError as e:
        print(e)

    s = input()
