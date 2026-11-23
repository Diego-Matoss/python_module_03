#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Command Quest ===")

    program_name = sys.argv[0]
    print(f"Program name: {program_name}")

    argument_number = 1

    if (len(sys.argv) > 1):
        print(f"Arguments received: {len(sys.argv) - 1}")

        for argument in sys.argv[1:]:
            print(f"Argument {argument_number}: {argument}")
            argument_number += 1
    else:
        print("No arguments provided!")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
