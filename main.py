from Neuron.Neuron import Neuron


def main():
    neuron = Neuron(4)

    print(neuron.weight_list)

    neuron.add_input([5, 4, 3, 2])

    print(neuron.add_input([5, 4, 3, 2]))


if __name__ == "__main__":
    main()
