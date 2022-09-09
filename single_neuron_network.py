from Neuron.Neuron import Neuron


def print_outputs(_neuron: Neuron, _data_set: list):
    """Prints the outputs of a certain training data_set

    Args:
        _data_set (list): List containing [ [input_list1, desired_output2] ... [input_listN, desired_outputN] ]
    """
    for input_set in _data_set:
        print(_neuron.return_output(input_set[0]))


def weight_adjustment(_neuron: Neuron, input_list: list, obtained_value, desirable_value):
    """Adjust the neuron weights to meet the desired output.

    Args:
        _neuron (Neuron): Neuron to be trained.
        input_list (list): Input data that is used to train.
        obtained_value (_type_): Obtained value from the input_list.
        desirable_value (_type_): Desired value to be returned with input_list.
    """
    for i in range(_neuron.input_amount):
        _neuron.weight_list[i] += 1 * \
            (desirable_value - obtained_value) * input_list[i]


def train_neuron(_neuron: Neuron, _data_set: list):
    """Train the neuron to the desired output.

    Args:
        _neuron (Neuron): Neuron that will be trained
        _data_set (List): List containing [ [input_list1, desired_output2] ... [input_listN, desired_outputN] ]
    """
    need_adjust = True
    while need_adjust:
        need_adjust = False

        for data in _data_set:
            desired_output = data[1]
            output = _neuron.return_output(data[0])
            # data[1] = desired output of the specific data set.
            if output != desired_output:
                weight_adjustment(_neuron, data[0], output, desired_output)
                need_adjust = True
