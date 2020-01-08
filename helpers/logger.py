import time


def print_no_input_passed():
    print("Warning: number of ranges should be passed")


def print_wrong_input_passed():
    print("Warning: input should include positive number representing the number of ranges")


def print_start_a_new_patch():
    print("A patch with 10 random numbers was processed. a new patch will start after 5 seconds. to Quit press Ctrl + c")
    time.sleep(5)  # Delays for 5 seconds.


def print_generate_random_ranges(number_of_ranges: int):
    print("Generating {} random ranges is being done now ...\nRanges are:".format(number_of_ranges))


def print_new_random_generated_range(range_start: int, range_end: int):
    print("[{}, {}]".format(range_start, range_end))


def print_random_generated_ranges(number_of_ranges: int):
    print("{} random ranges were generated ...".format(number_of_ranges))


def print_play_a_game_got_result(random_number: int, result: int):
    print("I played the game by {}, the result was {}!".format(random_number, result))


def print_game_start():
    print("Let the fun begins!!")
