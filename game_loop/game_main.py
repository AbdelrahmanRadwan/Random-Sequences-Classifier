from helpers.constants import MAX_NUMBER_OF_GAME_PATCHES, MAX_RANDOM_NUMBER_VALUE
from helpers.logger import (print_start_a_new_patch,
                            print_generate_random_ranges,
                            print_random_generated_ranges,
                            print_play_a_game_got_result,
                            print_game_start)
from helpers.numbers_generator import NumbersGenerator


class GameMain:
    def __init__(self, number_or_ranges):
        self.number_or_ranges = number_or_ranges
        self.numbers_generator = NumbersGenerator()
        self.patch_number = 1
        self.accumulated_ranges = [0] * (MAX_RANDOM_NUMBER_VALUE + 2)  # The accumulation of the ranges values

        print_generate_random_ranges(number_or_ranges)
        for range_index in range(number_or_ranges):
            lower_bound, upper_bound = self.numbers_generator.generate_range()
            self.accumulated_ranges[lower_bound] += 1  # a mark for the range start
            self.accumulated_ranges[upper_bound + 1] -= 1  # a mark for the range end
        # accumulate the ranges marks
        for index in range(1, MAX_RANDOM_NUMBER_VALUE):
            self.accumulated_ranges[index] += self.accumulated_ranges[index - 1]
        print_random_generated_ranges(number_or_ranges)

    def play(self):
        print_game_start()
        while self.patch_number <= MAX_NUMBER_OF_GAME_PATCHES:
            # Generate a random number to play

            random_number = self.numbers_generator.generate_number()
            print_play_a_game_got_result(random_number,
                                         self.accumulated_ranges[random_number])

            self.patch_number += 1
            # Await for a few seconds after each 10 numbers
            if self.patch_number % 10 == 0:
                print_start_a_new_patch()
