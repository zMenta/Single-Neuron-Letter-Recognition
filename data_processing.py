import os

data_path = "Data/TrainingData/LetterA"

for file in os.listdir(data_path):
    # file is str
    print(file)
