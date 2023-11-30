#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_arguments = len(sys.argv) - 1

    print(
            "{} argument{}.".format(
                num_arguments, ''if num_arguments == 1 else 's'
                )
            )

    for i in range(1, num_arguments + 1):
        print("{}: {}".format(i, sys.argv[i]))
