from Neuron.Neuron import Neuron
from image_processing import convert_image
import single_neuron_network as network
from data_processing import generate_data

neuron = Neuron(1296)


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
img_px = 36

set_letter_A = generate_data("Data/TrainingData/LetterA/", 1, img_px)
set_letter_B = generate_data("Data/TrainingData/LetterB/", 0, img_px)


training_data = set_letter_A + set_letter_B

prediction_letter_A = generate_data("Data/PredictionData/LetterA/", 1, img_px)
prediction_letter_B = generate_data("Data/PredictionData/LetterB/", 0, img_px)


def main():
    network.train_neuron(neuron, training_data)
    print("Neuron Trained")
    # network.print_outputs(neuron, training_data)
    print("Predictions")
    print("-Letter A = 1")
    network.print_outputs(neuron, prediction_letter_A)
    print("-Letter B == 0")
    network.print_outputs(neuron, prediction_letter_B)


if __name__ == "__main__":
    main()
