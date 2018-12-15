import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Run advent of code for specified day')
    parser.add_argument('day', metavar='day', type=int, choices=range(1, 25),
                        help='the day you want to process')
    parser.add_argument('--log_level', dest='log_level',
                        default='info', choices=['info', 'debug', 'warn', 'error'],
                        help='log level (default: info)')

    args = parser.parse_args()

    log_level = args.log_level
    print(log_level)
    logging.basicConfig(level=log_level.upper())
    day: int = args.day

    logger.info(f"Advent of code day {day}")
    mod = __import__(f'day_{day}')
    mod.main()


if __name__ == '__main__':
    main()
