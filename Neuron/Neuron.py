
class Neuron():
    def __init__(self, input_amount: int = 1, bias: float = 0) -> None:
        """
        Args:
            input_amount (int): Amount of inputs that the neuron can receive. Defaults to 1.
            bias (float): Bias amount of the neuron. Defaults to 0
        """
        if input_amount <= 0:
            raise Exception("input_amount must be > 0.")

        self.input_amount = input_amount
        self.bias = bias
        self.weight_list = [0] * input_amount

    def _sum_function(self, input_list: list) -> float:
        """Returns the sum value(float) of input_list[n] * weight_list[n].

        Args:
            input_list (list: floats): Input list of values to calculate

        Returns:
            float: sum value
        """

        if type(input_list) is not list:
            raise Exception("input_list is not a list")

        if len(input_list) != len(self.weight_list):
            raise Exception(
                "Length of input_list and weight_list are not the same length.")

        sum_value = self.bias
        for i in range(len(input_list)):
            sum_value += input_list[i] * self.weight_list[i]

        return sum_value

    def _activation(self, sum_value: float) -> int:
        return 1 if sum_value > 0 else 0

    def return_output(self, input_list: list) -> int:
        return self._activation(self._sum_function(input_list))
