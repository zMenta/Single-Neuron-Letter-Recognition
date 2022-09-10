from Neuron.Neuron import Neuron
from image_processing import convert_image
import single_neuron_network as network
from data_processing import generate_data

neuron = Neuron(2500)


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
img_px = 50

set_letter_A = generate_data("Data/TrainingData/LetterA/", 1, img_px)
set_letter_B = generate_data("Data/TrainingData/LetterB/", 0, img_px)


training_data = set_letter_A + set_letter_B

# training_set = [
#     [convert_image("Data/TrainingData/LetterA/a.jpg", img_px), 1],
#     [convert_image("Data/TrainingData/LetterB/b.jpg", img_px), 0]
# ]

prediction_letter_A = generate_data("Data/PredictionData/LetterA/", 1, img_px)

# prediction_data = [
#     [convert_image("Data/PredictionData/LetterA/a3.png", img_px)],
# ]


def main():
    network.train_neuron(neuron, training_data)
    print("Neuron Trained")
    network.print_outputs(neuron, training_data)
    print("Predictions")
    network.print_outputs(neuron, prediction_letter_A)


if __name__ == "__main__":
    main()
