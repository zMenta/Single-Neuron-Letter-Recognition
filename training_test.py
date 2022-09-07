from Neuron.Neuron import Neuron


neuron = Neuron(2)

# Inputs
input1 = [1, 1]
input2 = [0, 0]


# Desirable Outputs
output1 = 1
output2 = -1

print(f"Input1 {input1} with desirable output: {output1}")
print(f"Input2 {input2} with desirable output: {output2}")

print("-" * 40)

print(f"Neuron output1 without training: {neuron.add_input(input1)}")
print(f"Neuron output2 without training: {neuron.add_input(input2)}")

print(f"Neuron weight list: {neuron.weight_list}")


# Training area
def adjust_neuron_weight(_neuron: Neuron, input_list: list, obtained_value: float, desirable_value: float) -> None:
    for i in range(_neuron.input_amount):
        _neuron.weight_list[i] = _neuron.weight_list[i] + 1 * (desirable_value -
                                                               obtained_value) * input_list[i]


# Training loop
training_amount = 0
while True:

    training_amount += 1
    need_adjusts = False

    neuron_output1 = neuron.add_input(input1)
    if neuron_output1 != output1:
        adjust_neuron_weight(neuron, input1, neuron.add_input(input1), output1)
        need_adjusts = True

    neuron_output2 = neuron.add_input(input2)
    if neuron_output2 != output2:
        adjust_neuron_weight(neuron, input2, neuron.add_input(input2), output2)
        need_adjusts = True

    if not need_adjusts:
        break

print("-" * 40)
print("Trained")
print(f"Training amount: {training_amount}")
print("-" * 40)


print(f"Neuron output1 : {neuron.add_input(input1)}")
print(f"Neuron output2 : {neuron.add_input(input2)}")
print(f"Neuron weight list: {neuron.weight_list}")
