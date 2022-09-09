from Neuron.Neuron import Neuron
from image_processing import convert_image
import single_neuron_network as network

neuron = Neuron(400)


#  Testing Data
# input1 = [1, 1]
# input2 = [1, 0]
# input3 = [0, 1]
# input4 = [0, 0]

#   [Input list, desired output]
# data_set = [
#     [input1, 1],
#     [input2, 1],
#     [input3, 0],
#     [input4, 0],
# ]


# Image testing

# Downscale value
img_px = 20

data_set = [
    [convert_image("TrainingData/LetterA/a.jpg", img_px), 1],
    [convert_image("TrainingData/LetterB/b.jpg", img_px), 0]
]


def main():
    network.print_outputs(neuron, data_set)
    network.train_neuron(neuron, data_set)
    print("Neuron Trained")
    network.print_outputs(neuron, data_set)


if __name__ == "__main__":
    main()
