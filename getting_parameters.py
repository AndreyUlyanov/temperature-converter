def getting_parameters(input_string):
    scales = ('C', 'F', 'K', 'R', 'De', 'N')

    parameters = input_string.split(' ')

    if len(parameters) != 3:
        raise ValueError('Input string must contain 3 parameters. Please, try again.')

    if parameters[1] not in scales or parameters[2] not in scales:
        raise ValueError('Unknown temperature scale. Please, try again.')

    parameters[0] = float(parameters[0])

    return parameters

