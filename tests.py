import converter


def run_test(input_data):
    output = []

    converter.input = lambda: input_data.pop(0)
    converter.print = lambda item: output.append(item)
    converter.main()
    return output


class Tests:
    # comma test
    def test_1(self):
        output = run_test(['35,3 C F', 'exit'])

        assert str(output[0]) == "could not convert string to float: '35,3'"
        assert type(output[0]) == ValueError

    def test_2(self):
        output = run_test(['0 C K', '5 De R', 'exit'])

        assert output[0] == "0.0 C = 273.15 K"
        assert output[1] == "<----->"
        assert output[2] == "5.0 De = 665.67 R"
        assert output[3] == "<----->"

    # unknown temperature scale
    def test_3(self):
        output = run_test(['5 A C', 'exit'])

        assert str(output[0]) == "Unknown temperature scale. Please, try again."
        assert type(output[0]) == ValueError

    # bad temperature value
    def test_4(self):
        output = run_test(['1A C F', 'exit'])

        assert str(output[0]) == "could not convert string to float: '1A'"
        assert type(output[0]) == ValueError

    # similar temperature scales
    def test_5(self):
        output = run_test(['50 De De', 'exit'])

        assert output[0] == "The temperature scales are the same. No conversions required."
        assert output[1] == "<----->"
