import importlib
#import day_3


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Run advent of code for specified day')
    parser.add_argument('day', metavar='day', type=int, choices=range(1, 25),
                        help='the day you want to process')
    parser.add_argument('--log_level', dest='set the log level for the program',
                        default='info', choices=['info', 'debug', 'warn', 'error'],
                        help='log level (default: info)')

    args = parser.parse_args()
    day: int = args.day
    print(f"Advent of code day {day}")
    mod = __import__(f'day_{day}')
    #mod = importlib.import_module(f'day_{day}', 'aoc')
    #mod.main()
    mod.main()

if __name__ == '__main__':
    main()

