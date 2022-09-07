from logging import raiseExceptions
import Neuron.sum_functions as sf


class Neuron:
    def __init__(self, input_amount: int = 1) -> None:
        self.input_amount = input_amount

        if input_amount <= 0:
            self.input_amount = 1

        self.weight_list = [0] * input_amount

    def add_input(self, input_list: list, function_type: int = 0) -> float:
        """Add inputs to the neuron.

        Args:
            input_list (list): List of inputs. Must be the same size of the weight_list or input_amount
            function_type (int, optional): Select sum function to be used. Defaults to 0.

        Returns:
            float: Calculated value
        """

        if type(input_list) != list:
            raise Exception("Input_list is not a list")

        if len(input_list) != len(self.weight_list):
            raise Exception(
                "Input_list lenght is not the same as weight_list lenght")

        _input_sum: float = 0
        for i in range(len(self.weight_list)):
            _input_sum += self.weight_list[i] * input_list[i]

        if function_type == 0:
            return sf.fastLimit(_input_sum)
        elif function_type == 1:
            return sf.rampFunction(_input_sum)
        elif function_type == 2:
            return sf.sigmoidFunction(_input_sum)

        raise Exception("Invalid function_type value")
