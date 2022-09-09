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

training_set = [
    [convert_image("Data/TrainingData/LetterA/a.jpg", img_px), 1],
    [convert_image("Data/TrainingData/LetterB/b.jpg", img_px), 0]
]


prediction_data = [
    [convert_image("Data/PredictionData/LetterA/a2.png", img_px)],
    [convert_image("Data/PredictionData/LetterA/a3.png", img_px)],
]



def main():
    network.print_outputs(neuron, training_set)
    network.train_neuron(neuron, training_set)
    print("Neuron Trained")
    network.print_outputs(neuron, training_set)
    print("Predictions")
    network.print_outputs(neuron, prediction_data)


if __name__ == "__main__":
    main()
