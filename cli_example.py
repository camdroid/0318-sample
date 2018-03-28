import argparse


def main():
    parser = argparse.ArgumentParser()

    # Add available CLI arguments
    parser.add_argument('positional', help="I'm a positional argument!")
    parser.add_argument('--optional', help="I'm an optional argument")
    parser.add_argument('--number', type=int, help="This is a number")

    args = parser.parse_args()
    print(args)
    print(args.positional)


if __name__ == '__main__':
    main()
