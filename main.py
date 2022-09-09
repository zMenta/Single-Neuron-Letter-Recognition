from Neuron.Neuron import Neuron
import single_neuron_network as network

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


def main():
    network.print_outputs(neuron, data_set)
    network.train_neuron(neuron, data_set)
    print("Neuron Trained")
    network.print_outputs(neuron, data_set)


if __name__ == "__main__":
    main()
