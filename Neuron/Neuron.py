import Neuron.sum_functions as sf


class Neuron:
    def __init__(self, input_amount: int = 1, function_type: int = 0) -> None:
        self.input_amount = input_amount
        self.function_type = function_type

        if input_amount <= 0:
            self.input_amount = 1

        self.weight_list = [0] * input_amount

    def add_input(self, input_list: list) -> float:
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
                "Input_list length is not the same as weight_list length")

        _input_sum: float = 0
        for i in range(len(self.weight_list)):
            _input_sum += self.weight_list[i] * input_list[i]

        if self.function_type == 0:
            return sf.fastLimit(_input_sum)
        elif self.function_type == 1:
            return sf.rampFunction(_input_sum)
        elif self.function_type == 2:
            return sf.sigmoidFunction(_input_sum)

        raise Exception("Invalid function_type value")

    # NEED to think about how to train the AI in a better structured and flexible way
    # Create another class called network and have a network.train() method?

    # def train(self, input_list: list, desirable_value: float) -> None:
        # """Train the neuron to return desirable_value
#
        # Args:
        # input_list (list): List containing the inputs to the neuron.
        # desirable_value (float): Desirable value that you want to train the neuron to return on add_input().
        # """
#
        # obtained_value = self.add_input(input_list)
#
        # for i in range(self.input_amount):
        # self.weight_list[i] = self.weight_list[i] + 1 * (desirable_value -
        #  obtained_value) * input_list[i]
#
        # need_adjusts = True
        # while need_adjusts:
        # need_adjusts = False
        #
        #
