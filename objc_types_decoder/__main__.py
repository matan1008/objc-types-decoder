import argparse

from .decode import decode


def main():
    parser = argparse.ArgumentParser(description='Parse ObjectiveC encoded types')
    parser.add_argument('encoded', help='Type to decode')
    args = parser.parse_args()
    print(decode(args.encoded))


if __name__ == '__main__':
    main()
