
from random import randint
from helpers.constants import (MIN_RANGE_VALUE,
                               MAX_RANGE_VALUE,
                               MIN_RANDOM_NUMBER_VALUE,
                               MAX_RANDOM_NUMBER_VALUE)


class NumbersGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_random(lower_limit: int, upper_limit: int):
        """
        :param lower_limit: smallest number that can be returned
        :param upper_limit: largest number that can be returned
        :return:
        """
        return randint(lower_limit, upper_limit)

    def generate_range(self):
        return self.generate_random(MIN_RANGE_VALUE, MAX_RANGE_VALUE)

    def generate_number(self):
        return self.generate_random(MIN_RANDOM_NUMBER_VALUE, MAX_RANDOM_NUMBER_VALUE)
