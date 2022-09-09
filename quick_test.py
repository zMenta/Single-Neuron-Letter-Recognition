from Neuron.Neuron import Neuron

neuron = Neuron(2)


# Testing Data
input1 = [1, 1]
input2 = [1, 0]
input3 = [0, 1]
input4 = [0, 0]

# [Input list, desired output]
data_set = [
    [input1, 1],
    [input2, 1],
    [input3, 0],
    [input4, 0],
]

neuron.weight_list = [0, 0]


def test_outputs():
    for input_set in data_set:
        print(neuron.return_output(input_set[0]))


def weight_adjustment(_neuron: Neuron, input_list: list, obtained_value, desirable_value):
    for i in range(_neuron.input_amount):
        _neuron.weight_list[i] += 1 * \
            (desirable_value - obtained_value) * input_list[i]


def train_neuron():
    need_adjust = True
    while need_adjust:
        need_adjust = False

        for data in data_set:
            desired_output = data[1]
            output = neuron.return_output(data[0])
            # data[1] = desired output of the specific data set.
            if output != desired_output:
                weight_adjustment(neuron, data[0], output, desired_output)
                need_adjust = True


def main():
    test_outputs()
    train_neuron()
    print("Neuron Trained")
    test_outputs()


if __name__ == "__main__":
    main()
