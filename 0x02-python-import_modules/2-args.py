#!/usr/bin/python3
if __name__ == "__main__":
    """ prints the number of and the list of its arguments."""
    import sys

    num_arguments = len(sys.argv) - 1
    if num_arguments == 0:
        print("0 arguments.")
    elif num_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))
        for i in range(num_arguments):
            print("{}:{}".format(i + 1, sys.argv[i + 1]))
