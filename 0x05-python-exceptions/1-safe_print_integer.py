#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e))
        return False

