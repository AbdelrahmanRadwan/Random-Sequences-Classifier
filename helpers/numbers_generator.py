
from random import randint
from helpers.constants import (MIN_RANGE_VALUE,
                               MAX_RANGE_VALUE,
                               MIN_RANDOM_NUMBER_VALUE,
                               MAX_RANDOM_NUMBER_VALUE)
from helpers.logger import print_new_random_generated_range


class NumbersGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_random(lower_limit: int, upper_limit: int):
        """
        :param lower_limit: smallest number that can be returned
        :param upper_limit: largest number that can be returned
        :return: random integer in the given range inclusively
        """
        return randint(lower_limit, upper_limit)

    def generate_range(self):
        range_lower_number = self.generate_random(MIN_RANGE_VALUE, MAX_RANGE_VALUE - 1)
        range_upper_number = self.generate_random(range_lower_number, MAX_RANGE_VALUE)
        print_new_random_generated_range(range_lower_number, range_upper_number)
        return range_lower_number, range_upper_number

    def generate_number(self):
        return self.generate_random(MIN_RANDOM_NUMBER_VALUE, MAX_RANDOM_NUMBER_VALUE)
