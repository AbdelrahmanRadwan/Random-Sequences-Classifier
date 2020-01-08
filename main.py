import sys
import helpers.logger as logger
import game_loop.game_main as game
from helpers.constants import DEFAULT_NUMBER_OF_RANGES


def parse_input():
    args = sys.argv
    if len(args) < 2:
        logger.print_wrong_input_passed()
        return DEFAULT_NUMBER_OF_RANGES

    if not args[1].isdigit():
        logger.print_wrong_input_passed()
        return DEFAULT_NUMBER_OF_RANGES

    number_of_ranges = int(args[1])
    if number_of_ranges <= 0:
        logger.print_wrong_input_passed()
        return DEFAULT_NUMBER_OF_RANGES

    return number_of_ranges


if __name__ == "__main__":
    """
    Game main
    """
    number_or_ranges = parse_input()
    game_loop = game.GameMain(number_or_ranges)
    game_loop.play()
